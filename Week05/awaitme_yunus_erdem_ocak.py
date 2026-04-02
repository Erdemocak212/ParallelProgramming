import asyncio
import inspect
from functools import wraps


def awaitme(func):
    """
    A decorator that turns any function into a coroutine.
    - Passes all args/kwargs correctly
    - Preserves return value
    """

    @wraps(func)
    async def wrapper(*args, **kwargs):
        # If function is already async, just await it
        if inspect.iscoroutinefunction(func):
            return await func(*args, **kwargs)

        # Run sync function in a thread to avoid blocking event loop
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, lambda: func(*args, **kwargs))

    return wrapper


# Example usage
if __name__ == "__main__":

    @awaitme
    def add(a, b):
        return a + b

    @awaitme
    async def async_add(a, b):
        await asyncio.sleep(1)
        return a + b

    async def main():
        result1 = await add(2, 3)
        result2 = await async_add(5, 7)
        print("add result:", result1)
        print("async_add result:", result2)

    asyncio.run(main())
