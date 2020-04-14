from .parse import parse


def evaluate(string):
    return parse(string).evaluate()
