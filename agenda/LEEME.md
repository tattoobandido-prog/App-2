# Agenda del mes (Google Calendar o calendario del iPhone)

La página muestra un calendario del mes con los días **libres**, **con lugar** y **ocupados**.
Solo se publican los horarios ocupados: **nunca** los nombres ni los detalles de tus turnos.
Tú anotas los turnos en tu calendario como siempre; la página se actualiza sola
cada 30 minutos (GitHub lo hace automáticamente con `.github/workflows/agenda.yml`).

## Pasos (una sola vez)

### 1a. Con Google Calendar (recomendado)
1. Entra a **calendar.google.com** (en el celular: abre el navegador y pide la "versión para computadora").
2. ⚙️ **Configuración** → a la izquierda, en "Configuración de mis calendarios", toca tu calendario
   (o uno aparte, por ejemplo "Turnos Tattoo Lovers").
3. Baja hasta **"Integrar el calendario"** → **"Dirección secreta en formato iCal"** → copia el enlace.
   No hace falta hacer público el calendario.

### 1b. Con el calendario del iPhone (iCloud)
1. Abre la app **Calendario** → toca **Calendarios** (abajo).
2. Toca la **ⓘ** junto al calendario donde anotas los turnos (tiene que estar en **iCloud**).
3. Activa **Calendario público** → toca **Compartir enlace…** → **Copiar**.

> Recomendado: crea un calendario aparte, por ejemplo "Turnos Tattoo Lovers", solo para los
> tatuajes. Así tus cosas personales no cuentan como "ocupado".

### 2. En GitHub: guardar el enlace como secreto
1. Entra a https://github.com/tattoobandido-prog/App-2/settings/secrets/actions
2. **New repository secret** → Name: `AGENDA_ICS` → Secret: pega el enlace → **Add secret**.

### 3. Primera actualización
https://github.com/tattoobandido-prog/App-2/actions/workflows/agenda.yml → **Run workflow**.
En 1–2 minutos aparece la agenda en la página.

## Ajustes
- Horario de trabajo (para decidir si un día está libre o lleno): `HORARIO_INICIO` y `HORARIO_FIN`
  en `tattoolover.py`. Después: `python3 web/generar.py`.
- Un evento marcado como **"Libre"** en el iPhone (Mostrar como: Libre) no bloquea el horario.
