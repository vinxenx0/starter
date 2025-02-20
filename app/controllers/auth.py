from flask import request, redirect, url_for, flash
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models.user import User

class AuthController:
    @staticmethod
    def login():
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("users.dashboard"))
        
        flash("Credenciales inválidas", "danger")
        return redirect(url_for("auth.login"))

    @staticmethod
    def register():
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])

        if User.query.filter_by(username=username).first():
            flash("El usuario ya existe", "warning")
            return redirect(url_for("auth.register"))

        new_user = User(username=username, password=password, role="admin")
        db.session.add(new_user)
        db.session.commit()
        
        flash("Usuario registrado con éxito", "success")
        return redirect(url_for("auth.login"))

    @staticmethod
    def logout():
        logout_user()
        return redirect(url_for("auth.login"))
