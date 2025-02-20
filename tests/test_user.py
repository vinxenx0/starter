def test_dashboard(client):
    client.post("/login", data={"username": "testadmin", "password": "testadmin"})
    response = client.get("/dashboard")
    assert "Panel de Administración" in response.data.decode("utf-8")

def test_add_user(client):
    client.post("/login", data={"username": "testadmin", "password": "testadmin"})
    response = client.post("/users/add", data={
        "username": "newuser",
        "password": "password123",
        "role": "user"
    }, follow_redirects=True)
    assert "Usuario creado con éxito" in response.data.decode("utf-8")

def test_edit_user(client):
    client.post("/login", data={"username": "testadmin", "password": "testadmin"})

    # Crear usuario de prueba
    response = client.post("/users/add", data={
        "username": "edituser",
        "password": "password123",
        "role": "user"
    }, follow_redirects=True)

    assert "Usuario creado con éxito"  in response.data.decode("utf-8")


    # Editar usuario
    response = client.post("/users/edit/2", data={
        "username": "editeduser",
        "password": "newpassword"
    }, follow_redirects=True)

    assert "Usuario actualizado con éxito" in response.data.decode("utf-8")

def test_delete_user(client):
    client.post("/login", data={"username": "testadmin", "password": "testadmin"})
    
    # Crear usuario para eliminarlo
    client.post("/users/add", data={
        "username": "deleteuser",
        "password": "password123",
        "role": "user"
    })

    response = client.get("/users/delete/2", follow_redirects=True)
    assert "Usuario eliminado con éxito" in response.data.decode("utf-8")
