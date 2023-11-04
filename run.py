from app.app import app
from config.settings import config
from dotenv import load_dotenv
from app.models.logs import db

# Carregar variáveis de ambiente
load_dotenv()

# Configurar a aplicação com as configurações de ambiente
app.config.from_object(config)
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        
        db.create_all()
    app.run(host='0.0.0.0', port='5000')

