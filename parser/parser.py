import os
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


filepath = os.path.realpath('data.txt')
URL = 'https://www.reddit.com/top/?t=month'
URLPOST = 'https://www.reddit.com/r/antiwork/comments/q82vqk/quit_my_job_last_night_it_was_nice_to_be_home_to/'
HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/\
88.0.4324.150 Safari/537.36',
           'accept': '*/*'}


def get_html(url, params=None):
    """"""
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    """"""
    soup = BeautifulSoup(html, 'html.parser')
    title_items = soup.find_all('a', class_="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE")
    # user_items = soup.find_all('a', class_ ="_2mHuuvyV9doV3zwbZPtIPG")
    print(title_items)


def parse():
    """"""
    html = get_html(URL)
    get_content(html.text)


def main():
    """"""
    parse()


if __name__ == "__main__":
    main()
