from flask_restx import Resource, Namespace

api = Namespace('status', description='Status operations')

class StatusEndpoint(Resource):
    """
    Endpoint that returns the status of the api to allow knows that
    are working ok.
    """

    def get(self):
        """
        Endpoint to return an ok status
        :return: a 200 code with json message with status up!
        """
        #_LOGGER.info("%s - %s", request.path, request.method)

        return {
            "status": "Up!"
        }


api.add_resource(StatusEndpoint, "")