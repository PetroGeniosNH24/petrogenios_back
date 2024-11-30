
from hackaton_api.config.config import HEADER_DATABRICK, URL_DATABRICK
import requests
import json
import copy

class SimplificatorService:
    def __init__(self, prompt, text):
        self.prompt_model = prompt
        self.text = text
        self.url = URL_DATABRICK
        self.headers = HEADER_DATABRICK
    
    def simplify(self):
        prompt = copy.deepcopy(self.prompt_model)
        prompt["messages"].append({"role": "user", "content": self.text})

        try:
            response = requests.post(URL_DATABRICK, headers=HEADER_DATABRICK, data=json.dumps(prompt))
            if response.status_code != 200:
                return {
                    "message": "Sin permisos para acceder al modelo"
                    }
            response_json = response.json()
        except Exception as e:
            return {
                "message": "Fallo al conectar con el modelo"
            }

        response_json = self.translate_result_model(response_json)
        return {
            "message": response_json
        }

    def translate_result_model(self, result_model):
        response_model = ""
        try:
            response_model = result_model.get("choices")[0].get("message").get("content")
        except Exception as e:
            response_model = "No se pudo obtener la respuesta del modelo"
        return response_model
