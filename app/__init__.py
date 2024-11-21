from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    app.config['SECRET_KEY'] = "ExpertSKB_FLASK"
    migrate.init_app(app, db)
    

    from .views import home, view
    app.add_url_rule('/', 'home', home, methods=['GET', 'POST'])
    app.add_url_rule('/view/<fid>', 'view', view, methods=['GET'])

    return app
