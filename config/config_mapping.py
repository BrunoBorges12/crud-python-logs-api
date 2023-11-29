import os 
from .dev_config import DevelopmentConfig
from .prod_config import ProductionConfig

config_mapping = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

app_env = os.getenv('FLASK_ENV', 'default')
config = config_mapping.get(app_env )

