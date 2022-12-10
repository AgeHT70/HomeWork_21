from exceptions import NotEnoughSpaceError, InvalidRequestError, \
    UnknownStorageError, ManyProductsError
from entities.storage import Storage


class Request:
    def __init__(self, request_str: str, storages: dict[str, Storage]):
        split_request = request_str.split(' ')

        if len(split_request) != 7 or not split_request[1].isdigit():
            raise InvalidRequestError

        self._from: str = split_request[4]
        self._to: str = split_request[6]
        self._amount: int = int(split_request[1])
        self._product: str = split_request[2]

        if self._from not in storages or self._to not in storages:
            raise UnknownStorageError

        self.departure = storages[self._from]
        self.destination = storages[self._to]

    def move(self):
        if self.destination.get_free_space() < self._amount:
            raise NotEnoughSpaceError

        if self.destination.get_unique_items_count() >= 5:
            raise ManyProductsError

        self.departure.remove(self._product, self._amount)
        print(f'Нужное количество есть на складе')
        print(f'Курьер забрал {self._amount} {self._product} со {self._from}')
        print(
            f'Курьер везет {self._amount} {self._product} со '
            f'{self._from} в {self._to}')

        self.destination.add(self._product, self._amount)
        print(f'Курьер доставил {self._amount} {self._product} в {self._to}')

