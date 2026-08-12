# modules/differentiation/rules.py

def identify_rule(expr):
    """
    Identifies which derivative rule is being applied.
    """

    if expr.is_Pow:
        return "Power Rule"

    if expr.is_Mul:
        return "Product Rule"

    if expr.is_Function:
        return f"Chain Rule ({expr.func.__name__})"

    if expr.is_Add:
        return "Sum Rule"

    return "Basic Rule"
