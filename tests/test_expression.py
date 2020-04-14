from calculator.expression import ConstExpr


def test_constant_expression_evaluates_to_itself():
    expr = ConstExpr(value=3)

    assert expr.evaluate() == 3
