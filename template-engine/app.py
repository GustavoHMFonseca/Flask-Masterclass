from logging import debug
from flask import Flask, render_template,flash

app = Flask(__name__,template_folder="tema")
app.config["SECRET_KEY"] = "secret"

@app.route("/templates")
def templates():
    users = {
        "name": "Lucas Silva",
        "idade": 99,
        "email": "lucas@teste.com.br"
    }

    flash("Usuário criado com sucesso!")
    flash("passei por aqui.")
    
    return render_template("index.html",users=users)

if __name__ == "__main__":
    app.run(debug=True)
