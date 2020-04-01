# here we will be focusing on how to test test cases from class
import pytest
from pytestclass import class_to_test


@pytest.mark.usefixtures('setUp', 'oneTimeSetUp')  # Make sure conftest.py file is in same package
class TestClassToTest:

    def test_add(self):
        print('Successfully added two numbers')

    def test_mod(self):
        print('Successfully mod two numbers')

# Now the question is how we can add some of the fixture at class level
