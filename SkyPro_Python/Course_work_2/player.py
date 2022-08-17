class Player:

    def __init__(self, name: str):
        self.name = name
        self.user_subwords = []

    def count_user_subwords(self) -> int:
        return len(self.user_subwords)

    def add_to_subwords(self, word: str) -> None:
        self.user_subwords.append(word)

    def is_used(self, word: str) -> bool:
        if word in self.user_subwords:
            return True
        return False

    def __repr__(self):
        return f"class Player: name {self.name}"
