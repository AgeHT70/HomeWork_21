import json


def load_candidates(filename: str) -> list[dict]:
    """
    Loads data from json-file.
    :param filename: name of json-file
    :return: list of dictionaries with data
    """
    with open(filename) as file:
        data = json.load(file)
    return data


def get_all(data: list[dict]) -> str:
    """
    Return all candidate
    :param data: list of dictionaries with data
    :return: formatted string
    """
    out_str = ''
    for candidate in data:
        out_str += f'{candidate["name"]}\n{candidate["position"]}\n{candidate["skills"]}\n\n'
    return out_str


def get_by_pk(data: list[dict], pk: int) -> str:
    """
    Return candidate by pk
    :param data: list of dictionaries with data
    :param pk: primary key
    :return: formatted string
    """
    out_str = ''
    for candidate in data:
        if candidate["pk"] == pk:
            out_str += f'{candidate["name"]}\n{candidate["position"]}\n{candidate["skills"]}\n\n'
    return out_str


def get_by_skill(data: list[dict], skill_name: str) -> str:
    """
    Return candidate by skill name
    :param data: dictionary with data
    :param skill_name: name of skill
    :return: formatted string
    """
    out_str = ''
    for candidate in data:
        if skill_name.lower() in candidate["skills"].lower().split(', '):
            out_str += f'{candidate["name"]}\n{candidate["position"]}\n{candidate["skills"]}\n\n'
    return out_str
