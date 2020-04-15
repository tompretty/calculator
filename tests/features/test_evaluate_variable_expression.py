from calculator import evaluate


def test_evaluating_a_variable_expression():
    source = "x + y"
    context = {"x": 3, "y": 4}

    assert evaluate(source, context) == 7
