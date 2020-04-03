import pytest


@pytest.mark.usefixtures(scope='module')
def oneTimeSetUp():
    print('Setting driver path')
    print('launching browser')
