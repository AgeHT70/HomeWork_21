class Player:

    def __init__(self, name: str):
        self.__name = name
        self.__list_of_subwords = []

    @property
    def name(self):
        return self.__name

    @property
    def list_of_subwords(self):
        return self.__list_of_subwords

    def count_user_subwords(self) -> int:
        return len(self.list_of_subwords)

    def add_to_subwords(self, word: str) -> None:
        self.list_of_subwords.append(word)

    def is_used(self, word: str) -> bool:
        if word in self.list_of_subwords:
            return True
        return False

    def __repr__(self):
        return f"class Player: name {self.name}"
