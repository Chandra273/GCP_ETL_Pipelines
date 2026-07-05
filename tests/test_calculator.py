import pytest

from src.calculator import add, divide, evaluate, multiply, power, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 2) == 3


def test_multiply():
    assert multiply(4, 2.5) == 10.0


def test_divide():
    assert divide(9, 3) == 3.0


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)


def test_power():
    assert power(2, 3) == 8


def test_evaluate_simple_expression():
    assert evaluate("2 + 3 * 4") == 14.0


def test_evaluate_unary_expression():
    assert evaluate("-5 + 3") == -2.0


def test_evaluate_invalid_expression():
    with pytest.raises(ValueError):
        evaluate("2 + foo")
