from calculator.expression import ConstExpr, PlusExpr, TimesExpr, DivExpr, ExpExpr, SubExpr


def test_constant_expression_evaluates_to_itself():
    expr = ConstExpr(value=3)

    assert expr.evaluate() == 3


def test_plus_expression_evaluates_to_the_sum_of_operands():
    expr = PlusExpr(left=ConstExpr(value=3), right=ConstExpr(value=4))

    assert expr.evaluate() == 7


def test_subtract_expression_evaluates_to_the_difference_of_the_operands():
    expr = SubExpr(left=ConstExpr(value=3), right=ConstExpr(value=4))

    assert expr.evaluate() == -1


def test_times_expression_evaluates_to_the_product_of_operands():
    expr = TimesExpr(left=ConstExpr(value=3), right=ConstExpr(value=4))

    assert expr.evaluate() == 12


def test_divide_expression_evaluates_to_the_left_divided_by_the_right_operand():
    expr = DivExpr(left=ConstExpr(value=3), right=ConstExpr(value=4))

    assert expr.evaluate() == 0.75


def test_exponentiation_expression_evaluates_to_the_left_raised_to_the_right_operand():
    expr = ExpExpr(left=ConstExpr(value=3), right=ConstExpr(value=4))

    assert expr.evaluate() == 81
