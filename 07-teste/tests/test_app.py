from click.core import Context
import pytest
from werkzeug.wrappers import response
from app import create_app, db

@pytest.fixture
def cliente():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"
    app.config["WTF_CSRF_ENABLED"] = False

    context = app.app_context()
    context.push()

    db.create_all()
    yield app.test_client()

    db.session.remove()
    db.drop_all()

    context.pop()
    
    


def test_se_a_pagina_de_usuarios_retorna_status_code_200(cliente):
   response = cliente.get("/")
   assert response.status_code == 200

def test_se_o_link_de_registrar_existe(cliente):
    response = cliente.get("/")
    assert "Registrar" in response.get_data(as_text = True)

def test_se_o_link_de_login_existe(cliente):
    response = cliente.get("/")
    assert "Login" in response.get_data(as_text = True)

def test_registrando_usuario(cliente):
    data ={
        "name": "Amanda",
        "email": "amanda@teste.com.br",
        "password":"1234"

    }
    response = cliente.post("/register", data=data, follow_redirects = True)
    assert "Amanda" in response.get_data(as_text=True)

def test_logando_usuario(cliente):
    data ={
        "name": "Amanda",
        "email": "amanda@teste.com.br",
        "password":"1234"
    }
    response = cliente.post("/register", data=data, follow_redirects = True)
    
    response2 = cliente.post("/login", data=data, follow_redirects=True)
    assert "Sair" in response2.get_data(as_text=True)