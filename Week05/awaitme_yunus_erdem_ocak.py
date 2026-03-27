import asyncio
from functools import wraps

def awaitme(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        # Fonksiyonu çağır
        result = func(*args, **kwargs)

        # Eğer sonuç await edilebilir ise await et
        if asyncio.iscoroutine(result):
            return await result

        # Değilse direkt döndür
        return result

    return wrapper 
  @awaitme
def normal_func(x):
    return x * 2

@awaitme
async def async_func(x):
    return x * 3

async def main():
    print(await normal_func(5))  # 10
    print(await async_func(5))   # 15

asyncio.run(main())




@awaitme
def normal_func(x):
    return x * 2

@awaitme
async def async_func(x):
    return x * 3

async def main():
    print(await normal_func(5))  # 10
    print(await async_func(5))   # 15

asyncio.run(main())
