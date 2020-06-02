from flask_restful import Resource
import time
from api import factory

celery_app = factory.celery_app


class Example(Resource):
    def get(self, name):
        return {'result': name}

    def post(self):
        return {'result': 'post success'}


class AsyncExample(Resource):

    def get(self, name):
        time.sleep(17)
        return {'result': 'async get success'}

    @celery_app.task()
    def post(self):
        time.sleep(29)
        return {'result': 'async post success'}
