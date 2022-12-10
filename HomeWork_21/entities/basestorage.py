from exceptions import NotEnoughSpaceError, UnknownProductError, \
    NotEnoughProductError
from entities.storage import Storage


class BaseStorage(Storage):
    def __init__(self, items: dict[str, int], capacity: int):
        self._items = items
        self._capacity = capacity

    @property
    def items(self):
        return self._items

    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, value: int) -> None:
        self._capacity = value

    def add(self, title: str, quantity: int) -> None:
        self.items[title] = self.items.get(title, 0) + quantity

    def remove(self, title: str, quantity: int) -> None:
        if title not in self.items:
            raise UnknownProductError

        if self.items[title] < quantity:
            raise NotEnoughProductError

        self.items[title] -= quantity

        if self.items[title] == 0:
            self.items.pop(title)

    def get_free_space(self) -> int:
        return self.capacity - sum(self.items.values())

    def get_items(self) -> dict[str, int]:
        return self.items

    def get_unique_items_count(self) -> int:
        return len(self.items)
