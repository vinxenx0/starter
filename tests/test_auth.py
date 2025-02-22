def test_register(flask_client):
    response = flask_client.post("/register", data={"username": "newuser", "password": "newpass"}, follow_redirects=True)
    assert response.status_code == 200
    assert "Usuario registrado con éxito" in response.data.decode("utf-8")

def test_login(flask_client):
    response = flask_client.post("/login", data={"username": "testadmin", "password": "testadmin"}, follow_redirects=True)
    assert "Panel de Administración" in response.data.decode("utf-8")

def test_login_fail(flask_client):
    response = flask_client.post("/login", data={"username": "testadmin", "password": "wrongpass"}, follow_redirects=True)
    assert "Credenciales inválidas" in response.data.decode("utf-8")

def test_logout(flask_client):
    flask_client.post("/login", data={"username": "testadmin", "password": "testadmin"})
    response = flask_client.get("/logout", follow_redirects=True)
    assert "Iniciar Sesión" in response.data.decode("utf-8")
