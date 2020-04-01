import pytest

@pytest.fixture()
def setUp():
    print('I am setup and will execute before ech test')

def test_first(setUp):
    print('I am test one')


def test_second(setUp):
    print('I am test two')


def test_three():
    print('I am test three')
