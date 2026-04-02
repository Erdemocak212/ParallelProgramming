import time
import tracemalloc
import functools


def performance(func):
    """
    A decorator that measures and stores performance statistics of the wrapped function.

    Attributes on the wrapper:
        counter (int): Number of times the decorated function has been called.
        total_time (float): Cumulative execution time in seconds across all calls.
        total_mem (int): Cumulative memory consumed in bytes across all calls.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Measure time
        start_time = time.perf_counter()

        # Measure memory
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        end_time = time.perf_counter()

        wrapper.counter += 1
        wrapper.total_time += (end_time - start_time)
        wrapper.total_mem += peak  # peak memory usage in bytes

        return result

    wrapper.counter = 0
    wrapper.total_time = 0.0
    wrapper.total_mem = 0

    return wrapper
