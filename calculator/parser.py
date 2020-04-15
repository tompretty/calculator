from .expression import (
    ConstExpr,
    DivExpr,
    ExpExpr,
    MinusExpr,
    PlusExpr,
    TimesExpr,
    VarExpr,
)
from .scanner import TokenType


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        return self._expression()

    def _expression(self):
        return self._addition()

    def _addition(self):
        expr = self._multiplication()

        while self._match(TokenType.PLUS, TokenType.MINUS):
            op = self._previous()
            if op.type == TokenType.PLUS:
                expr = PlusExpr(expr, self._multiplication())
            else:
                expr = MinusExpr(expr, self._multiplication())

        return expr

    def _multiplication(self):
        expr = self._exponentiation()

        while self._match(TokenType.TIMES, TokenType.DIVIDE):
            op = self._previous()
            if op.type == TokenType.TIMES:
                expr = TimesExpr(expr, self._exponentiation())
            else:
                expr = DivExpr(expr, self._exponentiation())

        return expr

    def _exponentiation(self):
        expr = self._primary()

        while self._match(TokenType.EXP):
            expr = ExpExpr(expr, self._primary())

        return expr

    def _primary(self):
        if self._match(TokenType.NUMBER):
            return ConstExpr(value=self._previous().value)
        elif self._match(TokenType.VARIABLE):
            return VarExpr(value=self._previous().value)
        elif self._match(TokenType.LEFT_PAREN):
            expr = self._expression()
            self._consume(TokenType.RIGHT_PAREN)
            return expr

    def _match(self, *token_types):
        for token_type in token_types:
            if self._check(token_type):
                self._advance()
                return True

        return False

    def _consume(self, token_type):
        token = self._advance()
        assert token.type == token_type

    def _check(self, token_type):
        if self._is_at_end():
            return False
        return self._peek().type == token_type

    def _is_at_end(self):
        return self.current >= len(self.tokens)

    def _peek(self):
        return self.tokens[self.current]

    def _previous(self):
        return self.tokens[self.current - 1]

    def _advance(self):
        self.current += 1
        return self.tokens[self.current - 1]
