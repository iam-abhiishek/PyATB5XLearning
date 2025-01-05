# 5. Invalid Creation - enter a wrong payload or Wrong JSON.
import requests


def test_create_booking_id():
    url = "https://restful-booker.herokuapp.com/booking"
    header = {"Content-Type": "application/json"}
    payload = {
        "firstname": null,
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    res = requests.post(url=url,headers=header,json=payload)