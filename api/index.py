from flask import Flask, g
from api.config import Config
from api.extensions.database import Database
from api.main import main_blueprint
from api.auth import auth_blueprint

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

app: Flask = create_app()

if __name__ == "__main__":
	app.run(port=4000, host="0.0.0.0", debug=True)