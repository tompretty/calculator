from calculator import evaluate


def test_evaluating_a_constant_expression():
    expression = "3"

    assert evaluate(expression) == 3
