from flask import Flask, g
from config import Config
from extensions.database import Database
from main import main_blueprint
from auth import auth_blueprint

def create_app() -> Flask:
   app = Flask(__name__)
   config: Config = Config()
   app.config.from_object(config)

   database: Database = Database(config)

   @app.before_request
   def before_request():
      g.database: Database = database

   app.register_blueprint(main_blueprint, url_prefix="/")
   app.register_blueprint(auth_blueprint, url_prefix="/auth")

   return app