from calculator import evaluate


def test_evaluate_a_subtract_expression():
    source = "3-4"

    assert evaluate(source) == -1
