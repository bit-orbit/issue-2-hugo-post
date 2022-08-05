from core import Issue
import requests
import config


data = requests.get(config.REPO_API)
while data.status_code != 200:
    data = requests.get(config.REPO_API)

for i in data.json():
    issue = Issue(i)
    issue.get_issue_context()
    for label in issue.labels:
        print(label)
        with open(f'{config.PUBLISH_DIR}/{issue.title}.md', 'w') as fli:
            fli.write(issue.body)



