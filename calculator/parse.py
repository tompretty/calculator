from .expression import ConstExpr, PlusExpr


def parse(string):
    return Parser(string).parse()


class Parser:
    def __init__(self, string):
        self.string = string
        self.output_stack = []
        self.operator_stack = []

    def parse(self):
        for c in self.string:
            if self._is_digit(c):
                self._push_constant_to_output_stack(c)
            elif self._is_plus(c):
                self._push_plus_to_operator_stack()
            else:
                pass

        while self.operator_stack:
            op = self.operator_stack.pop()
            if self._is_plus(op):
                self._push_plus_to_output_stack()

        return self.output_stack.pop()

    def _push_constant_to_output_stack(self, c):
        self.output_stack.append(ConstExpr(value=int(c)))

    def _push_plus_to_operator_stack(self):
        self.operator_stack.append("+")

    def _push_plus_to_output_stack(self):
        right = self.output_stack.pop()
        left = self.output_stack.pop()

        self.output_stack.append(PlusExpr(left=left, right=right))

    def _is_digit(self, c):
        return c.isdigit()

    def _is_plus(self, c):
        return c == "+"
