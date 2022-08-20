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
        if subword in self.subwords:
            return True
        return False

    def count_subwords(self) -> int:
        return len(self.subwords)

    def __repr__(self):
        return f"class - BasicWord: word - {self.word}"
