import requests
import json
from bs4 import BeautifulSoup  # importing modules

repo_url = 'https://github.com/KennyMichael/CA3-OOP'  # setting url

repo = requests.get(repo_url)  # connecting to url using requests module

# print(repo.status_code)  # code 200 confirms we are connected

repo_soup = BeautifulSoup(repo.content, 'html.parser')  # Beautiful Soup repo

# navigating github repo to links into folders using class Box-row and div/span tags
# js-navigation tag selects only folder link not commit
repo_script = repo_soup.select('div.Box-row div span')
folders = []
for week_folder in repo_script:
    # finding links using attribute 'href'
    href_link = week_folder.a.attrs['href']
    folders.append(href_link)  # saving links to folders to a list

# print(folders)


# print(folders[0::2]) trying to get rid of commit hyperlinks

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
        week_files.append(href_link)  # saving links to folders to a list
        print(week_files)
        # content[link] = week_files


print(content)
