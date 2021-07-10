from click.core import Context
import pytest
from app import create_app

@pytest.fixture
def cliente():
    app = create_app()
    app.config["TESTING"] = True

    context = app.app_context()
    context.push()

    yield app.test_client()

    context.pop()
    


def test_se_a_pagina_de_usuarios_retorna_status_code_200(cliente):
   response = cliente.get("/")
   assert response.status_code == 200