import json


def load_candidates(filename):
    with open(filename) as file:
        data = json.load(file)
    return data


def get_all(data):
    out_str = ''
    for candidate in data:
        out_str += f'{candidate["name"]}\n{candidate["position"]}\n{candidate["skills"]}\n\n'

    return out_str


def get_by_pk(data, pk):
    out_str = ''
    for candidate in data:
        if candidate["pk"] == pk:
            out_str += f'{candidate["name"]}\n{candidate["position"]}\n{candidate["skills"]}\n\n'

    return out_str


def get_by_skill(data, skill_name):
    out_str = ''
    for candidate in data:
        if skill_name.lower() in candidate["skills"].lower():
            out_str += f'{candidate["name"]}\n{candidate["position"]}\n{candidate["skills"]}\n\n'

    return out_str
