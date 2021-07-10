from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms.fields.html5 import EmailField
from wtforms.fields import PasswordField, BooleanField, SubmitField
from wtforms.validators import Length, Email


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[Email()])
    password = PasswordField("senha", validators=[Length(3,6,"Sua senha deve conter de 3 a 6 cxaracteres.")])
    remember = BooleanField("Permanecer Conectado")
    submit = SubmitField("Logar")
