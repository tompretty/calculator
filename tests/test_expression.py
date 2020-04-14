from calculator.expression import ConstExpr, PlusExpr, TimesExpr


def test_constant_expression_evaluates_to_itself():
    expr = ConstExpr(value=3)

    assert expr.evaluate() == 3


def test_plus_expression_evaluates_to_the_sum_of_operands():
    expr = PlusExpr(left=ConstExpr(value=3), right=ConstExpr(value=4))

    assert expr.evaluate() == 7


def test_times_expression_evaluates_to_the_product_of_operands():
    expr = TimesExpr(left=ConstExpr(value=3), right=ConstExpr(value=4))

    assert expr.evaluate() == 12
