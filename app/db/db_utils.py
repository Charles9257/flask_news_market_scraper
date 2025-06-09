from flask_sqlalchemy import SQLAlchemy
from app.db.models import db
import os

def init_db(app):
    # Only override if it's not already set (e.g., by TestConfig)
    if 'SQLALCHEMY_DATABASE_URI' not in app.config:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
            'DATABASE_URL',
            'postgresql://postgres:9257postgres@localhost/newsdb'
        )

    db.init_app(app)

    # For testing and development environments only
    if app.config.get("TESTING") or app.config.get("ENV") == "development":
        with app.app_context():
            db.create_all()
