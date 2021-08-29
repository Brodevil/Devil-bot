import aiohttp
from aiohttp import ClientSession, ClientResponse
import asyncio

import requests
from bs4 import BeautifulSoup
from random import randint


async def short_google_search(queary: str) -> str:
    """Short Google Search"""
    queary = "-".join(queary.split())
    url = f"https://www.google.com/search?q={queary}"

    data = requests.get(url)
    data = BeautifulSoup(data.text, "html.parser")
    data = data.find("div", class_="BNeawe").text

    return data


async def qna_jokes():
    """Get the random QNA Jokes"""
    url=r"https://readme-jokes.vercel.app/api?bgColor=%23696969&textColor=%23FFC0CB&aColor=%23AFEEEE&borderColor=%23F5F5F5"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as joke:
            joke = await joke.text()
            joke = BeautifulSoup(joke, "html5lib")
            question = joke.find('p', attrs = {'class': "question"})
            answer = joke.find('p', attrs = {'class': "answer"})
            question = str(question).split("</b>")[-1].replace("</p>", "")
            answer = str(answer).split("</b>")[-1].replace("</p>", "")
            return question, answer


if __name__ == "__main__":
    run = asyncio.get_event_loop()
    print(run.run_until_complete(qna_jokes()))
