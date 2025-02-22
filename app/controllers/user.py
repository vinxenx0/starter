from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from werkzeug.security import generate_password_hash
from app import db
from app.models.user import User
from app.forms import UserForm

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

        form = UserForm()
        if form.validate_on_submit():
            if User.query.filter_by(username=form.username.data).first():
                flash("El usuario ya existe.", "warning")
                return redirect(url_for("users.add_user"))

            hashed_password = generate_password_hash(form.password.data)
            new_user = User(username=form.username.data, password=hashed_password, role=form.role.data)
            db.session.add(new_user)
            db.session.commit()

            flash("Usuario creado con éxito.", "success")
            return redirect(url_for("users.dashboard"))

        return render_template("add_user.html", form=form)

    @staticmethod
    @login_required
    def edit_user(user_id):
        user = User.query.get(user_id)
        if not user:
            flash("Usuario no encontrado.", "danger")
            return redirect(url_for("users.dashboard"))

        if not current_user.is_admin() and current_user.id != user.id:
            flash("No tienes permiso para editar este perfil.", "danger")
            return redirect(url_for("users.dashboard"))

        form = UserForm(user_id=user.id, obj=user)  # ✅ PASAMOS EL user_id

        if form.validate_on_submit():
            if form.username.data != user.username and User.query.filter_by(username=form.username.data).first():
                flash("El nombre de usuario ya está en uso.", "warning")
                return redirect(url_for("users.edit_user", user_id=user.id))

            user.username = form.username.data
            if form.password.data:
                user.password = generate_password_hash(form.password.data)
            if current_user.is_admin():
                user.role = form.role.data

            db.session.commit()
            flash("Usuario actualizado con éxito.", "success")
            return redirect(url_for("users.dashboard") if current_user.is_admin() else url_for("users.dashboard"))

        return render_template("edit_user.html", form=form, user=user)

    @staticmethod
    @login_required
    def delete_user(user_id):
        if not current_user.is_admin():
            flash("🚨 Acceso denegado: No tienes permisos para eliminar usuarios.", "danger")
            return redirect(url_for("users.dashboard"))

        user = User.query.get(user_id)
        if not user:
            flash("⚠️ No se encontró el usuario especificado. Verifica la información e intenta de nuevo.", "danger")
            return redirect(url_for("users.dashboard"))

        if user.role == "admin":
            flash("⚠️ No puedes eliminar una cuenta de administrador por seguridad del sistema.", "warning")
            return redirect(url_for("users.dashboard"))

        db.session.delete(user)
        db.session.commit()
        flash(f"🗑️ Usuario '{user.username}' eliminado con éxito.", "success")

        return redirect(url_for("users.dashboard"))
