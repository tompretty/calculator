from calculator import evaluate


def test_parenthesis_bind_most_strongly():
    expression = "(3+4)*5"

    assert evaluate(expression) == 35
