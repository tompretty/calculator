class Expr:
    def evaluate(self):
        raise NotImplementedError()


class ConstExpr(Expr):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value


class BinaryExpr(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class PlusExpr(BinaryExpr):
    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()


class SubExpr(BinaryExpr):
    def evaluate(self):
        return self.left.evaluate() - self.right.evaluate()


class TimesExpr(BinaryExpr):
    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()


class DivExpr(BinaryExpr):
    def evaluate(self):
        return self.left.evaluate() / self.right.evaluate()


class ExpExpr(BinaryExpr):
    def evaluate(self):
        return self.left.evaluate() ** self.right.evaluate()
