from .parser import Parser
from .scanner import Scanner


def evaluate(source, context=None):
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()
    parser = Parser(tokens)
    expr = parser.parse()

    return expr.evaluate(context)
