from exceptions import BaseError
from entities.request import Request
from entities.shop import Shop
from entities.store import Store

shop = Shop(items={"собачки": 2, "печеньки": 5, }, )
store = Store(items={"собачки": 2, "печеньки": 50, "коробки": 5}, )

storages = {"магазин": shop, "склад": store, }


def main():
    while True:

        for storage_name in storages:
            print(f"\nВ {storage_name} хранится:")
            for key, value in storages[storage_name].items.items():
                print(f"{value} {key}")

        user_input = input(
            'Для выхода наберите стоп или stop.\n'
            'Введите строку в формате:" Доставить 3 печеньки из склад в '
            'магазин"\n')

        if user_input in ["stop", "стоп"]:
            break
        try:
            request = Request(request_str=user_input, storages=storages)
            request.move()
        except BaseError as error:
            print(error.message)


if __name__ == '__main__':
    main()
