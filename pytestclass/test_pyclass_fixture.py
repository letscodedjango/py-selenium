from pytestclass.class_to_test import ClassToTest
import pytest


class TestClassLevelFixture:
    def test_add(self):
        ct = ClassToTest(70, 35)
        result = ct.add()
        assert 105, result
        print('Testing the add functionality')

    def test_mod(self):
        ct = ClassToTest(70, 35)
        result = ct.mod()
        assert 105, result
        print('Testing the mod functionality')


# To access setUp and OneTimeSetUp


class TestClassLevelFixtureTwo:
    def test_add(self, setUp, oneTimeSetUp):
        ct = ClassToTest(70, 35)
        result = ct.add()
        assert 105, result
        print('Testing the add functionality')

    def test_mod(self, setUp, oneTimeSetUp):
        ct = ClassToTest(70, 35)
        result = ct.mod()
        assert 105, result
        print('Testing the mod functionality')


# So in teh above case, we have accessed setUp and oneTimeSetup but thing is -
# if there are 20 test cases then its not efficient way to place setUp and oneTimeSetUp in each & every
# test case

@pytest.mark.usefixtures('setUp', 'oneTimeSetUp')
class TestClassLevelFixtureThree:

    def test_add(self):
        ct = ClassToTest(70, 35)
        result = ct.add()
        assert 105, result
        print('Testing the add functionality')

    def test_mod(self):
        ct = ClassToTest(70, 35)
        result = ct.mod()
        assert 105, result
        print('Testing the mod functionality')


# What if we have to setup specific to class and should be excuted at the class level before all tests

@pytest.mark.usefixtures('setUp', 'oneTimeSetUp')
class TestClassLevelFixtureFour:

    @pytest.fixture()  # This decorator is mandatory
    def classSetUp(self):
        self.ct = ClassToTest(70, 35)

    def test_add(self, classSetUp):
        # ct = ClassToTest(70, 35) # this is repetitive code so move it to classSetUp
        result = self.ct.add()
        assert result == 105
        print('Testing the add functionality')

    def test_mod(self, classSetUp):
        # ct = ClassToTest(70, 35) # this is repetitive code so move it to classSetUp
        result = self.ct.mod()
        assert result == 0
        print('Testing the mod functionality')


# Again, here we have the same issue -what if we have multiple test cases and we have to apply the
# class level setup to all and to do so -- use 'autouse'

@pytest.mark.usefixtures('setUp', 'oneTimeSetUp')
class TestClassLevelFixtureFive:

    @pytest.fixture(autouse=True)  # This decorator is mandatory
    def classSetUp(self):
        self.ct = ClassToTest(70, 35)

    def test_add(self):
        # ct = ClassToTest(70, 35) # this is repetitive code so move it to classSetUp
        result = self.ct.add()
        assert result == 105
        print('Testing the add functionality')

    def test_mod(self):
        # ct = ClassToTest(70, 35) # this is repetitive code so move it to classSetUp
        result = self.ct.mod()
        assert result == 1  # This will fail since 70 will be completely divisible by 35
        print('Testing the mod functionality')
