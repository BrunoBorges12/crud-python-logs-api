from flask_restful import Resource
from ..utils.common import MessageGenerator
from flask import make_response,jsonify


class Logs(Resource):
    def get(self):
        return  make_response('ssssss')