from rasa_sdk import Action
from rasa_sdk.events import ActiveLoop

class ActivarFormulario(Action):
    def name(self):
        return "action_activar_formulario"

    def run(self, dispatcher, tracker, domain):
            return [ActiveLoop("formulario_nombre_delegacion")]

  
