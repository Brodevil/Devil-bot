import aiohttp
from aiohttp import ClientSession, ClientResponse
import asyncio

import requests
from bs4 import BeautifulSoup


async def short_google_search(queary: str) -> str:
    """Short Google Search"""
    queary = "-".join(queary.split())
    url = f"https://www.google.com/search?q={queary}"


    # async with aiohttp.ClientSession() as session:
    #     async with session.get(url) as data:
    #         data = await data.text()
    #         data = BeautifulSoup(data, "html.parser")
    #         data = data.find('div', class_="BNeawe")
    #         print(data)

    data = requests.get(url)
    data = BeautifulSoup(data.text, "html.parser")
    data = data.find("div", class_="BNeawe").text

    return data


async def qna_jokes_img():
    url = r"https://readme-jokes.vercel.app/api?bgColor=%23696969&textColor=%23FFC0CB&aColor=%23AFEEEE&borderColor=%23F5F5F5"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as joke:
            joke = await joke.content
            return joke
