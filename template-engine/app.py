from logging import debug
from flask import Flask, render_template,flash

app = Flask(__name__,template_folder="tema",static_folder="public")
app.config["SECRET_KEY"] = "secret"

@app.route("/templates")
def templates():
    

    flash("Usuário criado com sucesso!")
    flash("passei por aqui.")

    return render_template("index.html")

@app.route("/usuarios")
def users():
    flash("Users routes")
    users = [{
        "name": "Lucas Silva",
        "idade": 99,
        "email": "lucas@teste.com.br",
        "active": True
    },
    {
        "name": "Amanda Gomes",
        "idade": 17,
        "email": "manda@teste.com.br",
        "active": False
    },
    
    ]
    return render_template("users.html",users=users)

if __name__ == "__main__":
    app.run(debug=True)
