from .expression import ConstExpr, PlusExpr, TimesExpr
from .utils import Stack


def parse(string):
    return Parser(string).parse()


class Parser:
    def __init__(self, string):
        self.string = string
        self.output_stack = Stack()
        self.operator_stack = Stack()

    def parse(self):
        for c in self.string:
            if self._is_digit(c):
                self._push_constant_to_output_stack(c)
            elif self._is_plus(c):
                self._push_plus_to_operator_stack()
            elif self._is_times(c):
                self._push_times_to_operator_stack()
            else:
                pass

        while self.operator_stack:
            op = self.operator_stack.pop()
            if self._is_plus(op):
                self._push_plus_to_output_stack()
            elif self._is_times(op):
                self._push_times_to_output_stack()

        return self.output_stack.pop()

    def _push_constant_to_output_stack(self, c):
        self.output_stack.push(ConstExpr(value=int(c)))

    def _push_plus_to_operator_stack(self):
        self.operator_stack.push("+")

    def _push_times_to_operator_stack(self):
        self.operator_stack.push("*")

    def _push_plus_to_output_stack(self):
        right = self.output_stack.pop()
        left = self.output_stack.pop()

        self.output_stack.push(PlusExpr(left=left, right=right))

    def _push_times_to_output_stack(self):
        right = self.output_stack.pop()
        left = self.output_stack.pop()

        self.output_stack.push(TimesExpr(left=left, right=right))

    def _is_digit(self, c):
        return c.isdigit()

    def _is_plus(self, c):
        return c == "+"

    def _is_times(self, c):
        return c == "*"
