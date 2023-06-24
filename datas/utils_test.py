import json
import logging

from exceptions import (
    CreateBoardNameError,
    CreateListNameError,
    CreateTaskNameError
)


def open_data_file():
    with open(r'.\datas.json', 'r') as file:
        datas = json.load(file)
        # str_datas = json.dumps(datas, indent=4)
        return datas


def verify_boards_name(new_board_name: str, datas: callable = open_data_file()):
    list_boards_name = datas["Each information"]["ListBoardsNames"]
    for name in list_boards_name:
        if new_board_name.lower() in name["board_name"].lower():
            logging.warning(
                f' Conforme nome passado, foi encontrado o grupo: {name["boards_name"]}')
            raise CreateBoardNameError()


def verify_list_name(new_list_name: str, datas: callable = open_data_file()):
    list_name = datas["Each information"]["ListNames"]
    for name in list_name:
        if new_list_name.lower() in name["list_name"].lower():
            logging.warning(
                f' Conforme nome passado, foi encontrada a lista: {name["list_name"]}')
            raise CreateListNameError()


def verify_task_name(tasks_name: str, datas: callable = open_data_file()):
    list_name = datas["Each information"]["TasksList"]
    for name in list_name:
        if tasks_name in name["tasks_name"].lower():
            logging.warning(
                f' Conforme nome passado, foi encontrada a tarefa: {name["tasks_name"]}')
            raise CreateTaskNameError()


if __name__ == '__main__':
    # open_data_file()

    verify_task_name("export c")
    # verify_list_name("don")
    # verify_boards_name("j")
