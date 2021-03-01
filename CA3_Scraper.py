import requests
import json
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


folders = retrieve_folders()  # calling functions
content = retrieve_files(folders)
data = format_content(content)
print(data)
