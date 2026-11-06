"""
Lee el calendario de iCloud (enlace de "Calendario público") y guarda en
agenda.json SOLO los horarios ocupados, sin títulos ni detalles.

Uso:
    AGENDA_ICS="webcal://p..-caldav.icloud.com/published/2/..." python3 agenda/actualizar.py
    python3 agenda/actualizar.py archivo.ics      # para probar con un archivo
"""
import json
import os
import sys
import urllib.request
from datetime import datetime, time, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import icalendar
import recurring_ical_events

BASE = Path(__file__).resolve().parent.parent
ZONA = ZoneInfo(os.environ.get("ZONA_HORARIA", "America/Asuncion"))
DIAS_ATRAS, DIAS_ADELANTE = 1, 92


def leer_ics() -> bytes:
    if len(sys.argv) > 1:
        return Path(sys.argv[1]).read_bytes()
    url = os.environ.get("AGENDA_ICS", "").strip()
    if not url:
        print("Todavía no hay enlace del calendario (secreto AGENDA_ICS). No se hace nada.")
        sys.exit(0)
    if url.startswith("webcal://"):
        url = "https://" + url[len("webcal://"):]
    req = urllib.request.Request(url, headers={"User-Agent": "TattooLovers-agenda/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def a_local(v) -> datetime:
    """Fecha u hora del evento -> datetime en la zona del estudio."""
    if isinstance(v, datetime):
        return (v.replace(tzinfo=ZONA) if v.tzinfo is None else v.astimezone(ZONA)).replace(tzinfo=None)
    return datetime.combine(v, time())  # evento de día completo


def main():
    cal = icalendar.Calendar.from_ical(leer_ics())
    hoy = datetime.now(ZONA).date()
    desde, hasta = hoy - timedelta(days=DIAS_ATRAS), hoy + timedelta(days=DIAS_ADELANTE)

    bloques = []
    for ev in recurring_ical_events.of(cal).between(desde, hasta):
        if str(ev.get("TRANSP", "")).upper() == "TRANSPARENT":   # marcado como "libre"
            continue
        if str(ev.get("STATUS", "")).upper() == "CANCELLED":
            continue
        inicio = ev.decoded("DTSTART")
        todo_el_dia = not isinstance(inicio, datetime)
        ini = a_local(inicio)
        if ev.get("DTEND"):
            fin = a_local(ev.decoded("DTEND"))
        elif ev.get("DURATION"):
            fin = ini + ev.decoded("DURATION")
        else:
            fin = ini + (timedelta(days=1) if todo_el_dia else timedelta(hours=1))
        if fin <= ini:
            fin = ini + timedelta(hours=1)
        bloques.append([ini, fin])

    # unir bloques que se pisan
    bloques.sort()
    unidos = []
    for ini, fin in bloques:
        if unidos and ini <= unidos[-1][1]:
            unidos[-1][1] = max(unidos[-1][1], fin)
        else:
            unidos.append([ini, fin])

    salida = {
        "actualizado": datetime.now(ZONA).strftime("%Y-%m-%dT%H:%M"),
        "desde": desde.isoformat(),
        "hasta": hasta.isoformat(),
        "ocupado": [[i.strftime("%Y-%m-%dT%H:%M"), f.strftime("%Y-%m-%dT%H:%M")] for i, f in unidos],
    }
    destino = BASE / "agenda.json"
    anterior = json.loads(destino.read_text()) if destino.exists() else {}
    if anterior.get("ocupado") == salida["ocupado"] and anterior.get("desde") == salida["desde"]:
        print("Sin cambios en la agenda.")
        return
    destino.write_text(json.dumps(salida, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"agenda.json actualizado: {len(unidos)} bloques ocupados.")


if __name__ == "__main__":
    main()
