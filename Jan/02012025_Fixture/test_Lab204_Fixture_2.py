import pytest

@pytest.fixture()
def before_run():
    return True

@pytest.fixture()
def test_update(before_run):
    assert before_run == True