from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder="templates")

    app.config.from_object('config.Config')

    db.init_app(app)
    CORS(app)

    with app.app_context():
        from . import routes
        db.create_all()

    return app
