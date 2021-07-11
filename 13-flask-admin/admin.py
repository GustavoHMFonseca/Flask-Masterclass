from re import search
from flask_admin.contrib.sqla import ModelView
from wtforms.fields import PasswordField
from werkzeug.security import generate_password_hash

from models import User
from app import db

class UserView(ModelView):
    column_editable_list = ("name","email")
    form_edit_rules={"name","email"}
    column_searchable_list = ["email"]
    edit_modal=True

    form_extra_fields={
        "password": PasswordField("Password")
    }
    column_exclude_list = ["password"]

    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(form.password.data)
        return super().on_model_change(form, model, is_created)
    

def init_app(admin):
    admin.add_view(UserView(User, db.session))