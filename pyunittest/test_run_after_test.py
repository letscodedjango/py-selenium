import pytest


# if we have to run specific test after every test case we have to use yield
@pytest.fixture()  # we can also @pytest.yield_fixture but it has been deprecated after pytest 2.10 version
def setUp():
    print('I am setup and will execute before each test')
    yield
    print('I am teardown and will execute after each test')


def test_first(setUp):
    print('I am test one')


def test_second(setUp):
    print('I am test two')


def test_three():
    print('I am test three')
