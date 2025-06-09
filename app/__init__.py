from flask import Flask
from app.config import Config
from app.db.db_utils import init_db
from app.db.db_utils import db  # Import the db object
from app.api.routes import api_bp  # your existing API blueprint
from app.main.routes import main_bp  # your new blueprint

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)  # Initialize the database with the app

    app.register_blueprint(api_bp, url_prefix='/api')
    init_db(app)
    app.register_blueprint(main_bp, url_prefix='/')# Register the main blueprint
   
    

 

    return app
