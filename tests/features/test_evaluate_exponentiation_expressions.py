from calculator import evaluate


def test_evaluating_a_simple_exponentiation_expression():
    expression = "3^4"

    assert evaluate(expression) == 81
