import requests
from random import choice
from basic_word import BasicWord


def load_random_word(url: str) -> BasicWord:
    data = requests.get(url).json()
    basic_word = BasicWord(*choice(data).values())
    return basic_word


# - получит список слов с внешнего ресурса,
# - выберет случайное слово, - создаст экземпляр класса `BasicWord`,
# - вернет этот экземпляр.
