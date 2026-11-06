/**
 * Tattoo Lovers – guarda cada cotización en esta hoja de Google.
 * Pega este código en Extensiones → Apps Script de tu hoja (ver LEEME.md).
 */
const HOJA = "Clientes";
const COLUMNAS = ["Fecha", "Nombre", "WhatsApp", "Zona", "Tamaño", "Medida marcada",
                  "Estilo", "Idea", "Acepta promociones"];

function doPost(e) {
  const d = JSON.parse(e.postData.contents);
  const libro = SpreadsheetApp.getActiveSpreadsheet();
  let hoja = libro.getSheetByName(HOJA);
  if (!hoja) {
    hoja = libro.insertSheet(HOJA);
    hoja.appendRow(COLUMNAS);
    hoja.setFrozenRows(1);
  }
  const campos = ["nombre", "telefono", "zona", "tamano", "medida", "estilo", "idea", "promos"];
  hoja.appendRow([new Date()].concat(campos.map(k => limpiar(d[k]))));
  return ContentService.createTextOutput("ok");
}

// Evita textos larguísimos y que algo escrito por el cliente se tome como fórmula.
function limpiar(valor) {
  let t = String(valor == null ? "" : valor).slice(0, 500);
  if (/^[=+\-@]/.test(t)) t = "'" + t;
  return t;
}
