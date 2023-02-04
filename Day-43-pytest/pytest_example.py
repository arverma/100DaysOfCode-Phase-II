__author__ = 'aman.rv'
import pytest


def calculator(expression):
    return eval(expression)


def test_calculator():
    actual = calculator("1+4*6/3")
    assert actual == 9


def test_calculator_zero_division_exception():
    with pytest.raises(ZeroDivisionError):
        calculator("1+4*6/0")


def test_calculator_syntax_error_exception():
    with pytest.raises(SyntaxError):
        calculator("1+4*6/")


if __name__ == '__main__':
    print(calculator("1+4*6/0"))


