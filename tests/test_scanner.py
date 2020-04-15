from calculator.scanner import Scanner, TokenType


def test_scanner_can_tokenize_a_plus():
    source = "+"

    token = Scanner(source).scan_tokens()[0]

    assert token.type == TokenType.PLUS


def test_scanner_can_tokenize_a_minus():
    source = "-"

    token = Scanner(source).scan_tokens()[0]

    assert token.type == TokenType.MINUS


def test_scanner_can_tokenize_a_times():
    source = "*"

    token = Scanner(source).scan_tokens()[0]

    assert token.type == TokenType.TIMES


def test_scanner_can_tokenize_a_divide():
    source = "/"

    token = Scanner(source).scan_tokens()[0]

    assert token.type == TokenType.DIVIDE


def test_scanner_can_tokenize_an_exponentiation():
    source = "^"

    token = Scanner(source).scan_tokens()[0]

    assert token.type == TokenType.EXP


def test_scanner_can_tokenize_a_left_paren():
    source = "("

    token = Scanner(source).scan_tokens()[0]

    assert token.type == TokenType.LEFT_PAREN


def test_scanner_can_tokenize_a_right_paren():
    source = ")"

    token = Scanner(source).scan_tokens()[0]

    assert token.type == TokenType.RIGHT_PAREN


def test_scanner_can_tokenize_a_digit():
    source = "1"

    token = Scanner(source).scan_tokens()[0]

    assert token.type == TokenType.NUMBER
    assert token.value == 1


def test_scanner_can_tokenize_multiple_digits():
    source = "123"

    token = Scanner(source).scan_tokens()[0]

    assert token.type == TokenType.NUMBER
    assert token.value == 123


def test_scanner_can_tokenize_numbers_with_fractional_parts():
    source = "123.456"

    token = Scanner(source).scan_tokens()[0]

    assert token.type == TokenType.NUMBER
    assert token.value == 123.456


def test_scanner_can_tokenize_a_variable():
    source = "var_1"

    token = Scanner(source).scan_tokens()[0]

    assert token.type == TokenType.VARIABLE
    assert token.value == "var_1"
