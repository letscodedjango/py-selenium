import pytest


# DRY - Do not repeat yourself

@pytest.fixture()
def setUp():
    print('Taking screenshot  before test')
    yield
    print('Taking screenshot after test')


def test_browser_launch(oneTimeSetUp, setUp):
    # print('Setting driver path')
    # print('launching browser')
    assert True
    # print('driver close')


def test_homepage_title(oneTimeSetUp, setUp):
    # print('Setting driver path')
    # print('launching browser')
    print('Getting homepage title')
    print('Comparing title')
    assert True
    # print('driver close')


def test_homepage_links(oneTimeSetUp, setUp):
    # print('Setting driver path')
    # print('launching browser')
    print('Getting all links')
    print('Validating links from homepage')
    assert False
    # print('driver close')
