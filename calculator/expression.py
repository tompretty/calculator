
class ConstExpr():
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value


class PlusExpr():
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()
