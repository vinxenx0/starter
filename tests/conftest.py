import pytest
from app import create_app, db
from app.api import app as api_app
from app.models.user import User
from werkzeug.security import generate_password_hash
from fastapi.testclient import TestClient

@pytest.fixture(scope="session")
def flask_app():
    """Crea y configura una instancia de la aplicación Flask para pruebas."""
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["WTF_CSRF_ENABLED"] = False  # Desactivar CSRF en pruebas
    return app

@pytest.fixture(scope="session")
def api_test_client():
    """Crea un cliente de pruebas para FastAPI."""
    return TestClient(api_app)

@pytest.fixture(scope="function")
def flask_client(flask_app):
    """Crea un cliente de pruebas para Flask y maneja la base de datos."""
    with flask_app.test_client() as client:
        with flask_app.app_context():
            db.create_all()
            create_test_users()
            yield client
            db.session.remove()
            db.drop_all()

def create_test_users():
    """Crea usuarios de prueba en la base de datos."""
    admin = User(username="testadmin", password=generate_password_hash("testadmin"), role="admin")
    user = User(username="testuser", password=generate_password_hash("testpass"), role="user")

    db.session.add_all([admin, user])
    db.session.commit()
