import pytest
import requests    

#------------------------------------------------------------------------------------------------------------------------------------
# [post]/auth/login

@pytest.fixture()
def f_test_auth():
    credentials = {
        "username": "bloom",
        "password": "fire-fairy"
        }
        
    response = requests.post("https://x-clients-be.onrender.com/auth/login", json=credentials)
    assert response.status_code == 201
    print("Токен получен: " + response.json()["userToken"])
    return response.json()["userToken"]

    
