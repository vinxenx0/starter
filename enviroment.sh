python3 -m venv .venv
source .venv/bin/activate

pip install flask flask-login flask-sqlalchemy flask-wtf flask-bootstrap python-dotenv
pip install pytest flask-testing
pip install flask-wtf wtforms email-validator


cp .env.example .env