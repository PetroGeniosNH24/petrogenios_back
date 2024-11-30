from flask import request
from flask_restx import Resource, Namespace

from hackaton_api.config.config import PROMT_DATABRICK_TAREAS, PROMT_DATABRICK_TEXT_HTML, PROMT_DATABRICK_TEXT
from hackaton_api.service.simplificator_service import SimplificatorService

api = Namespace('simplificator', description='Status operations')

class SimplificatorTaskEndpoint(Resource):
    """
    Endpoint that returns the status of the api to allow knows that
    are working ok.
    """

    def post(self):
        """
        Endpoint to return an ok status
        :return: a 200 code with json message with status up!
        """
        #_LOGGER.info("%s - %s", request.path, request.method)
        data = request.get_json()
        
        simplificador_service = SimplificatorService(prompt=PROMT_DATABRICK_TAREAS, text=data.get("text",""))
        return simplificador_service.simplify()
    

class SimplificatorTextEndpoint(Resource):
    """
    Endpoint that returns the status of the api to allow knows that
    are working ok.
    """

    def post(self):
        """
        Endpoint to return an ok status
        :return: a 200 code with json message with status up!
        """
        #_LOGGER.info("%s - %s", request.path, request.method)
        
        prom_tareas={"text_html":PROMT_DATABRICK_TEXT_HTML, "text":PROMT_DATABRICK_TEXT}
        data = request.get_json()
        simplificador_service = SimplificatorService(prompt=prom_tareas[data.get("promt")], text=data.get("text",""))
        return simplificador_service.simplify()


api.add_resource(SimplificatorTaskEndpoint, "/task")
api.add_resource(SimplificatorTextEndpoint, "/text")