from datetime import timedelta

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user, current_user

from wtforms.form import Form

from app import db
from app.models import User, Book
from app.forms import LoginForm, RegisterForm, BookForm, UserBookForm
from app.auth import auth as auth_blueprint
from app.book import book as book_blueprint


def init_app(app):
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(book_blueprint)
    
    @app.route("/")
    def index():
        users = User.query.all()# select * from users;
        return render_template("users.html", users=users)

    @app.route("/user/<int:id>")
    @login_required
    def unique(id):
        user = User.query.get(id)
        return render_template("user.html",user=user)

    @app.route("/user/delete/<int:id>")
    def delete(id):
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()

        return redirect("/")


    
    
