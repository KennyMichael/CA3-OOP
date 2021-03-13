import requests
from requests import get, post
import json
from bs4 import BeautifulSoup
from dateutil import parser
from datetime import datetime, timedelta
from bs4 import BeautifulSoup  # importing modules


def retrieve_folders():
    repo_url = 'https://github.com/KennyMichael/CA3-OOP'  # setting url

    repo = requests.get(repo_url)  # connecting to url using requests module

    # print(repo.status_code)  # code 200 confirms we are connected

    repo_soup = BeautifulSoup(
        repo.content, 'html.parser')  # Beautiful Soup repo

    # navigating github repo to links into folders using class Box-row and div/span tags
    # js-navigation tag selects only folder link not commit
    repo_script = repo_soup.select('div.Box-row div span')
    folders = []
    for week_folder in repo_script:
        # finding links using attribute 'href'
        href_link = week_folder.a.attrs['href']
        if 'wk' in href_link:   # only downloading week folders and not the script file
            folders.append(href_link)  # saving links to folders to a list

    return folders


def retrieve_files(folders):  # function to take files from the folders
    content = {}
    for link in folders:

        folder_url = 'https://github.com' + link  # urls for each of the github folders
        # connecting to folder using the requests module
        folder = requests.get(folder_url)

        folder_soup = BeautifulSoup(
            folder.content, 'html.parser')  # Beautiful Soup folders

        folder_script = folder_soup.select('div.Box-row')

        week_files = []
        for files in folder_script:
            href_link = files.a.attrs['href']
            # collecting only html and pdf files
            if href_link.lower().endswith('.pdf') or href_link.lower().endswith('.html'):
                # saving links to folders to a list
                week_files.append('https://github.com' + href_link)
                content[link] = week_files
    return(content)


def format_content(content):
    data = []
    sec = content.keys()

    for folder in sec:
        # summary section puts files in html paragraph format
        para = '<p>' + '</p><p>'.join(content[folder]) + '</p>'
        # section number taken from last digit of key name
        index = {'section': (folder[-1]), 'summary': para}
        data.append(index)
    return data


def update_moodle(data):
    KEY = "bc7ad59923ad95f17dd955868790ccb5"
    URL = "http://f0ae7213ef73.eu.ngrok.io/"
    ENDPOINT = "/webservice/rest/server.php"

    def rest_api_parameters(in_args, prefix='', out_dict=None):
        """Transform dictionary/array structure to a flat dictionary, with key names
        defining the structure.
        Example usage:
        >>> rest_api_parameters({'courses':[{'id':1,'name': 'course1'}]})
        {'courses[0][id]':1,
        'courses[0][name]':'course1'}
        """
        if out_dict == None:
            out_dict = {}
        if not type(in_args) in (list, dict):
            out_dict[prefix] = in_args
            return out_dict
        if prefix == '':
            prefix = prefix + '{0}'
        else:
            prefix = prefix + '[{0}]'
        if type(in_args) == list:
            for idx, item in enumerate(in_args):
                rest_api_parameters(item, prefix.format(idx), out_dict)
        elif type(in_args) == dict:
            for key, item in in_args.items():
                rest_api_parameters(item, prefix.format(key), out_dict)
        return out_dict

    def call(fname, **kwargs):
        """Calls moodle API function with function name fname and keyword arguments.
        Example:
        >>> call_mdl_function('core_course_update_courses',
                            courses = [{'id': 1, 'fullname': 'My favorite course'}])
        """
        parameters = rest_api_parameters(kwargs)
        parameters.update(
            {"wstoken": KEY, 'moodlewsrestformat': 'json', "wsfunction": fname})
        # print(parameters)
        response = post(URL+ENDPOINT, data=parameters).json()
        if type(response) == dict and response.get('exception'):
            raise SystemError("Error calling Moodle API\n", response)
        return response

    ################################################
    # Rest-Api classes
    ################################################

    class LocalUpdateSections(object):
        """Updates sectionnames. Requires: courseid and an array with sectionnumbers and sectionnames"""

        def __init__(self, cid, sectionsdata):
            self.updatesections = call(
                'local_wsmanagesections_update_sections', courseid=cid, sections=sectionsdata)

    ################################################
    # Example
    ################################################

    # Update sections. Example for onetopic format.
    courseid = "4"  # Exchange with valid id.
    data = data
    sec = LocalUpdateSections(courseid, data)
    print(sec.updatesections)


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
        links.append('https://drive.google.com/file/d/' +
                     item['data-id'] + '/view?usp=sharing')

    # collecting their names
    titles = []
    for item in base.find_all(attrs={"data-tooltip": True}):
        titles.append(str(item['data-tooltip']))
    titles = titles[1:]

    return links, titles


def update_moodle(data):
    KEY = "bc7ad59923ad95f17dd955868790ccb5"
    URL = "http://f0ae7213ef73.eu.ngrok.io/"
    ENDPOINT = "/webservice/rest/server.php"

    def rest_api_parameters(in_args, prefix='', out_dict=None):
        """Transform dictionary/array structure to a flat dictionary, with key names
        defining the structure.
        Example usage:
        >>> rest_api_parameters({'courses':[{'id':1,'name': 'course1'}]})
        {'courses[0][id]':1,
        'courses[0][name]':'course1'}
        """
        if out_dict == None:
            out_dict = {}
        if not type(in_args) in (list, dict):
            out_dict[prefix] = in_args
            return out_dict
        if prefix == '':
            prefix = prefix + '{0}'
        else:
            prefix = prefix + '[{0}]'
        if type(in_args) == list:
            for idx, item in enumerate(in_args):
                rest_api_parameters(item, prefix.format(idx), out_dict)
        elif type(in_args) == dict:
            for key, item in in_args.items():
                rest_api_parameters(item, prefix.format(key), out_dict)
        return out_dict

    def call(fname, **kwargs):
        """Calls moodle API function with function name fname and keyword arguments.
        Example:
        >>> call_mdl_function('core_course_update_courses',
                            courses = [{'id': 1, 'fullname': 'My favorite course'}])
        """
        parameters = rest_api_parameters(kwargs)
        parameters.update(
            {"wstoken": KEY, 'moodlewsrestformat': 'json', "wsfunction": fname})
        # print(parameters)
        response = post(URL+ENDPOINT, data=parameters).json()
        if type(response) == dict and response.get('exception'):
            raise SystemError("Error calling Moodle API\n", response)
        return response

    ################################################
    # Rest-Api classes
    ################################################

    class LocalUpdateSections(object):
        """Updates sectionnames. Requires: courseid and an array with sectionnumbers and sectionnames"""

        def __init__(self, cid, sectionsdata):
            self.updatesections = call(
                'local_wsmanagesections_update_sections', courseid=cid, sections=sectionsdata)

    ################################################
    # Example
    ################################################

    # Update sections. Example for onetopic format.
    courseid = "4"  # Exchange with valid id.
    data = data
    sec = LocalUpdateSections(courseid, data)
    print(sec.updatesections)


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
        links.append('https://drive.google.com/file/d/' +
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

folders = retrieve_folders()  # calling functions
content = retrieve_files(folders)
data = format_content(content)

data2 = video_data + data

update_moodle(data2)
