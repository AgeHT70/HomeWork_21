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


def get_by_id(data: list[dict], uid: int) -> dict:
    """
    Return candidate by uid
    :param data: list of dictionaries with data
    :param uid: candidate`s id
    :return:
    """
    for candidate in data:
        if candidate["id"] == uid:
            return candidate


def get_by_skill(data: list[dict], skill_name: str) -> list:
    """
    Return list of candidates by skill name
    :param data: dictionary with data
    :param skill_name: name of skill
    :return:
    """

    matching_candidates = []
    for candidate in data:
        if skill_name.lower() in candidate["skills"].lower().split(', '):
            matching_candidates.append(candidate)
    return matching_candidates


def get_by_name(data: list[dict], name: str) -> list:
    """
    Return list of candidates by name
    :param data:
    :param name:
    :return:
    """
    matching_candidates = []
    for candidate in data:
        if name.lower() in candidate["name"].lower():
            matching_candidates.append(candidate)
    return matching_candidates
