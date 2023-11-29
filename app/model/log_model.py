from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Log(db.Model):
    __tablename__ = 'logs'
    
    id = db.Column(db.Integer, primary_key=True)
    serie = db.Column(db.Integer, unique=True)
    start_date  = db.Column(db.Date)
    end_date = db.Column(db.Date)
    level = db.Column(db.String)
    text = db.Column(db.String)

