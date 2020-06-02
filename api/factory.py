#!/usr/bin/env python
# https://flask.palletsprojects.com/en/1.1.x/patterns/celery/


import os
from flask import Flask
from celery import Celery
from api.config import base_config


class Server:
    """Build an instance for API Server"""

    def __init__(self, devmode='production'):
        if os.getenv('SERVER_ENV'):
            self._config = os.getenv('DEVMODE')
        else:
            self._devmode = devmode

    @property
    def env(self):
        return self._devmode

    @env.setter
    def env(self, devmode):
        self._devmode = devmode

        self.flask_app.config.from_object(base_config[self._devmode])
        self.celery_app.conf.update(self.flask_app.config)

    def run_flask(self, **kwargs):
        self.flask_app = Flask(__name__, **kwargs)
        self.flask_app.config.from_object(base_config[self._devmode])

        # Swagger documentation
        self.flask_app.config.SWAGGER_UI_DOC_EXPANSION = 'list'
        self.flask_app.config.SWAGGER_UI_JSONEDITOR = True

        return self.flask_app

    def run_celery(self, **kwargs):
        self.celery_app = Celery(__name__, **kwargs)
        self.celery_app.conf.update(self.flask_app.config)

        return self.celery_app

    def register_flask_blueprint(self, blueprint):
        self.flask_app.register_blueprint(blueprint)
