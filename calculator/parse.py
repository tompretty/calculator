from .expression import ConstExpr, DivExpr, ExpExpr, PlusExpr, TimesExpr
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
                self._push_to_operator_stack(PlusOp())
            elif self._is_times(c):
                self._push_to_operator_stack(TimesOp())
            elif self._is_divide(c):
                self._push_to_operator_stack(DivOp())
            elif self._is_exponentiation(c):
                self._push_to_operator_stack(ExpOp())
            elif self._is_left_paren(c):
                self._push_left_paren_to_operator_stack()
            elif self._is_right_paren(c):
                self._push_right_paren_to_operator_stack()
            else:
                pass

        self._push_all_operators_to_output_stack()

        return self.output_stack.pop()

    def _push_constant_to_output_stack(self, c):
        self.output_stack.push(ConstExpr(value=int(c)))

    def _push_to_operator_stack(self, op):
        while self.operator_stack:
            top = self.operator_stack.peak()
            if op.precedence >= top.precedence:
                break
            self._push_top_operator_to_output_stack()

        self.operator_stack.push(op)

    def _push_left_paren_to_operator_stack(self):
        self.operator_stack.push(LeftParenOp())

    def _push_right_paren_to_operator_stack(self):
        while self.operator_stack:
            top = self.operator_stack.peak()
            if type(top) == LeftParenOp:
                self.operator_stack.pop()
                break
            self._push_top_operator_to_output_stack()

    def _push_top_operator_to_output_stack(self):
        top = self.operator_stack.pop()
        top.push_to_stack(self.output_stack)

    def _push_all_operators_to_output_stack(self):
        while self.operator_stack:
            self._push_top_operator_to_output_stack()

    def _is_digit(self, c):
        return c.isdigit()

    def _is_plus(self, c):
        return c == "+"

    def _is_times(self, c):
        return c == "*"

    def _is_divide(self, c):
        return c == "/"

    def _is_exponentiation(self, c):
        return c == "^"

    def _is_left_paren(self, c):
        return c == "("

    def _is_right_paren(self, c):
        return c == ")"


class Op:
    precedence = 0

    def push_to_stack(self, stack):
        pass


class PlusOp(Op):
    precedence = 1

    def push_to_stack(self, stack):
        right = stack.pop()
        left = stack.pop()

        stack.push(PlusExpr(left, right))


class TimesOp(Op):
    precedence = 2

    def push_to_stack(self, stack):
        right = stack.pop()
        left = stack.pop()

        stack.push(TimesExpr(left, right))


class DivOp(Op):
    precedence = 2

    def push_to_stack(self, stack):
        right = stack.pop()
        left = stack.pop()

        stack.push(DivExpr(left, right))


class ExpOp(Op):
    precedence = 3

    def push_to_stack(self, stack):
        right = stack.pop()
        left = stack.pop()

        stack.push(ExpExpr(left, right))


class LeftParenOp(Op):
    pass
