from logging import debug
from flask import Flask
from flask_mail import Mail, Message

config ={
    "MAIL_SERVER" : "smtp.ethereal.email",
    "MAIL_PORT" : 587,
    "MAIL_TLS" : True,
    "MAIL_DEBUG" : True,
    "MAIL_USERNAME" : "dagmar.swift@ethereal.email",
    "MAIL_PASSWORD" : "WxbgxbGRmmHs12ejGZ",
    "MAIL_DEFAULT_SENDER" : "Teste <teste@teste.com.br>",
}

app = Flask(__name__)
mail = Mail(app)


@app.route("/sendmail")
def sendmail():
    msg = Message()
    return "Email enviado com sucesso!"

if __name__ == "__main__":
    app.run(debug=True)