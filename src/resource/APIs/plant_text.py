from logging import getLogger

import asyncio
import aiohttp
from json import loads

__all__= ("get_quote", )
log = getLogger(__name__)


async def get_quote() -> str:
    url = "https://zenquotes.io/api/random"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as quote:
            quote = await quote.text()
            quote = loads(quote)
            return quote[0]["q"], quote[0]["a"]
