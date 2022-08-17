import requests
from Question import Question


def load_data(url: str) -> list:
    """
    Load json_file from URL
    :param url:
    :return: List of dictionaries
    """
    data = requests.get(url).json()
    return data


def create_questions(data: list) -> list:
    """
    Create list of objects Question
    :param data:
    :return: list of objects Question
    """
    questions = [Question(element['q'], int(element['d']), element['a']) for element in data]
    return questions


def get_statistics(questions_list) -> str:
    """
    Return statistic of game
    :param questions_list:
    :return: f-string with statistic
    """

    rigth_answer_counter = 0
    total = 0
    for question in questions_list:
        if question.is_correct():
            rigth_answer_counter += 1
            total += question.points

    return f"Вот и всё!\nОтвечено {rigth_answer_counter} вопроса из {len(questions_list)}\nНабрано баллов: {total}\n"
