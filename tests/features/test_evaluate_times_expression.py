from calculator import evaluate


def test_evaluating_a_simple_times_expression():
    source = "3*4"

    assert evaluate(source) == 12


def test_times_binds_more_strongly_than_plus():
    source = "3*4+5"

    assert evaluate(source) == 17
