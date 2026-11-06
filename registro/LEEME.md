# Guardar los datos de los clientes en Google Sheets

Cada vez que un cliente toca "Enviar cotización por WhatsApp", se agrega una fila
en una hoja de Google con: fecha, nombre, WhatsApp, zona, tamaño, medida, estilo,
idea y si acepta recibir promociones.

## Pasos (una sola vez, ~5 minutos)

1. Entra a https://sheets.new (crea una hoja nueva). Ponle de nombre "Clientes Tattoo Lovers".
2. Menú **Extensiones → Apps Script**.
3. Borra lo que aparece y pega todo el contenido de `registro/codigo.gs`. Guarda (ícono del disquete).
4. Arriba a la derecha: **Implementar → Nueva implementación**.
   - Tipo (rueda ⚙️): **Aplicación web**.
   - Ejecutar como: **Yo**.
   - Quién tiene acceso: **Cualquier persona**.
   - Toca **Implementar** y acepta los permisos de Google
     (si dice "Google no verificó esta app": *Configuración avanzada → Ir a … (no seguro)*; es tu propio código).
5. Copia la **URL de la aplicación web** (termina en `/exec`) y pégala en `tattoolover.py`:
   `REGISTRO_URL = "https://script.google.com/macros/s/..../exec"`
6. Regenera la página: `python3 web/generar.py` y sube los cambios.

## Importante

- Envía promociones **solo** a quienes tienen "Sí" en "Acepta promociones".
- La hoja es tuya y privada: solo la ven las personas con las que la compartas.
