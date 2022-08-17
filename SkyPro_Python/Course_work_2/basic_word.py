class BasicWord:

    def __init__(self, word: str, subwords: list):
        self.word = word
        self.subwords = subwords

    def is_correct(self, subword: str) -> bool:
        if subword in self.subwords:
            return True
        return False

    def count_subwords(self) -> int:
        return len(self.subwords)
