from flask import Blueprint, render_template, request
from flask_login import login_required
from app.controllers.auth import AuthController

bp = Blueprint("auth", __name__)

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return AuthController.login()
    return render_template("login.html")

@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return AuthController.register()
    return render_template("register.html")

@bp.route("/logout")
@login_required
def logout():
    return AuthController.logout()
