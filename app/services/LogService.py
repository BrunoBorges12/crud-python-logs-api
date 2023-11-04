from ..models.logs import Log, db 

class LogService:
    @staticmethod
    def save_log(logs):
        
        saved_logs = []

        for log in logs:
            existing_log = Log.query.filter_by(number=log['number']).first()

            if not existing_log:
                new_log = Log(number=log['number'], date=log['data'], time=log['hora'], text=log['texto'], nivel=log['nivel'])
                db.session.add(new_log)

                saved_logs.append({
                    'number': new_log.number,
                    'date': new_log.date,
                    'time': new_log.time,
                    'text': new_log.text,
                    'nivel': new_log.nivel
                })
            
            db.session.commit() 
      
        return saved_logs
    def get_logs():        
        logs = Log.query.all()
        serialized_logs = [log.serialize() for log in logs]  
        return serialized_logs
    def filter_logs_by_date_and_content(start_date=None, end_date=None, nivel=None, text=None):
        if start_date and end_date and nivel and text:
            # Filtrar por data, nível e texto
            logs = Log.query.filter(
                Log.date >= start_date,
                Log.date <= end_date,
                Log.nivel.ilike(f'%{nivel}%'),
                Log.text.ilike(f'%{text}%')
            ).all()
        elif start_date and end_date and nivel:
            # Filtrar por data e nível
            logs = Log.query.filter(
                Log.date >= start_date,
                Log.date <= end_date,
                Log.nivel.ilike(f'%{nivel}%')
            ).all()
        elif start_date and end_date and text:
            # Filtrar por data e texto
            logs = Log.query.filter(
                Log.date >= start_date,
                Log.date <= end_date,
                Log.text.ilike(f'%{text}%')
            ).all()
        elif nivel and text:
            # Filtrar por nível e texto
            logs = Log.query.filter(
                Log.nivel.ilike(f'%{nivel}%'),
                Log.text.ilike(f'%{text}%')
            ).all()
        elif start_date and end_date:
            # Filtrar por data apenas
            logs = Log.query.filter(
                Log.date >= start_date,
                Log.date <= end_date
            ).all()
        elif nivel:
            # Filtrar por nível apenas
            logs = Log.query.filter(Log.nivel.ilike(f'%{nivel}%')).all()
        elif text:
            # Filtrar por texto apenas
            logs = Log.query.filter(Log.text.ilike(f'%{text}%')).all()
        else:
            # Se nenhum critério for fornecido, retorna todos os registros
            logs = Log.query.all()

        return logs