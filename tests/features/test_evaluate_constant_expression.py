from calculator import evaluate


def test_evaluating_a_constant_expression():
    source = "3"

    assert evaluate(source) == 3
