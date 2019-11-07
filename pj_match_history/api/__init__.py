# from functools import wraps
# from flask import jsonify

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from secrets import Config
from ..core import db
from .users import bp as users_blueprint
from .matches import bp as matches_blueprint

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    app.register_blueprint(users_blueprint, url_prefix='/users')
    app.register_blueprint(matches_blueprint, url_prefix='/matches')
    db.init_app(app)
    return app
