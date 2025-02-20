from flask import Blueprint, request
from app.controllers.user import UserController

bp = Blueprint("users", __name__)

@bp.route("/")
def index():
    return UserController.dashboard()

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
