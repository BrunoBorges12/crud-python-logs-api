from  dotenv import load_dotenv
import os 

load_dotenv()
class  BaseConfig:
      SQLALCHEMY_DATABASE_URI = os.getenv('POSTGRES_DB')



