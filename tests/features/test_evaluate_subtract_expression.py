from calculator import evaluate


def test_evaluate_a_subtract_expression():
    expression = "3-4"

    assert evaluate(expression) == -1
