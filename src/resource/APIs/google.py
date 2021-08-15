import aiohttp
from aiohttp import ClientSession, ClientResponse
import asyncio

from bs4 import BeautifulSoup


async def short_google_search(queary: str) -> str:
    """Short Google Search"""
    queary = "-".join(queary.split())
    url = f"https://www.google.com/search?q={queary}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as data:
            data = await data.text
            data = await BeautifulSoup(data, "html.parser")
            data = await data.find('div', class_="BNeawe").text
    
    return await data


async def http_request(url: str) -> ClientResponse:
    async with ClientSession() as session:
        async with session.get(url) as data:
            return data


if __name__ == '__main__':
    url = f"http://ip-api.com/json/"
    response = asyncio.run(http_request(url))
    print(response.text())

