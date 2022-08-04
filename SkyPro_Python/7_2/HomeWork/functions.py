from os import path
import json


def load_students(filename: str) -> dict:
    """
    Load information about students from json file
    :param filename: name of file with information about students
    :return: dictionary  with decoded information about students
    """
    with open(filename, mode='r', encoding='utf-8') as students_file:
        students = json.load(students_file)
    return students


def load_professions(filename: str) -> dict:
    """
    Load information about professions from json file
    :param filename: name of file with information about professions
    :return: dictionary  with decoded information about professions
    """
    with open(filename, mode='r', encoding='utf-8') as professions_file:
        professions = json.load(professions_file)
    return professions


def get_student_by_pk(pk: int, data: dict) -> dict:
    """
    Get dict with data about student by pk
    :param data: dictionary with all students
    :param pk: number of student
    :return: dictionary with data about student
    """
    for student in data:
        if student["pk"] == pk:
            return student


def get_profession_by_title(title: str, data: dict) -> dict | bool:
    """
    Get dictionary with data about profession by title
    :param data: dictionary with all professions
    :param title: name of profession
    :return: dictionary with data about profession
    """
    for profession in data:
        if profession["title"].lower() == title.lower():
            return profession
    return False


def check_fitness(student: dict, profession: dict) -> dict:
    """
    Get student dict and profession dict return dictionary example:
    {
      "has": ["Python", "Linux"],
      "lacks": ["Docker, SQL"],
      "fit_percent": 50
    }
    :param student: dictionary with data about student
    :param profession: dictionary with data about profession
    :return: dictionary with suitable skills
    """
    has = set(student["skills"]).intersection(set(profession["skills"]))
    lacks = set(profession["skills"]).difference(set(student["skills"]))
    fit_percent = round(len(has) / len(set(profession["skills"])) * 100)
    result_dict = {
        "has": has,
        "lacks": lacks,
        "fit_percent": fit_percent
    }
    return result_dict
