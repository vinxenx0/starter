python3 -m venv .venv
source .venv/bin/activate

# SaaS base
pip install flask flask-login flask-sqlalchemy flask-wtf flask-bootstrap python-dotenv

# test unitarias
pip install pytest flask-testing httpx


# seguridad formularios
pip install flask-wtf wtforms email-validator

# api
pip install fastapi uvicorn flask-jwt-extended pydantic flask-logging python-jose[cryptography]
pip install python-multipart



cp .env.example .env