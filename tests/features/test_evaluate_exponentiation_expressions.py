from calculator import evaluate


def test_evaluating_a_simple_exponentiation_expression():
    expression = "3^4"

    assert evaluate(expression) == 81


def test_exponentiation_binds_more_strongly_than_times():
    expression = "3^4*5"

    assert evaluate(expression) == 405
