# Создайте класс `Player`. Этот класс будет содержать в себе:
#
# **Поля:**
#
# - имя пользователя,
# - использованные слова пользователя.
#
# **Методы:**
#
# - получение количества использованных слов (возвращает int);
# - добавление слова в использованные слова (ничего не возвращает);
# - проверка использования данного слова до этого (возвращает bool).
#
# Не забудьте определить метод  `__repr__`

class Player:

    def __init__(self, name: str):
        self.name = name
        self.user_subwords = []

    def count_user_subwords(self) -> int:
        return len(self.user_subwords)

    def add_to_subwords(self, word: str):
        self.user_subwords.append(word)

    def is_used(self, word: str) -> bool:
        if word in self.user_subwords:
            return True
        return False

    def __repr__(self):
        return f"class Player: name {self.name}"
