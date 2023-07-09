import time
import requests
# from pprint import pprint
from time import sleep
from dotenv import load_dotenv, find_dotenv
import os
import urllib.request
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


# Музыка для скачивания/удаления остается в бэке/фолдере
def filter_music(folder_list, alarm_list):
    backend_list = get_list_keys(alarm_list)
    # print(folder_list, backend_list)

    for f_name in folder_list:
        if f_name not in backend_list:
            os.remove(f"music/{f_name}.mp3")

    for name in backend_list:
        if name not in folder_list:
            url = alarm_list[name]["url"]
            filename = alarm_list[name]["hash"]
            download_music(url, filename + ".mp3")
            print(name)


    # Удаляться, если его нет в бэке но есть в фолдер листе
    # Скачиваться, когда его нет в фолдере и есть в бэке

def sync():
    alarm_list = get_alarm_list()
    backend_list = get_list_keys(get_alarm_list())
    folder_list = get_list_music()
    filter_music(folder_list, alarm_list)

    # print(backend_list)
    # print(folder_list)
    # pprint(alarm_list())


def main():
    while True:
        sync()
        time.sleep(5)


if __name__ == "__main__":
    main()

