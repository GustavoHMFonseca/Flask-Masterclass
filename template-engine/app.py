from logging import debug
from flask import Flask, render_template,flash
from datetime import datetime
from filtros import format_date

app = Flask(__name__,template_folder="tema",static_folder="public")
app.config["SECRET_KEY"] = "secret"
app.jinja_env.filters["formatdate"] = format_date

@app.route("/templates")
def templates():

    user_page = True     

    return render_template("index.html",user_page=user_page)

@app.route("/usuarios")
def users():
    flash("Users routes")
    users = [{
        "name": "Lucas Silva",
        "idade": 99,
        "email": "lucas@teste.com.br",
        "active": True,
        "since" : datetime.utcnow()
    },
    {
        "name": "Amanda Gomes",
        "idade": 17,
        "email": "manda@teste.com.br",
        "active": False,
        "since" : datetime.utcnow()
    },
    
    ]
    return render_template("users.html",users=users)

if __name__ == "__main__":
    app.run(debug=True)
