import pytest

@pytest.fixture
def cliente():
    return "ACESSANDO A PÁGINA INDEX.HTML"


def test_client(cliente):
    assert cliente == "ACESSANDO A PÁGINA INDEX.HTMLS"