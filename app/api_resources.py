from flask import request
from flask_restful import Resource
from .functions import *
from app import app
from flask_restful import Api


api = Api(app)


class GetInfo(Resource):
    def post(self):
        json = request.get_json()
        email(json)
        telegram(json)
        return {'got info': json}, 201


api.add_resource(GetInfo, '/')
