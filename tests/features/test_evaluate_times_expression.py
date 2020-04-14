from calculator import evaluate


def test_evaluating_a_simple_times_expression():
    expression = "3*4"

    assert evaluate(expression) == 12


def test_times_binds_more_strongly_than_plus():
    expression = "3*4+5"

    assert evaluate(expression) == 17
