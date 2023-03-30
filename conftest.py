import pytest


@pytest.fixture(scope="function")
def url():
    return "https://hosting.timeweb.ru/login"


@pytest.fixture(scope="function")
def login():
    return "******"


@pytest.fixture(scope="function")
def password():
    return "******"
