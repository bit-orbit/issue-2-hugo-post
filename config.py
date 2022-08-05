"""all variable in this file are configs"""
from os.path import join


DOMAIN = 'github.com'

REPO_OWNER = ''

REPO_NAME = ''

PUBLISH_DIR = ''

REPO_API = join(f'https://api.{DOMAIN}', 'repos', REPO_OWNER, REPO_NAME)

REPO_ADDR = join(f'https://{DOMAIN}', REPO_OWNER, REPO_NAME)
