import axios from "axios";

async function respuestachatbot(mensaje: string) {
  try {
    // Realiza la llamada API usando axios
    const response = await axios.post('http://localhost:5005/webhooks/rest/webhook', {
      message: mensaje, // Asegúrate de pasar el mensaje correctamente
    });

    // Verifica que haya respuesta y retorna el texto del chatbot
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
