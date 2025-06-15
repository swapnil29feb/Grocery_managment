from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os


def create_app():
    load_dotenv()  # Load environment variables from .env file
    app = Flask(__name__)
    
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
    DATABASE_URL = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Bind db instance to app
    db.init_app(app)
    
    #  Import models to register with SQLAlchemy
    from Grocery import models
    
    # with app.app_context():
    #     db.create_all()  # Optional: creates tables on startup
    
    # Register Blueprints
    from Grocery.routes.auth_bp import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    
    return app
    
