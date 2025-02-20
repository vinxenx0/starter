from flask_bootstrap import Bootstrap5
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap5()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    
    bootstrap = Bootstrap5(app)

    with app.app_context():
        from app.views import auth, users
        app.register_blueprint(auth.bp)
        app.register_blueprint(users.bp)

        db.create_all()

    return app
