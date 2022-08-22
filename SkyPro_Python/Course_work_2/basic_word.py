class BasicWord:

    def __init__(self, word: str, subwords: list):
        self.__word = word
        self.__subwords = subwords

    @property
    def word(self):
        return self.__word

    @property
    def subwords(self):
        return self.__subwords

    def is_correct(self, subword: str) -> bool:
        """
        This method checks the word in the list of subwords
        :param subword:
        :return:True or False
        """
        if subword in self.subwords:
            return True
        return False

    def count_subwords(self) -> int:
        """
        This method counts the number of words that can be formed from a main word.
        :return: length of the list of subwords
        """
        return len(self.subwords)

    def __repr__(self):
        return f"class - BasicWord: word - {self.word}"
