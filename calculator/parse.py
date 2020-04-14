from .expression import ConstExpr


def parse(string):
    return Parser(string).parse()


class Parser:
    def __init__(self, string):
        self.string = string

    def parse(self):
        return ConstExpr(value=int(self.string))
