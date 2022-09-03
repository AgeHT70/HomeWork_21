import json


def load_candidates(filename: str) -> dict:
    """
    Loads data from json-file.
    :param filename: name of json-file
    :return: dictionary with data
    """
    with open(filename) as file:
        data = json.load(file)
    return data


def get_all(data: dict) -> str:
    """
    Return all candidate
    :param data: dictionary with data
    :return: formatted string
    """
    out_str = ''
    for candidate in data:
        out_str += f'{candidate["name"]}\n{candidate["position"]}\n{candidate["skills"]}\n\n'
    return out_str


def get_by_pk(data: dict, pk: int) -> str:
    """
    Return candidate by pk
    :param data: dictionary with data
    :param pk: primary key
    :return: formatted string
    """
    out_str = ''
    for candidate in data:
        if candidate["pk"] == pk:
            out_str += f'{candidate["name"]}\n{candidate["position"]}\n{candidate["skills"]}\n\n'
    return out_str


def get_by_skill(data: dict, skill_name: str) -> str:
    """
    Return candidate by skill name
    :param data: dictionary with data
    :param skill_name: name of skill
    :return: formatted string
    """
    out_str = ''
    for candidate in data:
        if skill_name.lower() in candidate["skills"].lower():
            out_str += f'{candidate["name"]}\n{candidate["position"]}\n{candidate["skills"]}\n\n'
    return out_str
