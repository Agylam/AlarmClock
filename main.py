import requests
from pprint import pprint
from dotenv import load_dotenv, find_dotenv
import os
import urllib.request
import re


load_dotenv(find_dotenv())

SCHOOL_ID = os.environ.get('SCHOOL_ID')
TOKEN = os.environ.get('TOKEN')
API_URL = os.environ.get('API_URL')
HEADERS = {"Authorization": f"Bearer {TOKEN}"}


def alarm_list():
    response = requests.get(f"{API_URL}/api/v1/alarm/list/{SCHOOL_ID}", headers=HEADERS)
    return response.json()


def download_music(url, filename):
    urllib.request.urlretrieve(url, "music/" + filename)


def get_filename(fullname):
    return re.search(r'^([a-f0-9]{32})\.mp3$', fullname).group(1)


def get_list_music():
    return list(map(get_filename, os.listdir("music")))


# print(get_list_music())

pprint(alarm_list())

