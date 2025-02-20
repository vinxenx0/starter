python3 -m venv .venv
source .venv/bin/activate

pip install flask flask-login flask-sqlalchemy flask-wtf flask-bootstrap python-dotenv

cp .env.example .env