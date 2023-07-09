from playsound import playsound
from dotenv import load_dotenv, find_dotenv
import urllib.request
import requests
import os
import re

load_dotenv(find_dotenv())

SCHOOL_ID = os.environ.get('SCHOOL_ID')
TOKEN = os.environ.get('TOKEN')
API_URL = os.environ.get('API_URL')
HEADERS = {"Authorization": f"Bearer {TOKEN}"}


def get_values_list(dictionary):
    return list(dictionary.values())


def get_alarm_list():
    response = requests.get(f"{API_URL}/api/v1/alarm/list/{SCHOOL_ID}", headers=HEADERS)
    return response.json()


def download_music(url, filename):
    urllib.request.urlretrieve(url, "music/" + filename)


def get_filename(fullname):
    return re.search(r'^([a-f0-9]{32})\.mp3$', fullname).group(1)


def get_list_music():
    return list(map(get_filename, os.listdir("music")))


def get_list_keys(dictionary):
    return list(dictionary.keys())


def play_music(filename):
    playsound(f"music/{filename}.mp3")



