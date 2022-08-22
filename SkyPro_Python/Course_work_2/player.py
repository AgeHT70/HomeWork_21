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
        """
        Counting words composed by the user
        :return: length of the list
        """
        return len(self.list_of_subwords)

    def add_to_subwords(self, word: str) -> None:
        """
        Add the word into the list
        :param word:
        :return:
        """
        self.list_of_subwords.append(word)

    def is_used(self, word: str) -> bool:
        """
        Check the word in the list
        :param word:
        :return:
        """
        if word in self.list_of_subwords:
            return True
        return False

    def __repr__(self):
        return f"class Player: name {self.name}"
