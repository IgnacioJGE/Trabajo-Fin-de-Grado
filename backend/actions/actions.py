import datetime
import json
from typing import Text, Any
from rasa_sdk import Action,FormValidationAction
from rasa_sdk.events import ActiveLoop,Restarted
from rasa_sdk.events import SlotSet,FollowupAction,UserUtteranceReverted
import os
import requests
from .funciones import decidir_persona_asignada,calcular_importancia,token_auth,buscarcontra
from dotenv import load_dotenv


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

    def validate_tipo_solicitud(self, slot_value, dispatcher, tracker, domain): #validación del tipo de solicitud
        if (slot_value.lower().find("etique") or slot_value.lower().find("impres") or slot_value.lower().find("equip")):
            return {"tipo_solicitud": "Equipos, etiquetadoras e impresoras"}
        elif (slot_value.lower().find("viaw")):
            return {"tipo_solicitud": "Viaweb"}
        elif (slot_value.lower().find("otr")):
            return {"tipo_solicitud": "Otros"}
        elif (slot_value.lower().find("alba")):
            return {"tipo_solicitud": "Albarán digital"}
        elif (slot_value.lower().find("clien")):
            return {"tipo_solicitud": "Clientes"}
        elif (slot_value.lower().find("desarr")):
            return {"tipo_solicitud": "Desarrollos y proyectos"}
        elif (slot_value.lower().find("padu")):
            return {"tipo_solicitud": "Padua"}
        else:
            dispatcher.utter_message(text="Lo siento, no entiendo el tipo de solicitud. Por favor, indícamelo de nuevo.")
            return {"tipo_solicitud": None}
    
    def validate_problema(self, slot_value, dispatcher, tracker, domain):
        mensaje_usuario = tracker.latest_message.get('text')
        return { "problema": mensaje_usuario }
        
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
        load_dotenv()
        ticket=tracker.get_slot("ticket")
        json_data =  await token_auth()
        headers = {
        'Authorization': "Bearer " + json_data['access_token'],
        'Accept':'application/json;odata=verbose',
        'Content-Type': 'application/json;odata=verbose'
        }
        url = os.getenv("url")  +f"({ticket})"
        p= requests.get(url, headers=headers)
        data= p.json()
        estado= data.get("d", {}).get("Estado_solicitud")
        solucion= data.get("d", {}).get("Descripci_x00f3_n_soluci_x00f3_n")
        if(str(estado)=="Finalizado"):
            dispatcher.utter_message(text="El estado de su ticket es: " + str(estado) + ".\nY la solución es: "+ str(solucion))
        elif(str(estado)=="None"):
            dispatcher.utter_message(text="No existe ningú ticket con el id: " + str(ticket))            
        else:
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
    
class buscarcontras(Action):

    def name(self):
        return "buscar_contra"

    def run(self, dispatcher, tracker, domain):
        email= tracker.get_slot("emailconductor")
        idpadua= tracker.get_slot("idpadua")
         
        contra= buscarcontra(email,idpadua)
        if contra== "id":
            dispatcher.utter_message(text="Se ha encontrado el id pero no conincide con el correo.")
            return [SlotSet("idpadua", None),
                    ActiveLoop("form_contras")]
        elif contra== "correo":
            dispatcher.utter_message(text="Se ha encontrado el correo pero no conincide con el id.")
            return [SlotSet("emailconductor", None),
                    ActiveLoop("form_contras")]
        elif str(contra)== "None":
            dispatcher.utter_message(text="No se ha encontrado un conductor con ese id ni ese correo.")
            return [SlotSet("emailconductor", None),
                    SlotSet("idpadua", None),
                    ActiveLoop("form_contras")]
        else:
            dispatcher.utter_message(text="La contraseña es: " + str(contra))
        return [SlotSet("idpadua", None),
                SlotSet("emailconductor", None)]