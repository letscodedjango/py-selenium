import pytest

#https://pytest-ordering.readthedocs.io/en/develop/
# by default test cases run in the same order it is placed in the file


@pytest.mark.run(after='test_case_run_order_two')
def test_case_run_order_one(oneTimeSetUp, setUp):
    print('I am test one')


@pytest.mark.run(before='test_case_run_order_three')
def test_case_run_order_two(oneTimeSetUp, setUp):
    print('I am test two')


@pytest.mark.run(order=1)
def test_case_run_order_five(oneTimeSetUp, setUp):
    print('I am test five')


@pytest.mark.run(order=7)
def test_case_run_order_three(oneTimeSetUp, setUp):
    print('I am test three')


# since we haven't apply any order will run at the last
def test_case_run_order_four(oneTimeSetUp, setUp):
    print('I am test four')

# pyunittest/test_case_run_order.py:6
#   /Users/gaurnitai/Desktop/PySelenium/pyunittest/test_case_run_order.py:6: PytestUnknownMarkWarning: Unknown pytest.mark.run - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
#     @pytest.mark.run(order=3)

# We will get this warning since we are trying to order without installing package pytest-ordering
