"""all variable in this file are configs"""
from os.path import join
import os


DOMAIN = 'github.com'

REPO_OWNER = os.environ.get('OWNER')

REPO_NAME = os.environ.get('REPO')

PUBLISH_DIR = os.environ.get('PUB_DIR')

REPO_API = join(f'https://api.{DOMAIN}', 'repos', REPO_OWNER, REPO_NAME, 'issues')

REPO_ADDR = join(f'https://{DOMAIN}', REPO_OWNER, REPO_NAME)
