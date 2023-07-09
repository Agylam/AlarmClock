from time import sleep
from methods import *


def filter_music(folder_list, alarm_list):
    backend_list = get_list_keys(alarm_list)

    for f_name in folder_list:
        if f_name not in backend_list:
            os.remove(f"music/{f_name}.mp3")

    for name in backend_list:
        if name not in folder_list:
            url = alarm_list[name]["url"]
            filename = alarm_list[name]["hash"]
            download_music(url, filename + ".mp3")
            print(f"'{name}.mp3' установлен!")


def sync():
    alarm_list = get_alarm_list()
    backend_list = get_list_keys(get_alarm_list())
    folder_list = get_list_music()
    filter_music(folder_list, alarm_list)


def main():
    while True:
        sync()
        sleep(5)


if __name__ == "__main__":
    main()
