from flask import Flask
from flask_cors import CORS

from flask_restx import Api as Swagger
from hackaton_api.controller.status_controller import api as status_controller
from hackaton_api.controller.simplificator_controller import api as simplificator_controller



def create_app():
    _app = Flask(__name__)
    CORS(_app)
    authorization = {
        'bearerToken': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    }

    base_path = ""
    api_prefix = "petrogenios"
    if api_prefix:
        if not api_prefix.startswith('/'):
            base_path += "/"
        base_path += api_prefix

    _app.config["SWAGGER_BASEPATH"] = base_path

    app_server = Swagger(_app, version="1.0.0",
                         title="PetroGenios API",
                         description="",
                         validate=True,
                         authorizations=authorization)
    
    app_server.add_namespace(status_controller)
    app_server.add_namespace(simplificator_controller)

    return _app, app_server
