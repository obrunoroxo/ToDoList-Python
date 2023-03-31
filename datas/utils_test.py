import json
from pprint import pprint as pp


def open_data_file():
    with open(r'.\datas.json', 'r') as file:
        datas = json.load(file)
        str_datas = json.dumps(datas, indent=4)
        return print(str_datas)


def verify_boards_name(name_boards: str):
    with open(r'.\datas.json', 'r') as file:
        datas = json.load(file)

        list_boards_name = datas["Each information"]["ListBoardsNames"]
        for name in list_boards_name:
            if name_boards in name["boards_name"].lower():
                print(
                    f' Conforme nome passado foi achado o grupo: {name["boards_name"]}')


def verify_list_name(list_name_passed: str):
    with open(r'.\datas.json', 'r') as file:
        datas = json.load(file)

        list_name = datas["Each information"]["ListNames"]
        for name in list_name:
            if list_name_passed in name["list_name"].lower():
                print(
                    f' Conforme nome passado foi achado a lista: {name["list_name"]}')


def verify_task_name(tasks_name: str):
    with open(r'.\datas.json', 'r') as file:
        datas = json.load(file)

        list_name = datas["Each information"]["TasksList"]
        for name in list_name:
            if tasks_name in name["tasks_name"].lower():
                print(
                    f' Conforme nome passado foi achado a lista: {name["tasks_name"]}')


if __name__ == '__main__':
    open_data_file()

    # verify_task_name("export c")
    # verify_list_name("don")
    # verify_boards_name("reactcalendar")
