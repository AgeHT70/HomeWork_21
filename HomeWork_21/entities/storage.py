from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def add(self, title: str, quantity: int) -> None:
        """Увеличивает запас items"""
        pass

    @abstractmethod
    def remove(self, title: str, quantity: int) -> None:
        """Уменьшает запас items"""
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        """Возвращает количество свободных мест"""
        pass

    @abstractmethod
    def get_items(self) -> dict[str, int]:
        """Возвращает содержимое склада в словаре {товар: количество}"""
        pass

    @abstractmethod
    def get_unique_items_count(self) -> int:
        """Возвращает количество уникальных товаров"""
        pass
