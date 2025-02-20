from flask import request, redirect, url_for, flash, render_template
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models.user import User
from app.forms import LoginForm, RegisterForm  
class AuthController:
    @staticmethod
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for("users.dashboard"))
            flash("Credenciales inválidas", "danger")
        return render_template("login.html", form=form)

    @staticmethod
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            print("✅ Formulario validado correctamente")  # Depuración
            
            hashed_password = generate_password_hash(form.password.data)
            new_user = User(username=form.username.data, password=hashed_password, role="user")
            db.session.add(new_user)
            db.session.commit()

            flash("Usuario registrado con éxito", "success")
            return redirect(url_for("auth.login"))

        flash("❌ Error en el registro. Verifica los datos.", "danger")
        return render_template("register.html", form=form)  # Asegurar que se pase el formulario correctamente


    @staticmethod
    def logout():
        logout_user()
        return redirect(url_for("auth.login"))
