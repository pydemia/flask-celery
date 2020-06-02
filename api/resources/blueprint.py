from flask_restful import Resource


class BluePrintResource(Resource):
    def get(self, name):
        return {'result': name}
