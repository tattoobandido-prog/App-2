# Mostrar la agenda del mes (Google Calendar)

Los clientes ven qué horarios están ocupados y cuáles libres, sin detalles,
y no pueden modificar nada. Se actualiza sola cuando cambias tu calendario.

## Pasos (una sola vez, desde una computadora: calendar.google.com)

1. A la izquierda, junto a "Otros calendarios" o "Mis calendarios", toca **+ → Crear calendario**.
   Nombre: **Agenda Tattoo Lovers** → Crear calendario.
   (Así tus eventos personales no aparecen en la página.)
2. Abre la **configuración** de ese calendario (los tres puntitos → Configuración y uso compartido).
3. En **"Permisos de acceso a eventos"** marca **"Hacer que esté disponible para el público"**
   y elige **"Ver solo libre/ocupado (ocultar detalles)"**.
4. Baja hasta **"Integrar el calendario"** y copia el **ID del calendario**
   (algo como `abc123...@group.calendar.google.com`).
5. Pégalo en `tattoolover.py`:  `AGENDA_ID = "abc123...@group.calendar.google.com"`
   y regenera la página con `python3 web/generar.py`.

Después, cada turno que anotes en "Agenda Tattoo Lovers" aparece como ocupado en la página.
