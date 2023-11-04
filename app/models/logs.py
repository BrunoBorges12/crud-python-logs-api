from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Log(db.Model):
    __tablename__ = 'logs'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True)
    date = db.Column(db.Date)
    time = db.Column(db.String)
    nivel = db.Column(db.String)
    text = db.Column(db.String)



    def serialize(self):
        return {
            'id': self.id,
            'number': self.number,
            'date': self.formatted_date,
            'time': self.time,
            'nivel': self.nivel,
            'text':self.text
            # Adicione outros campos se necessário
        }

    @property
    def formatted_date(self):
        # Formate a data como desejar
        return self.date.strftime("%Y-%m-%d %H:%M:%S")