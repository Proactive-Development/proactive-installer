import urllib.request
import json
import os
def get_repositories(org):
    url = 'https://api.github.com/orgs/' + org + '/repos'
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = json.loads(response.read().decode())
    return [repo['name'] for repo in data]

if __name__ == "__main__":
    if input("Do you want to install all the public Proactive Development repository's? [y/N]") == "y":
        pass
    else:
        exit()
    for i in get_repositories('proactive-development'):
        os.system('git clone https://github.com/Proactive-Development/' + i)
