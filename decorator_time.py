import time
from functools import wraps


def timer(unit="s"):
    multipliers = {"s": 1, "ms": 1e3, "us": 1e6}

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            try:
                return func(*args, **kwargs)
            finally:
                elapsed = (time.perf_counter() - start) * multipliers[unit]
                print(f"{func.__name__}: {elapsed:.4f} {unit}")
        return wrapper
    return decorator


@timer(unit="ms")
def do_something():
    time.sleep(1)
    return "ok"

do_something()
