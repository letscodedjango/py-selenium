import pytest
from pytestfunctions import conftest


# DRY - Do not repeat yourself

@pytest.fixture()
def setUp():
    print('Setting driver path')
    print('launching browser')
    yield
    print('driver close')


def test_browser_launch(oneTimeSetup):
    # print('Setting driver path')
    # print('launching browser')
    assert True
    # print('driver close')


def test_homepage_title(oneTimeSetup):
    # print('Setting driver path')
    # print('launching browser')
    print('Getting homepage title')
    print('Comparing title')
    assert True
    # print('driver close')


def test_homepage_links(oneTimeSetup):
    # print('Setting driver path')
    # print('launching browser')
    print('Getting all links')
    print('Validating links from homepage')
    assert False
    # print('driver close')
