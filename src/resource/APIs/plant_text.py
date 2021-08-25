from logging import getLogger

import asyncio
import aiohttp
from json import load

__all__= ("get_quote", )
log = getLogger(__name__)


async def get_quote() -> str:
    url = "https://zenquotes.io/api/random"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as quote:
            quote = await quote.text()
            print(quote)
            quote = load(quote)
            return quote[0]["q"], quote[0]["a"]
