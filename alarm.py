from methods import play_music, API_URL, SCHOOL_ID, HEADERS
from time import sleep
import requests


def get_answer():

    """Получает бул ответ от бэка, исходя из которого будет/не будет
       проигрываться звонок """

    response = requests.get(f"{API_URL}/api/v1/alarm/status/{SCHOOL_ID}", headers=HEADERS)
    return response.json()


def sync_answers():
    answer = get_answer()["alarm"]
    if answer:
        filename = get_answer()["hash"]
        play_music(filename)


def main_answers():
    while True:
        sync_answers()
        sleep(1)


if __name__ == '__main__':
    main_answers()
