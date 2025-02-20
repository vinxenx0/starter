from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from app.models.user import User

class LoginForm(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    submit = SubmitField("Ingresar")

class RegisterForm(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField("Contraseña", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirmar Contraseña", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Registrarse")

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError("Este usuario ya existe. Elige otro.")

class UserForm(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField("Nueva Contraseña")
    role = SelectField("Rol", choices=[("user", "Usuario"), ("admin", "Administrador")])
    submit = SubmitField("Guardar")
