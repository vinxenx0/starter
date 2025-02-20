from flask import session

def test_register(client):
    response = client.post("/register", data={"username": "testuser", "password": "testpass"}, follow_redirects=True)
    
    # Verificar que la página se cargó correctamente
    assert response.status_code == 200  
    assert "Usuario registrado con éxito" in response.data.decode("utf-8")


    # Extraer mensajes flash correctamente
    with client.session_transaction() as sess:
        flash_messages = sess.get("_flashes", [])  # Usar .get() para evitar KeyError
    
    assert any("Usuario registrado con éxito" in msg for _, msg in flash_messages)


def test_login(client):
    response = client.post("/login", data={"username": "testadmin", "password": "testadmin"}, follow_redirects=True)
    assert "Panel de Administración" in response.data.decode("utf-8")

def test_login_fail(client):
    response = client.post("/login", data={"username": "testadmin", "password": "wrongpass"}, follow_redirects=True)
    assert "Credenciales inválidas" in response.data.decode("utf-8")

def test_logout(client):
    client.post("/login", data={"username": "testadmin", "password": "testadmin"})
    response = client.get("/logout", follow_redirects=True)
    assert "Iniciar Sesión" in response.data.decode("utf-8")
