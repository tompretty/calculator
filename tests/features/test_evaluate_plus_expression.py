from calculator import evaluate


def test_evaluating_a_plus_expression():
    source = "3+4"

    assert evaluate(source) == 7
