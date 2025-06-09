from flask import Flask
from app.config import Config
 
from app.db.db_utils import init_db
from app.api.routes import api_bp  # your existing API blueprint
from app.main.routes import main_bp  # your new blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(api_bp, url_prefix='/api')
    init_db(app)
    app.register_blueprint(main_bp, url_prefix='/')# Register the main blueprint
   
    
    


    return app
