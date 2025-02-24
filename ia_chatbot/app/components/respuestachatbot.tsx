import axios from "axios";

async function respuestachatbot(mensaje: string) {
  try {
    const response = await axios.post('http://192.168.128.82:5005/webhooks/rest/webhook', {
      message: mensaje, 
    });

    if (response.data && response.data.length > 0) {

      return response.data[0].text || "Sin respuesta";
    } else {
      return "Sin respuesta del chatbot";
    }
  } catch (error) {
    console.error("Error en la llamada API:", error);
    return "Error al obtener respuesta";
  }
}

export default respuestachatbot;
