import json, pprint

from utils_test import (
    verify_boards_name,
    verify_list_name,
    verify_task_name
)


def read_data_file() -> dict:
    with open(r'.\datas.json', 'r') as file:
        datas = json.load(file)
        return datas


def write_new_datas(datas: dict, new_all_informations: list, new_each_informations: list = None):
    try:
        datas['All informations']['AllDatas'] = new_all_informations
        if new_each_informations != None:
            datas["Each information"]["ListBoardsNames"] = new_each_informations
    except:
        pass
    with open(r'.\datas.json', 'w') as file:
        json.dump(datas, file, indent=4)


def add_board_name(datas: dict, new_board_name: str) -> list:
    verify_boards_name(new_board_name=new_board_name)
    all_datas = datas['All informations']['AllDatas']
    base_structure_all_datas = {
        "board_name": new_board_name,
        "lists": []
    }
    all_datas.append(base_structure_all_datas)

    each_information_board_name = datas["Each information"]["ListBoardsNames"]
    base_structure_list_board_name = {
        "board_name": new_board_name
    }
    each_information_board_name.append(base_structure_list_board_name)

    return all_datas, each_information_board_name


def add_list_name(datas: dict, new_list_name: str, board_name: str) -> list:
    verify_list_name(new_list_name=new_list_name)
    all_datas = datas['All informations']['AllDatas']
    base_structure_all_datas = {
        "name": new_list_name,
        "tasks": []
    }
    for data in all_datas:
        if data.get('board_name') and board_name.lower() in data['board_name'].lower():
            data['lists'].append(base_structure_all_datas)
        else:
            continue
    all_datas.append(data)

    return all_datas





if __name__ == '__main__':
    datas = read_data_file()
    # all_datas, each_information_board_name = add_board_name(datas = datas, new_board_name = 'Compras mercado')
    d = add_list_name(datas=datas, new_list_name='Prototypes', board_name='reactcalendar')
    # print(d)
    write_new_datas(
        datas = datas,
        new_all_informations = d,
        # new_each_informations = None
    )
