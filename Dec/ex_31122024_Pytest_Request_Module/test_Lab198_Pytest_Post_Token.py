import pytest
import allure
import requests

# create token - post
base_url = "https://restful-booker.herokuapp.com"
headers = {"Content-Type": "application/json"}

def test_create_token():
    base_path = "/auth"
    full_url = base_url+base_path
    payload = {
            "username": "admin",
            "password": "password123"
    }

    response_data = requests.post(url=full_url,headers=headers,json=payload)
    print(response_data)

    assert response_data.status_code == 200
    response_data_json = response_data.json()
    token = response_data_json["token"]
    print(token)

    assert type(token) == str
    assert len(token) > 0