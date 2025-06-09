from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from app.db import models  # Import models so they're registered with SQLAlchemy
