from calculator import evaluate


def test_evaluating_a_simple_divide_expression():
    expression = "3/4"

    assert evaluate(expression) == 0.75


def test_divide_binds_more_strongly_than_plus():
    expression = "3/4+5"

    assert evaluate(expression) == 5.75
