def test_get_users_without_token(api_test_client):
    response = api_test_client.get("/api/users")
    assert response.status_code == 401

def test_get_users_with_valid_token(api_test_client):
    login_response = api_test_client.post("/api/login", data={"username": "testadmin", "password": "testadmin"})
    token = login_response.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}
    response = api_test_client.get("/api/users", headers=headers)

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_users_with_invalid_token(api_test_client):
    headers = {"Authorization": "Bearer invalidtoken"}
    response = api_test_client.get("/api/users", headers=headers)
    assert response.status_code == 401

def test_get_users_with_user_role(api_test_client):
    login_response = api_test_client.post("/api/login", data={"username": "testuser", "password": "testpass"})
    token = login_response.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}
    response = api_test_client.get("/api/users", headers=headers)

    assert response.status_code == 403
