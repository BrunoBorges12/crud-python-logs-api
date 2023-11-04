from flask import Flask
from flask_restful import Resource, Api, reqparse
from  app.controller.logs import Logs,LogsFilter


app = Flask(__name__)

@app.after_request

def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response
api = Api(app)
api.add_resource(Logs, '/api/logs')
api.add_resource(LogsFilter, '/api/logs/filter')

