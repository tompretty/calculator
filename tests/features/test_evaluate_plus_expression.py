from calculator import evaluate


def test_evaluating_a_plus_expression():
    expression = "3+4"

    assert evaluate(expression) == 7
