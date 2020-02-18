from typing import Any, Callable
from time import perf_counter
from functools import wraps


def timer_decorator(fn: Callable[..., Any]):
    """
    timer_decorator calls fn and prints how long it took to execute.

    :param fn: The wrapped function.
    :return: The return value of the wrapped function.
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        retval = fn(*args, **kwargs)
        end = perf_counter()
        print(f'{fn.__module__}.{fn.__name__}:\t{"%.2f" %(end-start)} seconds')
        return retval

    return wrapper