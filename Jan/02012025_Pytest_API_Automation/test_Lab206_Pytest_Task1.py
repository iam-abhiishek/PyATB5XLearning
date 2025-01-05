#1. Verify that Create Booking -> Patch Request - Verify that firstName is updated.

import pytest
import requests
import allure

def test_patch_request(create_token, create_booking):
    base_url = "https://restful-booker.herokuapp.com"
    # booking_value = create_booking()
    base_path = "/booking/" + create_booking
    full_url = base_url + base_path
    # token_value = create_token()
    cookie = "token=" + create_token
    headers = {
        "Content-Type": "application/json",
        "Cookie" : cookie
    }
    json_payload = {
        "firstname": "abhi",
        "lastname": "Brown"
    }

    response = requests.patch(url=full_url,headers=headers,json=json_payload)
    response_data_json = response.json()
    firstname = response_data_json["firstname"]
    print(firstname)
    assert firstname.text == "abhi"
