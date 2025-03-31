from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from src.routes.router import router

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    app.register_blueprint(router)
    return app