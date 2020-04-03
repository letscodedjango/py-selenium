import pytest
from pytestfunctions import arithmetic_module

#pip install pytest-ordering

@pytest.mark.run(after='test_mul')
def test_add():
    res = arithmetic_module.add(10, 20)
    assert res == 30 # pass
    res = arithmetic_module.add(20.30, 20.70)
    assert res == 40  # fail
    res = arithmetic_module.add(20.30, '23')
    assert res == 43.30  # fail


@pytest.mark.run(order=3)
def test_mul():
    res = arithmetic_module.product(10, 20)
    assert res == 200


@pytest.mark.run(order=2)
def test_mod():
    res = arithmetic_module.mod(20, 10)
    assert res == 0
