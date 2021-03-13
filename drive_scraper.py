import requests
from requests import get, post
import json
from dateutil import parser
from datetime import datetime, timedelta
from bs4 import BeautifulSoup  # importing modules


def retrieve_videos():
    repo_url = 'https://drive.google.com/drive/folders/1pFHUrmpLv9gEJsvJYKxMdISuQuQsd_qX'  # setting url

    repo = requests.get(repo_url)  # connecting to url using requests module

    print(repo.status_code)  # code 200 confirms we are connected

    repo_soup = BeautifulSoup(
        repo.content, 'html.parser')  # Beautiful Soup repo

    base = repo_soup.find('div', id="drive_main_page")

    # collecting links to the videos
    links = []
    for item in base.find_all(attrs={"data-id": True}):
        links.append('drive.google.com/file/d/' +
                     item['data-id'] + '/view?usp=sharing')

    # collecting their names
    titles = []
    for item in base.find_all(attrs={"data-tooltip": True}):
        titles.append(str(item['data-tooltip']))
    titles = titles[1:]

    return links, titles


def dates(titles):
    date_ls = []
    for date in titles:
        date = date[0:10]
        # turning string dates to datetime objects
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        date_ls.append(date_obj)

    start = date_ls[0]

    weeks = [1]  # weeks will populate 'sections' starting with 1 for week 1
    for i in date_ls[1:]:
        int_day = (i - start + timedelta(days=7))  # steps of 7 for week
        int_week = int_day / 7  # dividing number of days since start to weeks to get section
        weeks.append(int_week.days)  # adding section to list

    return weeks


links, titles = retrieve_videos()  # links to and the titles of videos
# calling function to generate list of week sections from the titles
weeks = dates(titles)

# zipping together the week and it's link
section_links = dict(zip(weeks, links))


def format_vids(section_links):
    data = []

    for section, link in section_links.items():
        para = '<p>' + '</p><p>' + link + '</p>'
        index = {'section': section, 'summary': para}
        data.append(index)
    return data


video_data = format_vids(section_links)
print(video_data)
