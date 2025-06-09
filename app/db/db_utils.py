from flask_sqlalchemy import SQLAlchemy
from app.db.models import db
import os

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://postgres:9257postgres@localhost/newsdb')
    db.init_app(app)
    with app.app_context():
        db.create_all()
