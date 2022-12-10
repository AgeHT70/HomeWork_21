from entities.basestorage import BaseStorage
from exceptions import ManyProductsError


class Shop(BaseStorage):
    def __init__(self, items: dict[str, int], capacity: int = 20):
        super().__init__(items, capacity)

