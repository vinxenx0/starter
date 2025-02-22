from fastapi import APIRouter, HTTPException
from datetime import timedelta, datetime
from jose import JWTError, jwt
from app.models.user import User
from app import db, create_app
from werkzeug.security import check_password_hash
import os

router = APIRouter()
app = create_app()  # Crear instancia de Flask para el contexto

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt_secret_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/login")
def login(username: str, password: str):
    with app.app_context():  # 👈 Ahora Flask tiene contexto para usar `db.session`
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            raise HTTPException(status_code=401, detail="Credenciales inválidas")
        
        token = create_access_token({"sub": user.username, "role": user.role})
        return {"access_token": token, "token_type": "bearer"}
