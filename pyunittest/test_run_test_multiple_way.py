# We can run test cases in mulyiple ways using Pytest

# to run whole module
# pytest module_path.py

# To run all the test cases within package
# pytest package_path

# To run single method from module
# pytest python_module.py::methods_name
import pytest


@pytest.fixture
def setUp():
    print('I m setup method')


def test_one(setUp):
    print('I am test one')


def test_two(setUp):
    print('I am test two')

# What if we have to execute setUp and teardown only once before and after all the test cases
