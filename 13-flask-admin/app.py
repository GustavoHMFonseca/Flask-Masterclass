from flask import Flask
from flask_admin import Admin

app = Flask(__name__)
app.config["FLASK_ADMIN_SWATCH"] = "cosmo"
Admin(app, name="SpaceDevs", template_mode="bootstrap3")

app.run(debug=True)