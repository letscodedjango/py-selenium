import pytest
from pytestfunctions.arithmetic_class import ArithmeticClass


class TestArithmeticModule:

    @pytest.fixture()
    def setUp(self):
        ac = ArithmeticClass()

    def test_add(self, setUp):
        # ac = ArithmeticClass()
        res = ac.add(10, 20)
        assert res == 30  # pass
        res = ac.add(20.30, 20.70)
        assert res == 40  # fail
        res = ac.add(20.30, '23')
        assert res == 43.30  # fail

    def test_mul(self, setUp):
        # ac = ArithmeticClass()
        res = ac.product(10, 20)
        assert res == 200

    def test_mod(self, setUp):
        # ac = ArithmeticClass()
        res = ac.mod(20, 10)
        assert res == 0
