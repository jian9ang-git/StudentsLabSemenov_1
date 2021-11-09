import os
import requests
import time
import uuid
from datetime import datetime
from datetime import timedelta
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


def get_post_date(parsed_date):
    if 'days' in parsed_date:
        parsed_date = int(parsed_date[:2])
        now = datetime.now()
        new_date = (now - timedelta(parsed_date)).strftime("%Y-%m-%d")
        return new_date
    else:
        new_date = datetime.now().strftime("%d-%m-%Y")
        return new_date


def get_html(url):
    """"""
    driver = get_selenium()
    driver.get(url=url)
    time.sleep(5)
    html = driver.page_source
    with open('data.txt', 'w') as file:
        file.write(html)


def get_posts():
    """"""
    with open('data.txt') as file:
        soup = BS(file, 'html.parser')
        all_posts = soup.find_all
        feed_items_html = soup.find('div', class_="rpBJOHq2PR60pnwJlUyP0")
        first_post = feed_items_html.find_next()
        all_posts_list = [first_post]
        all_posts = first_post.find_next_siblings()

        for post in all_posts:
            all_posts_list.append(post)

        return all_posts_list


def get_content_from_posts(all_posts_list):
    error_counter = 0
    a = len(all_posts_list)

    for item in all_posts_list:
        try:
            post_url = item.find('a', class_='SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE').get('href')
            post_category = item.find('a', class_="_3ryJoIoycVkA88fy40qNJc").get('href')
            username = item.find('a', class_="_2tbHP6ZydRpjI44J3syuqC _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE") \
                .get('href')
            date = get_post_date(item.find('a', class_="_3jOxDPIQ0KaOWpzvSQo-1s").text)

            print(date)
        except:
            error_counter += 1
            print('cant find data')
    print(error_counter)


def parser():
    """"""
    html = get_html(URL)
    # get_content(html)


def main():
    # parse()
    # id = uuid.uuid4().hex
    # get_html(URL)
    posts = get_posts()
    get_content_from_posts(posts)


if __name__ == "__main__":
    main()
