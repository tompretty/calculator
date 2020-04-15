from calculator.expression import (
    ConstExpr,
    DivExpr,
    ExpExpr,
    MinusExpr,
    PlusExpr,
    TimesExpr,
    VarExpr,
)
from calculator.parser import Parser
from calculator.scanner import Token, TokenType


def test_parsing_a_constant_returns_a_constant_expression():
    tokens = [Token(TokenType.NUMBER, 3)]

    parser = Parser(tokens)
    expr = parser.parse()

    assert type(expr) == ConstExpr


def test_parsing_a_variable_returns_a_variable_expression():
    tokens = [Token(TokenType.VARIABLE, "x")]

    parser = Parser(tokens)
    expr = parser.parse()

    assert type(expr) == VarExpr


def test_parsing_a_plus_returns_a_plus_expression():
    tokens = [
        Token(TokenType.NUMBER, 3),
        Token(TokenType.PLUS),
        Token(TokenType.NUMBER, 4),
    ]

    parser = Parser(tokens)
    expr = parser.parse()

    assert type(expr) == PlusExpr


def test_parsing_a_minus_expression():
    tokens = [
        Token(TokenType.NUMBER, 3),
        Token(TokenType.MINUS),
        Token(TokenType.NUMBER, 4),
    ]

    parser = Parser(tokens)
    expr = parser.parse()

    assert type(expr) == MinusExpr


def test_parsing_a_times_returns_a_times_expression():
    tokens = [
        Token(TokenType.NUMBER, 3),
        Token(TokenType.TIMES),
        Token(TokenType.NUMBER, 4),
    ]

    parser = Parser(tokens)
    expr = parser.parse()

    assert type(expr) == TimesExpr


def test_parsing_a_divide_returns_a_divide_expression():
    tokens = [
        Token(TokenType.NUMBER, 3),
        Token(TokenType.DIVIDE),
        Token(TokenType.NUMBER, 4),
    ]

    parser = Parser(tokens)
    expr = parser.parse()

    assert type(expr) == DivExpr


def test_parsing_an_exponentiation_return_an_exponentiation_expression():
    tokens = [
        Token(TokenType.NUMBER, 3),
        Token(TokenType.EXP),
        Token(TokenType.NUMBER, 4),
    ]

    parser = Parser(tokens)
    expr = parser.parse()

    assert type(expr) == ExpExpr


def test_parsing_parenthesis_changes_the_precedence():
    tokens = [
        Token(TokenType.LEFT_PAREN),
        Token(TokenType.NUMBER, 3),
        Token(TokenType.PLUS),
        Token(TokenType.NUMBER, 4),
        Token(TokenType.RIGHT_PAREN),
        Token(TokenType.TIMES),
        Token(TokenType.NUMBER, 5),
    ]

    parser = Parser(tokens)
    expr = parser.parse()

    assert type(expr) == TimesExpr
