from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

print(fx(45))
print(fx(55))
print(fx(65))
print(fx(75))

print(fx(45))
print(fx(55))
print(fx(65))
print(fx(75))

print(fx(53))
print(fx(63))
print(fx(73))

