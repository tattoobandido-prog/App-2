# Tattoo Lovers – Cotizador de tatuajes

El cliente elige la zona del cuerpo (de frente o de espalda), marca el tamaño con el dedo,
elige un estilo y envía la cotización a WhatsApp.

## Dos formas de usarla

**1. Página web simple (GitHub Pages)** – `index.html`
Settings → Pages → *Deploy from a branch* → `main` / `(root)` → Save.
Queda en: https://tattoobandido-prog.github.io/App-2/

**2. App de Streamlit** – `tattoolover.py`
En https://share.streamlit.io → Create app → repositorio `tattoobandido-prog/App-2`,
rama `main`, archivo `tattoolover.py`.

## Cambiar cosas

- Número de WhatsApp, estilos y tamaños: al principio de `tattoolover.py`.
- Fotos de los estilos: carpeta `estilos/`.
- Después de cambiar algo, regenera la página web con `python3 web/generar.py`.
