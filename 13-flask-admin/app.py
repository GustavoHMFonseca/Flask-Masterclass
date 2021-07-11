

from flask import Flask
from flask_admin import Admin

from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)


   
    db.init_app(app)

    # register admin page
    import admin as adiministrator
    admin = Admin(app, name="SpaceDevs", template_mode="bootstrap3")
    adiministrator.init_app(admin)
    

    return app

