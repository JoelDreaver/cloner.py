import math
import requests
import os
import git

import config

# To determine how many pages are there
# v3 API: https://developer.github.com/v3/
mainurl = "https://api.github.com/users/{0}".format(config.USERNAME)
wc = requests.get(mainurl)
total = wc.json()["public_repos"]

# range excludes the last one, so, +1
totalpages = math.ceil(total/config.PERPAGE) + 1

if not os.path.isdir(config.PROJPATH):
    os.mkdir(config.PROJPATH)

for page in range(1, totalpages):
    params = {
        "per_page": config.PERPAGE,
        "page": page
    }

    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "cloner.py",
    }

    pageurl = "https://api.github.com/users/{0}/repos".format(config.USERNAME)
    
    wc = requests.get(pageurl, params=params, headers=headers)
    repos = wc.json()
    for repo in repos:
        #git.Git(config.PROJPATH).clone(repo["git_url"])
        print("Cloning: ", repo["git_url"])
