from calculator.parse import parse
from calculator.expression import ConstExpr, PlusExpr, TimesExpr, DivExpr, ExpExpr


def test_parsing_a_constant_returns_a_constant_expression():
    string = "3"

    expression = parse(string)

    assert type(expression) == ConstExpr


def test_parsing_a_plus_returns_a_plus_expression():
    string = "3+4"

    expression = parse(string)

    assert type(expression) == PlusExpr


def test_parsing_a_times_returns_a_times_expression():
    string = "3*4"

    expression = parse(string)

    assert type(expression) == TimesExpr


def test_parsing_a_divide_returns_a_divide_expression():
    string = "3/4"

    expression = parse(string)

    assert type(expression) == DivExpr


def test_parsing_an_exponentiation_return_an_exponentiation_expression():
    string = "3^4"

    expression = parse(string)

    assert type(expression) == ExpExpr


def test_parsing_parenthesis_changes_the_precedence():
    string = "(3+4)*5"

    expression = parse(string)

    assert type(expression) == TimesExpr
