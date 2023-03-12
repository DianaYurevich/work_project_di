import pytest

@pytest.fixture()
def set_up():
    print("START ALL TESTING PROGRAM")
    yield
    print("FINISH ALL TESTING PROGRAM")

@pytest.fixture(scope="module")
def set_group():
    print("ENTER TO SYSTEM SITE")
    yield
    print("EXIT TO SYSTEM SITE")