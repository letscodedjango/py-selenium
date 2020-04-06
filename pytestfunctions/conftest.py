import pytest


@pytest.fixture(scope='module')
def oneTimeSetUp():
    print('Setting driver path')
    print('launching browser')
    yield
    print('drive close')
    print('driver quit')
