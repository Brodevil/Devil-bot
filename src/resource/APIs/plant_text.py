from typing import getLogger

import asyncio
import aiohttp
import json

log = getLogger(__name__)


async def get_quote() -> str:
    url = "https://zenquotes.io/api/random"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as quote:
            quote = await quote.json()
            quote = quote[0]["q"] + " -" + quote[0]["a"]

    return quote
