from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import current_user, login_required
from app.controllers.user import UserController

bp = Blueprint("users", __name__)

@bp.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("users.dashboard"))
    return render_template("index.html")

@bp.route("/dashboard")
def dashboard():
    return UserController.dashboard()

@bp.route("/users/add", methods=["GET", "POST"])
def add_user():
    return UserController.add_user()

@bp.route("/users/edit/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    return UserController.edit_user(user_id)

@bp.route("/users/delete/<int:user_id>")
def delete_user(user_id):
    return UserController.delete_user(user_id)
