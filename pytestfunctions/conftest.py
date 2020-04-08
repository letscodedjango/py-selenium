import pytest


#@pytest.fixture(scope='module')
from pytestfunctions.arithmetic_class import ArithmeticClass


@pytest.fixture(scope='class')
def oneTimeSetUp():
    print('Setting driver path')
    print('launching browser')
    yield
    print('drive close')
    print('driver quit')




# @pytest.fixture()
# def setUp(self):
#     self.ac = ArithmeticClass()
