from flask import make_response,jsonify
class MessageGenerator:
    @staticmethod
    def generate_response(data=None, message=None, status=400):
        response = {
            "data": data,
            "message": message if message else ErrorFormatter.format_error(message, status),
            "status": status in (200, 201)
        }
        return make_response(jsonify(response), status)

class ErrorFormatter:
    @staticmethod
    def format_error(message, status):
        if message:
            return ErrorFormatter._parse_message(message, status)
        return None

    @staticmethod
    def _parse_message(message, status):
        if isinstance(message, str):
            return [{"error": message}] if status != 200 else message
        elif isinstance(message, list):
            return message
        elif isinstance(message, dict):
            return [{"error": f"{key}: {value[0]}" for key, value in message.items()}]