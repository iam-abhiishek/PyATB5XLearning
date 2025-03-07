import pytest
import allure
import requests

base_url = "https://restful-booker.herokuapp.com"
headers = {
    "Content-Type": "application/json",
}
def create_token():
    base_path = "/auth"
    token_url = base_url + base_path
    token_payload = {
        "username": "admin",
        "password": "password123"
    }

    token_response = requests.post(url=token_url,headers=headers,json=token_payload)
    response_data_json = token_response.json()
    token = response_data_json["token"]
    print(token)
    return token

def create_booking_id():
    base_path = "/booking"
    create_booking_url = base_url + base_path
    create_booking_payload = {
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

    booking_response = requests.post(url=create_booking_url,headers=headers,json=create_booking_payload)
    response_data_json = booking_response.json()
    bookingid = response_data_json["bookingid"]
    print(bookingid)
    return bookingid

def test_delete_request():
    global bookingid
    token = create_token()
    bookingid = create_booking_id()
    base_path = "/booking/" + str(bookingid)
    cookie = "token=" + token
    delete_url = base_url + base_path
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    response = requests.delete(url=delete_url, headers=headers)
    assert response.status_code == 201