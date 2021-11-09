import os
import requests
import time
import uuid
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert

filepath = os.path.realpath('data.txt')
URL = 'https://www.reddit.com/top/?t=month'
URLPOST = 'https://www.reddit.com/r/antiwork/comments/q82vqk/quit_my_job_last_night_it_was_nice_to_be_home_to/'
HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/\
88.0.4324.150 Safari/537.36',
           'accept': '*/*'}
fields = ['id', 'post_URL', 'username', 'user_karma', 'user_cake_day',
          'post_category', 'post_karma', 'post_date', ' num_comments', 'num_votes']


def get_selenium():
    """Build chrome driver with additional settings"""
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options = Options()
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("start-maximized")
    options.add_experimental_option("prefs", prefs)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('headless')
    driver = webdriver.Chrome(executable_path='/home/alex/PycharmProjects/StudentsLabSemenov_1/parser/chromedriver',
                              options=options)
    return driver


def get_html(url):
    """"""
    driver = get_selenium()
    driver.get(url=url)
    time.sleep(5)
    html = driver.page_source
    with open('data.txt', 'w') as file:
        file.write(html)


def get_content():
    """"""
    post_urls = []
    with open('data.txt') as file:
        soup = BS(file, 'html.parser')
        all_posts = soup.find_all
        feed_items_html = soup.find('div', class_="rpBJOHq2PR60pnwJlUyP0")
        first_post = feed_items_html.find_next()
        print(first_post)


    # title_items = soup.find_all('a', class_="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE")
    # user_items = soup.find_all('a', class_ ="_2mHuuvyV9doV3zwbZPtIPG")
    # for item in title_items:
    #     post_urls.append(item.get('href'))


def parse():
    """"""
    html = get_html(URL)
    # get_content(html)


def main():
    # parse()
    # id = uuid.uuid4().hex
    # get_html(URL, filepath)
    get_content()


if __name__ == "__main__":
    main()



    # find_post_urls = driver.\
    #     find_element_by_class_name("_2tbHP6ZydRpjI44J3syuqC") - post's url