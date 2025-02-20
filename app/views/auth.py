from flask import Blueprint, render_template, request
from flask_login import login_required
from app.controllers.auth import AuthController
from app.forms import LoginForm, RegisterForm  # <-- Importamos los formularios

bp = Blueprint("auth", __name__)

@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()  # <-- Crear instancia del formulario
    if request.method == "POST":
        return AuthController.login()
    return render_template("login.html", form=form)  # <-- Pasar form a la plantilla

@bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()  # <-- Crear instancia del formulario
    if request.method == "POST":
        return AuthController.register()
    return render_template("register.html", form=form)  # <-- Pasar form a la plantilla

@bp.route("/logout")
@login_required
def logout():
    return AuthController.logout()
