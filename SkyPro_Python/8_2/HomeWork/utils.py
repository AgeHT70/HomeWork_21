import requests
from random import shuffle


class Question:

    def __init__(self, question: str, difficulty_level: int, correct_answer: str):
        self.__question = question
        self.__difficulty_level = difficulty_level
        self.__correct_answer = correct_answer
        self.__is_question = False
        self.__user_answer = None
        self.__points = self.get_points()

    def __repr__(self):
        return f"{self.__question}, {self.__is_question}"

    @property
    def question(self):
        return self.__question

    @property
    def difficulty_level(self):
        return self.__difficulty_level

    @property
    def correct_answer(self):
        return self.__correct_answer

    @property
    def is_question(self):
        return self.__is_question

    @property
    def user_answer(self):
        return self.__user_answer

    @property
    def points(self):
        return self.__points

    @question.setter
    def question(self, question: str):
        self.__question = question

    @difficulty_level.setter
    def difficulty_level(self, difficulty_level: int):
        self.__difficulty_level = difficulty_level

    @correct_answer.setter
    def correct_answer(self, correct_answer: str):
        self.__correct_answer = correct_answer

    @is_question.setter
    def is_question(self, is_ask):
        self.__is_question = is_ask

    @user_answer.setter
    def user_answer(self, user_answer: str):
        self.__user_answer = user_answer

    @points.setter
    def points(self, points: int):
        self.__points = points

    def get_points(self):
        """
        Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        :return:
        """
        self.points = self.difficulty_level * 10
        return self.points

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        return str(self.correct_answer) == self.user_answer

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f'Вопрос: {self.question}\nСложность: {self.difficulty_level}/5\n{self.is_question}'

    def build_positive_feedback(self):
        """Возвращает :
        Ответ верный, получено __ баллов
        """
        return f'Ответ верный, получено {self.points} баллов'

    def build_negative_feedback(self):
        """Возвращает :
        Ответ неверный, верный ответ __
        """
        return f'Ответ неверный, верный ответ {type(self.correct_answer)} {self.correct_answer}'


def load_data(url: str) -> list:
    data = requests.get(url).json()
    return data


def create_questions(data: list) -> list:
    questions = []
    for i in data:
        question = Question(i['q'], int(i['d']), i['a'])
        questions.append(question)
    return questions


def get_question(questions: list) -> Question:
    shuffle(questions)
    if not questions[0].is_question:
        questions[0].is_question = True
        return questions[0]
    else:
        get_question(questions)
