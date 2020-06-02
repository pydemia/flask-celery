from flask import request
from flask_restful import Resource, reqparse
from api import factory
from ._imple_inference import request


celery_app = factory.celery_app

__all__ = ['Predict', 'Explain', 'AsyncPredict', 'AsyncExplain']

# For GET: location='args'
# For POST: location='form'
post_parser = reqparse.RequestParser()
post_parser.add_argument('instances', location='form')
post_parser.add_argument('model_name', type=str, default='mobilenet-fullstack', location='form')
post_parser.add_argument('namespace', type=str, default='ifsvc', location='form')


class Predict(Resource):
    # def post(self, predict):
    def post(self):
        post_args = post_parser.parse_args()
        INSTANCES = post_args['instances']
        MODEL_NAME = post_args['model_name']
        NAMESPACE = post_args['namespace']

        # json_data = request.get_json(force=True)
        # INSTANCES = json_data['instances']
        # MODEL_NAME = json_data.get('model_name', 'mobilenet-fullstack')
        # NAMESPACE = json_data.get('namespace', 'ifsvc')

        CLUSTER_IP = '104.198.233.27'
        HOSTNAME = f'{MODEL_NAME}.{NAMESPACE}.{CLUSTER_IP}.xip.io'
        res = request(
            instances=INSTANCES,
            cluster_ip=CLUSTER_IP,
            hostname=HOSTNAME,
            model_name=MODEL_NAME,
            op='predict',
        )
        return res, 200


class AsyncPredict(Predict):
    @celery_app.task()
    def post(self):
        return super(AsyncPredict, self).post()


class Explain(Resource):
    # def post(self, predict):
    def post(self):
        post_args = post_parser.parse_args()
        INSTANCES = post_args['instances']
        MODEL_NAME = post_args['model_name']
        NAMESPACE = post_args['namespace']

        # json_data = request.get_json(force=True)
        # INSTANCES = json_data['instances']
        # MODEL_NAME = json_data.get('model_name', 'mobilenet-fullstack')
        # NAMESPACE = json_data.get('namespace', 'ifsvc')

        CLUSTER_IP = '104.198.233.27'
        HOSTNAME = f'{MODEL_NAME}.{NAMESPACE}.{CLUSTER_IP}.xip.io'

        res = request(
            instances=INSTANCES,
            cluster_ip=CLUSTER_IP,
            hostname=HOSTNAME,
            model_name=MODEL_NAME,
            op='explain',
        )
        return res, 200


class AsyncExplain(Explain):
    @celery_app.task()
    def post(self):
        return super(AsyncExplain, self).post()


# URL = os.path.join('/v1/models', MODEL_NAME + '<string:predict>')
