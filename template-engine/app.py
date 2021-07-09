from logging import debug
from flask import Flask, render_template

app = Flask(__name__,template_folder="tema")

@app.route("/templates")
def templates():
    user = {
        "name": "Lucas Silva",
        "idade": 99,
        "email": "lucas@teste.com.br"
    }
    return render_template("index.html",user=user)

if __name__ == "__main__":
    app.run(debug=True)
