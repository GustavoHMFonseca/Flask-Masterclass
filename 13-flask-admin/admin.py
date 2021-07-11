from flask_admin.contrib.sqla import ModelView

from models import User
from app import db

class UserView(ModelView):
    pass

def init_app(admin):
    admin.add_view(UserView(User, db.session))