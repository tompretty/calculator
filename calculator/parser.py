from .expression import ConstExpr, DivExpr, ExpExpr, MinusExpr, PlusExpr, TimesExpr
from .scanner import TokenType
from .utils import Stack


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.output_stack = Stack()
        self.operator_stack = Stack()

    def parse(self):
        for t in self.tokens:
            if t.type == TokenType.NUMBER:
                self._push_constant_to_output_stack(t)
            elif t.type == TokenType.PLUS:
                self._push_to_operator_stack(PlusOp())
            elif t.type == TokenType.MINUS:
                self._push_to_operator_stack(MinusOp())
            elif t.type == TokenType.TIMES:
                self._push_to_operator_stack(TimesOp())
            elif t.type == TokenType.DIVIDE:
                self._push_to_operator_stack(DivOp())
            elif t.type == TokenType.EXP:
                self._push_to_operator_stack(ExpOp())
            elif t.type == TokenType.LEFT_PAREN:
                self._push_left_paren_to_operator_stack()
            elif t.type == TokenType.RIGHT_PAREN:
                self._push_right_paren_to_operator_stack()

        self._push_all_operators_to_output_stack()

        return self.output_stack.pop()

    def _push_constant_to_output_stack(self, t):
        self.output_stack.push(ConstExpr(value=t.value))

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

    def _is_subtract(self, c):
        return c == "-"

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
        raise NotImplementedError()


class BinaryOp(Op):
    def push_to_stack(self, stack):
        right = stack.pop()
        left = stack.pop()

        stack.push(self.expr_cls(left, right))


class PlusOp(BinaryOp):
    precedence = 1
    expr_cls = PlusExpr


class MinusOp(BinaryOp):
    precedence = 1
    expr_cls = MinusExpr


class TimesOp(BinaryOp):
    precedence = 2
    expr_cls = TimesExpr


class DivOp(BinaryOp):
    precedence = 2
    expr_cls = DivExpr


class ExpOp(BinaryOp):
    precedence = 3
    expr_cls = ExpExpr


class LeftParenOp(Op):
    pass
