#!/usr/bin/env python3
'''Import wait_random from the previous python file that you’ve written and
    write an async routine called wait_n that takes in 2 int arguments:
    max_delay and n
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes wait_random n times.
    '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
