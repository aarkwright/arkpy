from functools import wraps
from time import perf_counter


"""
Some decorators.

For the curious, see: https://gist.github.com/aarkwright/723c9b9dfca7c23442c55da8d95cd0c1
"""


def stopwatch(func):
    """
    Decorator that measures the execution time of the function being wrapped.

    :param func: a function, with or w/out parameters
    :return: prints out the execution time of the wrapped function
    """

    @wraps(func)
    def _measure_time(*args, **kwargs):
        # Register start time
        start = perf_counter()

        # Gracefully try
        try:
            # Handle functions that take arguments
            return func(*args, **kwargs)

        finally:
            # Register end time
            end = perf_counter()

            # Get duration
            duration = end - start

            print(f"{func.__name__!r} ran for: {(duration if duration > 0 else 0):>10.4f} s")

    return _measure_time
