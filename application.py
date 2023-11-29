from  flask import  Flask

from flask_restful import Api
from app.controller.logs import Logs

app = Flask(__name__)
api =  Api(app)
api.add_resource(Logs,'/api/logs')