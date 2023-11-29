from application import app
from config import config_mapping
from app.model.log_model import db

app.config.from_object(config_mapping.config) # configura a aplicação de acordo com ambiente
db.init_app(app) #  configura o banco de dados de acordo com uri do env

if  __name__ == "__main__":
    with app.app_context():
    
        try:
            result =  db.session()
            db.create_all()
            print('banco conectado com sucesso') 
        except Exception as e:
            print('Não foi possivel conectar no  banco erro' ,e)
                      
    app.run()