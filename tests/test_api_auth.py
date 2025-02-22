def test_login_success(api_test_client):
    response = api_test_client.post("/api/login", data={"username": "testadmin", "password": "testadmin"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_fail(api_test_client):
    response = api_test_client.post("/api/login", data={"username": "testadmin", "password": "wrongpass"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Credenciales inválidas"

def test_api_health(api_test_client):
    response = api_test_client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
