from calculator.parse import parse
from calculator.expression import ConstExpr, PlusExpr


def test_parsing_a_constant_returns_a_constant_expression():
    string = "3"

    expression = parse(string)

    assert type(expression) == ConstExpr


def test_parsing_a_plus_returns_a_plus_expression():
    string = "3+4"

    expression = parse(string)

    assert type(expression) == PlusExpr
