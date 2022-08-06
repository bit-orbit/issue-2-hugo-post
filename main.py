#!/usr/bin/env python3

from core import Issue
import requests
import config


if __name__ == '__main__':
    print('requesting data') if config.DEBUG else ...
    data = requests.get(config.REPO_API)
    while data.status_code != 200:
        print('request fail, trying again') if config.DEBUG else ...
        data = requests.get(config.REPO_API)

    print('data received') if config.DEBUG else ...

    for i in data.json():
        issue = Issue(i)
        print(f'founded labels are: {issue.labels}, saving data') if config.DEBUG else ...
        with open(f'{config.PUBLISH_DIR}/{issue.title}.md', 'w') as fli:
            fli.write(issue.body)
            print(f'data saved') if config.DEBUG else ...
