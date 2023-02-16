import re
import requests
from bs4 import BeautifulSoup
import random
import pandas as pd


def scrape(url):
    _url = requests.get(url=url, )

    soup = BeautifulSoup(_url.content, 'html.parser')

    quotes = []
    authors = []

    allLinks = soup.find_all("div",
                             {"class": "post-content description cf entry-content has-share-float content-spacious"})
    for link in allLinks:
        allText = link.find_all('p')
        for _text in allText:
            # print(_text.prettify())
            temp = (str)(_text.text)
            if (temp.find("“") != -1):
                temp = temp.replace("“", "")
                temp = temp.replace("”", "")
                temp = temp.replace("â€", "")
                
                quotes.append(temp)

            if (temp.find("– ") != -1 and len(temp) < 20):
                authors.append(temp)

    lent = min(len(authors), len(quotes))

    df = pd.DataFrame(quotes[:lent], authors[:lent])
    df.to_csv("a2.csv", header=False, mode='a', )


scrape('https://www.analytixlabs.co.in/blog/40-best-artificial-intelligence-quotes/')