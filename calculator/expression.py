class Expr:
    def evaluate(self, context=None):
        raise NotImplementedError()


class ConstExpr(Expr):
    def __init__(self, value):
        self.value = value

    def evaluate(self, context=None):
        return self.value


class VarExpr(Expr):
    def __init__(self, value):
        self.value = value

    def evaluate(self, context):
        return context[self.value]


class BinaryExpr(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class PlusExpr(BinaryExpr):
    def evaluate(self, context=None):
        return self.left.evaluate(context) + self.right.evaluate(context)


class MinusExpr(BinaryExpr):
    def evaluate(self, context=None):
        return self.left.evaluate(context) - self.right.evaluate(context)


class TimesExpr(BinaryExpr):
    def evaluate(self, context=None):
        return self.left.evaluate(context) * self.right.evaluate(context)


class DivExpr(BinaryExpr):
    def evaluate(self, context=None):
        return self.left.evaluate(context) / self.right.evaluate(context)


class ExpExpr(BinaryExpr):
    def evaluate(self, context=None):
        return self.left.evaluate(context) ** self.right.evaluate(context)
