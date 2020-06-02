"""Initialization module of Resources.
"""
# Flask based imports
from flask import Blueprint
from flask_restful import Api
# from flask_restful import reqparse, abort, Api, Resource

# Api based imports
from api.config import Config

# Resources based imports
#from api.resources.tasks import api as main

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

# API instantiation
api = Api(
    api_blueprint,
    title=Config.TITLE,
    version=Config.VERSION,
    description=Config.DESCRIPTION,
)

# Namespaces registration
# api.add_namespace(main, path='')

from api.resources.math import Example, AsyncExample
from api.resources.inference import (Predict, Explain,
                                     AsyncPredict, AsyncExplain)


api.add_resource(Example, '/example')
api.add_resource(AsyncExample, '/asyncexample')

api.add_resource(Predict, '/predict')
api.add_resource(Explain, '/explain')
api.add_resource(AsyncPredict, '/asyncpredict')
api.add_resource(AsyncExplain, '/asyncexplain')
