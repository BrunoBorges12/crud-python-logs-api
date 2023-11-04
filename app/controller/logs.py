from flask import request,make_response
from flask_restful import Resource, Api, reqparse
from ..services.LogService import LogService
from ..services.extract_logs import log_extractor
from ..utils.common import MessageGenerator
from ..utils.http_code import HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK


class Logs(Resource):
    def get(self):
        try:
            logs_ext = log_extractor()
            LogService.save_log(logs_ext)
            logs = LogService.get_logs()
            logs_ex = log_extractor()
            LogService.save_log(logs_ex)
            success_message = f"Encontrados {len(logs)} logs."
            response = MessageGenerator.generate_response(logs, success_message, HTTP_200_OK)
            return response
        except Exception as e:
            error_message = str(e)
            response = MessageGenerator.generate_response(None, error_message, HTTP_500_INTERNAL_SERVER_ERROR)
            return response

    
class LogsFilter(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('start_date', type=str, required=False)
        parser.add_argument('end_date', type=str, required=False)
        parser.add_argument('nivel', type=str, required=False)
        parser.add_argument('text', type=str, required=False)

        data = parser.parse_args()

        start_date = data['start_date']
        end_date = data['end_date']
        pattern = data['nivel']
        relatorio = data['text']


        try:
            logs = LogService.filter_logs_by_date_and_content(start_date, end_date, pattern,relatorio)
            serialized_logs = [log.serialize() for log in logs]
            return MessageGenerator.generate_response(serialized_logs, '', HTTP_200_OK)
        except Exception as e:
            error_message = str(e)
            response = MessageGenerator.generate_response(None, error_message, HTTP_500_INTERNAL_SERVER_ERROR)
            return response