def test_dashboard(flask_client):
    flask_client.post("/login", data={"username": "testadmin", "password": "testadmin"})
    response = flask_client.get("/dashboard")
    assert "Panel de Administración" in response.data.decode("utf-8")

def test_add_user(flask_client):
    flask_client.post("/login", data={"username": "testadmin", "password": "testadmin"})
    response = flask_client.post("/users/add", data={
        "username": "newuser",
        "password": "password123",
        "role": "user"
    }, follow_redirects=True)
    assert "Usuario creado con éxito" in response.data.decode("utf-8")

def test_edit_user(flask_client):
    flask_client.post("/login", data={"username": "testadmin", "password": "testadmin"})

    flask_client.post("/users/add", data={
        "username": "edituser",
        "password": "password123",
        "role": "user"
    }, follow_redirects=True)

    response = flask_client.post("/users/edit/2", data={
        "username": "editeduser",
        "password": "newpassword"
    }, follow_redirects=True)

    assert "Usuario actualizado con éxito" in response.data.decode("utf-8")

def test_delete_user(flask_client):
    flask_client.post("/login", data={"username": "testadmin", "password": "testadmin"})
    
    flask_client.post("/users/add", data={
        "username": "deleteuser",
        "password": "password123",
        "role": "user"
    })

    response = flask_client.get("/users/delete/2", follow_redirects=True)
    assert "Usuario eliminado con éxito" in response.data.decode("utf-8")
