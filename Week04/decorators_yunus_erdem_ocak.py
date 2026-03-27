import time
import tracemalloc
import functools

def performance(func):
    # Initialize attributes on the decorator function
    if not hasattr(performance, "counter"):
        performance.counter = 0
        performance.total_time = 0.0
        performance.total_mem = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        performance.counter += 1
        
        # Start tracking memory and time
        tracemalloc.start()
        start_time = time.perf_counter()
        
        result = func(*args, **kwargs)
        
        # Stop tracking
        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        performance.total_time += (end_time - start_time)
        performance.total_mem += peak  # Adding peak memory consumed during this call
        
        return result
    
    return wrapper

# Example usage:
@performance
def test_func():
    return [i for i in range(10000)]
