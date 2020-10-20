#!/usr/bin/env python3
''' async and await syntax '''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    ''' Function that returns the delay '''
    R = random.uniform(0, max_delay)
    await asyncio.sleep(R)
    return R
