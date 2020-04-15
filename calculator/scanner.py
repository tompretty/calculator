from enum import Enum


class TokenType(Enum):
    PLUS = 1
    MINUS = 2
    TIMES = 3
    DIVIDE = 4
    EXP = 5
    LEFT_PAREN = 6
    RIGHT_PAREN = 7
    NUMBER = 8
    VARIABLE = 9


class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value


class Scanner:
    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0

    def scan_tokens(self):
        while not self._is_at_end():
            self._scan_token()

        return self.tokens

    def _scan_token(self):
        self.start = self.current

        c = self._advance()
        if c == "+":
            self._add_token(TokenType.PLUS)
        elif c == "-":
            self._add_token(TokenType.MINUS)
        elif c == "*":
            self._add_token(TokenType.TIMES)
        elif c == "/":
            self._add_token(TokenType.DIVIDE)
        elif c == "^":
            self._add_token(TokenType.EXP)
        elif c == "(":
            self._add_token(TokenType.LEFT_PAREN)
        elif c == ")":
            self._add_token(TokenType.RIGHT_PAREN)
        elif c.isdigit():
            self._number()
        elif c.isalpha():
            self._variable()

    def _number(self):
        while self._peek().isdigit():
            self._advance()

        if self._peek() == "." and self._peek_next().isdigit():
            self._advance()

            while self._peek().isdigit():
                self._advance()

        self._add_token(TokenType.NUMBER, float(self.source[self.start:self.current]))

    def _variable(self):
        while self._peek().isalnum() or self._peek() == "_":
            self._advance()

        self._add_token(TokenType.VARIABLE, self.source[self.start:self.current])

    def _add_token(self, token_type, value=None):
        self.tokens.append(Token(token_type, value))

    def _peek(self):
        if self._is_at_end():
            return "\0"
        return self.source[self.current]

    def _peek_next(self):
        if self.current + 1 >= len(self.source):
            return "\0"
        return self.source[self.current + 1]

    def _advance(self):
        self.current += 1
        return self.source[self.current - 1]

    def _is_at_end(self):
        return self.current >= len(self.source)
