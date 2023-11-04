from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    DEBUG = True
    TESTING = False
    LOG_FILE = 'server_logs.log'
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@"
        f"db/{os.getenv('POSTGRES_DB')}"
    )

class ProductionConfig(Config):
    DEBUG = True

class DevelopmentConfig(Config):
        pass

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    LOG_FILE = 'test_logs.log'

config_mapping = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig  # Configuração padrão
}

app_env = os.getenv('FLASK_ENV', 'development')
config = config_mapping.get(app_env, DevelopmentConfig)
