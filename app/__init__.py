from flask_bootstrap import Bootstrap5
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from werkzeug.security import generate_password_hash

db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap5()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    bootstrap.init_app(app)

    with app.app_context():
        from app.views import auth, users
        app.register_blueprint(auth.bp)
        app.register_blueprint(users.bp)

        db.create_all()  # Crear tablas en la base de datos

        # Crear usuario admin por defecto si no existe
        from app.models.user import User
        if not User.query.filter_by(username="admin").first():
            admin_user = User(
                username="admin",
                password=generate_password_hash("admin123"),  # Contraseña segura
                role="admin"
            )
            db.session.add(admin_user)
            db.session.commit()
            print("✅ Usuario administrador creado: admin / admin123")

    return app
