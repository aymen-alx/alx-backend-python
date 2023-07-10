#!/usr/bin/env python3
""" Asyncs """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measure run time.
    """
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = (time.perf_counter() - s) / n
    return elapsed
