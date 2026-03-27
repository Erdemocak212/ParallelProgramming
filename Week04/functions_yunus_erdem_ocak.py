import inspect

# 1. custom_power: A lambda function
# x is positional-only (/), e is positional-or-keyword
custom_power = lambda x=0, e=1, /: x**e 
# Note: Standard lambdas don't easily support the '/' syntax in all versions. 
# If your environment errors, use a regular function or:
custom_power = lambda x=0, /, e=1: x**e

# 2. custom_equation
def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Calculates (x^a + y^b) / c.

    :param x: Base for the first term (positional-only)
    :param y: Base for the second term (positional-only)
    :param a: Exponent for x
    :param b: Exponent for y
    :param c: Divisor (keyword-only)
    :return: The result of the equation as a float
    """
    return float((x**a + y**b) / c)

# 3. fn_w_counter
def fn_w_counter():
    # Initialize storage on the function object itself to persist state
    if not hasattr(fn_w_counter, "calls"):
        fn_w_counter.calls = 0
        fn_w_counter.callers = {}

    # Get the name of the caller using the inspect module
    caller_name = inspect.currentframe().f_back.f_globals.get('__name__', '__main__')
    
    fn_w_counter.calls += 1
    fn_w_counter.callers[caller_name] = fn_w_counter.callers.get(caller_name, 0) + 1
    
    return fn_w_counter.calls, fn_w_counter.callers
