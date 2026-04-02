import inspect

# custom_power: lambda function with two parameters (x positional-only, e positional-or-keyword)
# x has default value 0, e has default value 1, returns x**e
custom_power = lambda x=0, e=1: x ** e

def custom_equation(x: float = 0, y: float = 0, /, a: float = 1, b: float = 1, *, c: float = 1) -> float:
    """
    Computes the custom equation (x**a + y**b) / c.

    :param x: positional-only with default value 0
    :type x: float
    :param y: positional-only with default value 0
    :type y: float
    :param a: positional-or-keyword with default value 1
    :type a: float
    :param b: positional-or-keyword with default value 1
    :type b: float
    :param c: keyword-only with default value 1
    :type c: float
    :return: (x**a + y**b) / c
    :rtype: float
    """
    return (x ** a + y ** b) / c


def fn_w_counter():
    """
    A function that counts how many times it has been called and by whom.

    :return: A tuple of (total_call_count, {caller_name: call_count})
    :rtype: tuple[int, dict[str, int]]
    """
    # Get the caller's name
    frame = inspect.stack()[1]
    caller = frame[0].f_globals.get('__name__', '<unknown>')

    fn_w_counter._total += 1
    fn_w_counter._callers[caller] = fn_w_counter._callers.get(caller, 0) + 1

    return (fn_w_counter._total, dict(fn_w_counter._callers))

fn_w_counter._total = 0
fn_w_counter._callers = {}
