from rasa_sdk import Action
from rasa_sdk.events import ActiveLoop
from rasa_sdk.events import SlotSet,FollowupAction


class GuardarProblema(Action):
    def name(self):
        return "cambio_problema"

    def run(self, dispatcher, tracker, domain):
        respuesta = tracker.get_slot('siono')
        
        if(respuesta == "no"):
            return [FollowupAction("action_crear_ticket_helpdesk")]
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
    

class ActionDespedir(Action):
    def name(self):
        return "action_crear_ticket_helpdesk"

    def run(self, dispatcher, tracker, domain):
        return [FollowupAction("utter_drop_info")]
    

class ActionCrearTicketHelpdesk(Action):
    def name(self):
        return "poner_siono_a_None"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("siono", None)]
  
