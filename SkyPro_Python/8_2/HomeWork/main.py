class Question:

    def __init__(self, question, difficulty_level, correct_answer, is_question=False, user_answer=None):
        self.question = question
        self.difficulty_level = difficulty_level
        self.correct_answer = correct_answer
        self.is_question = is_question
        self.user_answer = user_answer
        self.points = 10 * difficulty_level

    def get_points(self):
        """
        Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        :return:
        """
        return self.points
        pass

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        return self.correct_answer.lower() == self.user_answer.lower()

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f'Вопрос: {self.question}\nСложность: {self.difficulty_level}/5'

    def build_positive_feedback(self):
        """Возвращает :
        Ответ верный, получено __ баллов
        """
        return f'Ответ верный, получено {self.points} баллов'

    def build_negative_feedback(self):
        """Возвращает :
        Ответ неверный, верный ответ __
        """
        return f'Ответ неверный, верный ответ  {self.correct_answer}'



def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')
