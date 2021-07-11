from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["FLASK_ADMIN_SWATCH"] = "cosmo" 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dev.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


admin = Admin(app, name="SpaceDevs", template_mode="bootstrap3")
db = SQLAlchemy(app)


from models import User

class UserView(ModelView):
    pass

admin.add_view(UserView(User, db.session))

app.run(debug=True)