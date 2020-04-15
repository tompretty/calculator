from calculator import evaluate


def test_evaluating_a_simple_divide_expression():
    source = "3/4"

    assert evaluate(source) == 0.75


def test_divide_binds_more_strongly_than_plus():
    source = "3/4+5"

    assert evaluate(source) == 5.75
