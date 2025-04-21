import datetime
import json
from typing import Text, Any
from rasa_sdk import Action,FormValidationAction
from rasa_sdk.events import ActiveLoop,Restarted
from rasa_sdk.events import SlotSet,FollowupAction,UserUtteranceReverted
import os
import requests
from .funciones import decidir_persona_asignada,calcular_importancia,token_auth
from dotenv import load_dotenv
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ValidateFormHelpedesk(FormValidationAction):
    def name(self) -> Text:
        return "validate_form_helpedesk"
    

    def validate_siono(self, slot_value: Any, dispatcher, tracker, domain):
        if slot_value.lower() == "no":
            dispatcher.utter_message(text="De acuerdo, finalizamos el formulario.")
            return {"siono": "no"}
        elif slot_value.lower() == "si" or slot_value.lower() == "sí":
            # Reinicia solo el slot problema
            return {"siono": "sí", "problema": None, "requested_slot": "problema"}
        else:
            return{}
        
    def validate_nombre(self, slot_value, dispatcher, tracker, domain):
            return [
                SlotSet("siono", None),
                SlotSet("problema", None),
                SlotSet("departamento", None),
                SlotSet("email", None),
                SlotSet("tipo_solicitud", None),
                SlotSet("importancia", None),
                SlotSet("ticket", None),
                SlotSet("nombre", slot_value) 
            ]

class GuardarProblema(Action): #Legado esta funcion se mejoró con la validación
    def name(self):
        return "cambio_problema"

    def run(self, dispatcher, tracker, domain):
        respuesta = tracker.get_slot('siono')
        
        if(respuesta == "no"):
            return [ActiveLoop(None)]
        else:
            return [
                SlotSet("problema", None),
                SlotSet("siono", "no"),
                ActiveLoop("form_helpedesk")
            ]

class Crearticket(Action):
    def name(self):
        return "action_crear_ticket_helpdesk"

    async def run(self, dispatcher, tracker, domain):
        load_dotenv()
        nombre = tracker.get_slot("nombre")
        delegacion = tracker.get_slot("delegacion")
        departamento = tracker.get_slot("departamento")
        tipo_solicitud = tracker.get_slot("tipo_solicitud")
        problema= tracker.get_slot("problema")
        correo = tracker.get_slot("email")
        importancia = tracker.get_slot("importancia")
        url=os.getenv("url")

        json_data = await token_auth()
        headers = {
            'Authorization': "Bearer " + json_data['access_token'],
            'Accept':'application/json;odata=verbose',
            'Content-Type': 'application/json;odata=verbose'
        }
        fecha = datetime.datetime.now()
        dato = {
            '__metadata': {"type": "SP.Data.BBDD_x0020_HelpDeskListItem"},
            'Estado_solicitud': "Registrado",
            'Delegacion': delegacion,
            'Nombre_Apellido': nombre,
            'Tipo_Solicitud': tipo_solicitud,
            'Correo_electronico': correo,
            'Area_consulta': departamento,
            'Detalles_consulta': problema,
            'Criticidad': importancia,
            'Persona_Asignada': "",
            'Fecha_solicitud': fecha.isoformat()
        }
        Persona_asignada= decidir_persona_asignada(tipo_solicitud)
        dato["Persona_Asignada"] = Persona_asignada
        importancia= calcular_importancia(importancia)
        dato["Criticidad"]= importancia
        data=json.dumps(dato)
        p= requests.post(url, headers=headers,data=data)
        data= p.json()
        id= data.get("d", {}).get("ID")
        dispatcher.utter_message(text="Perfecto ya se ha enviado su ticket, el id es: " + str(id))
        return [Restarted()]

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

class reset(Action):


    def name(self):
        return "resetear_slots"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("siono", None),
                SlotSet("problema", None),
                SlotSet("departamento", None),
                SlotSet("email", None),
                SlotSet("tipo_solicitud", None),
                SlotSet("importancia", None),
                SlotSet("ticket", None),
        ]

class sionoaNone(Action):

    def name(self):
        return "poner_siono_a_None"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("siono", None)]

class Estadoticket(Action):
    def name(self):
        return "action_estado_ticket"

    async def run(self, dispatcher, tracker, domain):
        ticket=tracker.get_slot("ticket")
        json_data =  await token_auth()
        headers = {
        'Authorization': "Bearer " + json_data['access_token'],
        'Accept':'application/json;odata=verbose',
        'Content-Type': 'application/json;odata=verbose'
        }
        url=f"https://te917868526.sharepoint.com/sites/SistemaHelpdesk/_api/web/lists/getbytitle('BBDD Sistemas')/items({ticket})"
        p= requests.get(url, headers=headers)
        data= p.json()
        estado= data.get("d", {}).get("Estado_solicitud")
        dispatcher.utter_message(text="El estado de su ticket es: " + str(estado))
        return []

class ActionPruebas(Action):
    def name(self):
        return "action_pruebas"

    async def run(self, dispatcher, tracker, domain):
        load_dotenv()
        nombre = tracker.get_slot("nombre")
        delegacion = tracker.get_slot("delegacion")
        departamento = tracker.get_slot("departamento")
        tipo_solicitud = tracker.get_slot("tipo_solicitud")
        problema= tracker.get_slot("problema")
        correo = tracker.get_slot("email")
        importancia = tracker.get_slot("importancia")
        url=os.getenv("url")

        json_data = await token_auth()
        headers = {
            'Authorization': "Bearer " + json_data['access_token'],
            'Accept':'application/json;odata=verbose',
            'Content-Type': 'application/json;odata=verbose'
        }
        fecha = datetime.datetime.now()
        dato = {
            '__metadata': {"type": "SP.Data.BBDD_x0020_HelpDeskListItem"},
            'Estado_solicitud': "Registrado",
            'Delegacion': delegacion,
            'Nombre_Apellido': nombre,
            'Tipo_Solicitud': tipo_solicitud,
            'Correo_electronico': correo,
            'Area_consulta': departamento,
            'Detalles_consulta': problema,
            'Criticidad': importancia,
            'Persona_Asignada': "",
            'Fecha_solicitud': fecha.isoformat()
        }
        Persona_asignada= decidir_persona_asignada(tipo_solicitud)
        dato["Persona_Asignada"] = Persona_asignada
        importancia= calcular_importancia(importancia)
        dato["Criticidad"]= importancia
        data=json.dumps(dato)
        p= requests.post(url, headers=headers,data=data)
        data= p.json()
        id= data.get("d", {}).get("ID")
        dispatcher.utter_message(text="Perfecto ya se ha enviado su ticket, el id es: " + str(id))
        return []
    
