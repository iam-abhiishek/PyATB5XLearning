import pytest

@pytest.fixture()
def create_token():
    return "abc"

@pytest.fixture()
def create_booking():
    return 1

@pytest.fixture()
def read_excel_file():
    return "xyz"

def test_update_re1(create_token,create_booking):
    print(create_token)
    print(create_booking)

def test_put_2(create_token, create_booking, read_excel_file):
    print(create_token)
    print(create_booking)
    print(read_excel_file)
