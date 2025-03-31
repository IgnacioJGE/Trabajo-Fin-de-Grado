from rasa_sdk import Action
from rasa_sdk.events import ActiveLoop
from rasa_sdk.events import SlotSet,FollowupAction,UserUtteranceReverted
import msal
from dotenv import load_dotenv
import os
import requests


class GuardarProblema(Action):
    def name(self):
        return "cambio_problema"

    def run(self, dispatcher, tracker, domain):
        respuesta = tracker.get_slot('siono')
        
        if(respuesta == "no"):
            return []
        else:
            return [
                SlotSet("problema", None),
                SlotSet("siono", "no"),
                ActiveLoop("form_helpedesk")
            ]


class ActionSaludarPersonalizado(Action):
    def name(self):
        return "action_saludar_personalizado"

    def run(self, dispatcher, tracker, domain):
        nombre = tracker.get_slot("nombre")

        if nombre:
            dispatcher.utter_message(text=f"Hola {nombre}, ¿en qué puedo ayudarte?")
        else:
            dispatcher.utter_message(text="Hola, ¿cómo puedo ayudarte?")
        
        return []
    

class CrearTicket(Action):
    def name(self):
        return "action_crear_ticket_helpdesk"

    def run(self, dispatcher, tracker, domain):
        client_id = os.getenv("client_id")
        client_secret = os.getenv("client_secret")
        tenant_id = os.getenv("tenant_id")
        scope = os.getenv("scope")
        site_url = os.getenv("helpdesk_url")
        list_name = os.getenv("helpdesk_list")
        
        
        app = msal.ConfidentialClientApplication(
            client_id,
            authority=f"https://login.microsoftonline.com/{tenant_id}",
            client_credential=client_secret
            )
        token_response = app.acquire_token_for_client(scopes=scope)
        access_token = token_response.get('access_token')
        url = f"{site_url}/_api/web/lists/getbytitle('{list_name}')/items"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
            }
        data = {
            "Estado_Solicitud": "Registrado",  # Título de la entrada (debe coincidir con el nombre del campo en la lista)
            "Delegacion": "Prueba",
            "Nombre_Apellido": "Ignacio",
            "Departamento": "Proyectos y Sistemas",
            "Tipo_Solicitud": "Equipos, etiquetadoras e impresoras",
            "Detalles_solicitud": "Prueba",
            "Importancia": "Mínima",
            "Correo": "ignacio.garcia@narval.es"
        }
        response = requests.post(url, headers=headers, json=data)
        
        dispatcher.utter_message(text="Perfecto ya se ha enviado tu ticket, en breve nos pondremos en contacto")
        return [FollowupAction("utter_drop_info")]
    

class SionoaNone(Action):
    def name(self):
        return "poner_siono_a_None"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("siono", None)]
  
