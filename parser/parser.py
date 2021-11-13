import os
import re
import requests
import time
import uuid
from models import GoalPost
from datetime import datetime
from datetime import timedelta
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert


filepath = os.path.realpath('data.txt')
URL = 'https://www.reddit.com/top/?t=month'
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
    """"""
    if 'days' in parsed_date:
        parsed_date = int(parsed_date[:2])
        now = datetime.now()
        new_date = (now - timedelta(parsed_date)).strftime("%Y-%m-%d")
        return new_date
    else:
        new_date = datetime.now().strftime("%d-%m-%Y")
        return new_date


def get_html_and_page_height(url):
    """"""
    driver = get_selenium()
    driver.get(url=url)
    new_page_height = driver.execute_script("return document.body.scrollHeight")
    html = driver.page_source
    with open('parser/data.txt', 'w') as file:
        file.write(html)
    return new_page_height


def get_posts(this_is_first_cicle=True, last_post_id=''):
    """"""
    with open('parser/data.txt') as file:
        soup = BS(file, 'html.parser')
    all_posts = soup.find_all
    feed_items_html = soup.find('div', class_="rpBJOHq2PR60pnwJlUyP0")
    if this_is_first_cicle:
        first_post = feed_items_html.find_next()
        gross_posts_list = [first_post]
        all_posts = first_post.find_next_siblings()

        for post in all_posts:
            gross_posts_list.append(post)
        return gross_posts_list
    else:
        new_first_post = feed_items_html.find('div', id=last_post_id)
        gross_posts_list = [new_first_post]
        all_posts = new_first_post.find_next_siblings()

        for post in all_posts:
            gross_posts_list.append(post)
        return gross_posts_list


def get_content_from_posts(gross_posts_list, clean_posts_dict):
    """"""
    not_a_posts_num = 0
    posts_num = len(gross_posts_list)
    pattern = '_1oQyIsiPHYt6nx7VOmd1sz'
    for item in gross_posts_list:
        g_post = GoalPost()  # ToDo setters for all attributes?
        try:
            post_id_html = item.find('div', class_=re.compile(pattern)).get('id')
            g_post.post_id_html = post_id_html
            g_post.post_url = item.find('a', class_='SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE').get('href')
            g_post.post_category = item.find('a', class_="_3ryJoIoycVkA88fy40qNJc").get('href')
            g_post.username = item.find('a', class_="_2tbHP6ZydRpjI44J3syuqC _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE").get('href')
            g_post.post_date = get_post_date(item.find('a', class_="_3jOxDPIQ0KaOWpzvSQo-1s").text)
            g_post.num_votes = item.find('div', class_="_1rZYMD_4xY3gRcSS3p8ODO _3a2ZHWaih05DgAOtvu6cIo").text
            g_post.num_comments = item.find('span', class_="FHCV02u6Cp2zYL0fhQPsO").text

            clean_posts_dict[post_id_html] = g_post
        except:
            not_a_posts_num += 1
            print('cant find data')

    print(f'not posts - {not_a_posts_num}')
    posts_num = posts_num - not_a_posts_num
    print(f'posts num - {posts_num}')
    return clean_posts_dict


def parser():
    """"""
    html = get_html_and_page_height(URL)
    # get_content(html)


def main():
    # parser()
    # id = uuid.uuid4().hex
    new_page_height = get_html_and_page_height(URL)
    print(new_page_height)
    print(type(new_page_height))
    posts = get_posts()
    a = get_content_from_posts(posts, {})
    for i in a.values():
        print(i)

    # сюда двигается страница  1-class="FohHGMokxXLkon1aacMoi" 2-class="_1yYeg-XN7v7i06TrK8Lh13"


if __name__ == "__main__":
    main()
