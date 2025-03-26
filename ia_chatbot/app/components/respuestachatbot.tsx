import axios from "axios";
import { text } from "stream/consumers";


async function respuestachatbot(mensaje: string,sesion: string) {
  try {
        const response = await axios.post('http://192.168.128.123:5005/webhooks/rest/webhook', {
        sender: sesion,
        message: mensaje, 
      });
    
    if (response.data && response.data.length > 0) {
      console.log(response)
      return response.data;
    } else {
      return [{text:"Sin respuesta del chatbot"}];
    }
  } catch (error) {
    console.error("Error en la llamada API:", error);
    return [{text:"Error al obtener respuesta"}];
  }
}

export default respuestachatbot;
