from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Optional, ValidationError
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
    password = PasswordField("Nueva Contraseña", validators=[Optional(), Length(min=6)])
    role = SelectField("Rol", choices=[("user", "Usuario"), ("admin", "Administrador")])
    submit = SubmitField("Guardar")

    def __init__(self, user_id=None, *args, **kwargs):
        """ Se recibe `user_id` para validar duplicados en edición """
        super(UserForm, self).__init__(*args, **kwargs)
        self.user_id = user_id

    def validate_username(self, username):
        existing_user = User.query.filter_by(username=username.data).first()
        if existing_user and existing_user.id != self.user_id:
            raise ValidationError("Este usuario ya existe. Elige otro.")
