from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from werkzeug.security import generate_password_hash
from app import db
from app.models.user import User

class UserController:
    @staticmethod
    @login_required
    def dashboard():
        if current_user.is_admin():
            users = User.query.all()
            return render_template("dashboard.html", users=users)
        else:
            return render_template("profile.html", user=current_user)

    @staticmethod
    @login_required
    def add_user():
        if not current_user.is_admin():
            flash("Acceso denegado", "danger")
            return redirect(url_for("users.dashboard"))

        if request.method == "POST":
            username = request.form["username"]
            password = generate_password_hash(request.form["password"])
            role = request.form["role"]

            if User.query.filter_by(username=username).first():
                flash("El usuario ya existe", "warning")
                return redirect(url_for("users.add_user"))

            new_user = User(username=username, password=password, role=role)
            db.session.add(new_user)
            db.session.commit()

            flash("Usuario creado con éxito", "success")
            return redirect(url_for("users.dashboard"))

        return render_template("add_user.html")

    @staticmethod
    @login_required
    def edit_user(user_id):
        user = User.query.get(user_id)

        if not user:
            flash("Usuario no encontrado", "danger")
            return redirect(url_for("users.dashboard"))

        if not current_user.is_admin() and current_user.id != user.id:
            flash("Acceso denegado", "danger")
            return redirect(url_for("users.dashboard"))

        if request.method == "POST":
            user.username = request.form["username"]
            if request.form["password"]:
                user.password = generate_password_hash(request.form["password"])
            if current_user.is_admin():
                user.role = request.form["role"]

            db.session.commit()
            flash("Usuario actualizado con éxito", "success")
            return redirect(url_for("users.dashboard") if current_user.is_admin() else url_for("users.dashboard"))

        return render_template("edit_user.html", user=user)

    @staticmethod
    @login_required
    def delete_user(user_id):
        if not current_user.is_admin():
            flash("Acceso denegado", "danger")
            return redirect(url_for("users.dashboard"))

        user = User.query.get(user_id)
        if user and user.role != "admin":  # No permitir eliminar admins
            db.session.delete(user)
            db.session.commit()
            flash("Usuario eliminado con éxito", "success")
        else:
            flash("No puedes eliminar a este usuario", "danger")

        return redirect(url_for("users.dashboard"))
