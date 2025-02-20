import pytest
from app import create_app, db
from app.models.user import User
from werkzeug.security import generate_password_hash

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # Base de datos en memoria
    app.config["WTF_CSRF_ENABLED"] = False  # Desactivar CSRF para pruebas
    client = app.test_client()

    with app.app_context():
        db.create_all()  # Crear base de datos antes de cada test
        create_test_users()  # Crear usuarios de prueba

    yield client

    with app.app_context():
        db.session.remove()  # Cerrar la sesión de SQLAlchemy
        db.drop_all()  # Eliminar la base de datos después de cada test

def create_test_users():
    """Función para crear usuarios de prueba en cada test."""
    admin = User(username="testadmin", password=generate_password_hash("testadmin"), role="admin")
    user = User(username="testuser", password=generate_password_hash("testpass"), role="user")

    db.session.add(admin)
    db.session.add(user)
    db.session.commit()
