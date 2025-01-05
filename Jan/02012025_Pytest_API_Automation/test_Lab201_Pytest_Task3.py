import pytest
import requests

def getallbooking_id():
    url = "https://restful-booker.herokuapp.com/booking"

    response = requests.get(url=url)
    res_data_json = response.json()
    bookingid = res_data_json[0]["bookingid"]
    print("bookinid->",bookingid)
    return bookingid

base_url = "https://restful-booker.herokuapp.com"
headers = {
    "Content-Type": "application/json",
}
def get_token():
    base_path = "/auth"
    token_url = base_url + base_path
    token_payload = {
        "username": "admin",
        "password": "password123"
    }

    token_response = requests.post(url=token_url,headers=headers,json=token_payload)
    response_data_json = token_response.json()
    token = response_data_json["token"]
    print("token->",token)
    return token

def test_update_booking():
    token = get_token()
    bookinid = getallbooking_id()
    cookie = "token=" + token
    base_path = "/booking/" + str(bookinid)
    full_url = base_url + base_path
    headers = {
        "Cookie" : cookie
    }
    json_payload = {
        "firstname": "harry",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    update_res = requests.put(url=full_url,headers=headers,json=json_payload)
    res_data_json = update_res.json()


def test_getbooking_by_id():
    bookinid = getallbooking_id()
    base_path = "/booking/" + str(bookinid)
    full_url = base_url + base_path
    get_booking_by_id_res = requests.get(url=full_url)
    res_json = get_booking_by_id_res.json()
    first_nm = res_json["firstname"]
    print(first_nm)


