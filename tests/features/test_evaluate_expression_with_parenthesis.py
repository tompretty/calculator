from calculator import evaluate


def test_parenthesis_bind_most_strongly():
    source = "(3+4)*5"

    assert evaluate(source) == 35
