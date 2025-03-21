from rasa_sdk import Action
from rasa_sdk.events import ActiveLoop
from rasa_sdk.events import SlotSet


class GuardarProblema(Action):
    def name(self):
        return "action_guardar_problema"

    def run(self, dispatcher, tracker, domain):
        ultimo_problema = tracker.latest_message.get('text')
        return [SlotSet("problema,", ultimo_problema)]

class CrearentradaSharepoint(Action):
    def name(self):
        return "action_crear_entrada_sharepoint"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Creando entrada en Sharepoint")
        return []


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
  
