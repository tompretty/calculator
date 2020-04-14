from .expression import ConstExpr


def parse(string):
    return ConstExpr(value=int(string))
