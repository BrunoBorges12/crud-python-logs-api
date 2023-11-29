from application import app
from config import config_mapping

app.config.from_object(config_mapping.config)
    
if  __name__ == "__main__":
    app.run()