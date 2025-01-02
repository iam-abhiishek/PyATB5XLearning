import pytest
import allure
import requests

# create token - post
base_url = "https://restful-booker.herokuapp.com"
headers = {"Content-Type": "application/json"}

def get_token():
    base_path = "/auth"
    full_url = base_url + base_path
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=full_url,headers=headers,json=json_payload)
    response_data_json = response.json()
    token = response_data_json["token"]
    return token

def get_booking_id():
    base_path = "/booking"
    full_url = base_url+base_path
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response_data = requests.post(url=full_url,headers=headers,json=payload)
    response_data_json = response_data.json()
    bookingid = response_data_json["bookingid"]
    return bookingid

def test_put_request():
    token = get_token()
    bookingid = get_booking_id()
    print(token)
    print(bookingid)
    base_path = "/booking/" + str(bookingid)
    full_url = base_url + base_path
    cookie = "token=" + token

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    json_payload = {
        "firstname": "abhishek",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response_put = requests.put(url=full_url,headers=headers,json=json_payload)
    response_data_json = response_put.json()
    assert response_put.status_code == 200
    assert response_data_json["firstname"] == "abhishek"

def test_delete_request():
    token = get_token()
    bookingid = get_booking_id()
    base_path = "/booking/" + str(bookingid)
    cookie = "token=" + token
    delete_url = base_url + base_path
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    response = requests.delete(url=delete_url,headers=headers)
    assert response.status_code == 201

