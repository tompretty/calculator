from calculator import evaluate


def test_evaluating_a_simple_exponentiation_expression():
    source = "3^4"

    assert evaluate(source) == 81


def test_exponentiation_binds_more_strongly_than_times():
    source = "3^4*5"

    assert evaluate(source) == 405
