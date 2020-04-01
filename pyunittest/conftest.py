import pytest


@pytest.fixture()
def setUp():
    print('I will execute before each and every test case')
    yield
    print('I will execute after each & every test case')


# @pytest.fixture(scope="module") # for module functions
@pytest.fixture(scope="class")
def oneTimeSetUp(browser, osType):
    if browser == 'chrome':
        print('Run test in chrome')
        print('I will execute only once before all test cases')
    elif browser == 'firefox':
        print('Run test case in firefox')
        print('I will execute only once before all test cases')
    yield
    if osType.upper() == 'MAC':
        print('Running test on mac os')
    elif osType.lower() == 'WINDOWS':
        print('Running test on Windows')
    else:
        print('Runnning test on linux')
    print('I will execute only once after all test cases')


# What if we have to setup browser and other details as command line argument we need to use addition functions


def pytest_addoption(parser):  # name of function is very very important-
    # it must be pytest_addoption not addoptions
    parser.addoption('--browser')
    parser.addoption('--osType', help='You need to enter operating system')
    print('I am adding brower')


@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')


@pytest.fixture(scope='session')
def osType(request):
    return request.config.getoption('--osType')

# Now lets make our one time setup smart to act according to the browser and ostype
