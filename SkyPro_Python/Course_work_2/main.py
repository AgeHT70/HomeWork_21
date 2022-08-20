import os
from player import Player
from basic_word import BasicWord
from utils import load_random_word


def main():
    URL = "https://jsonkeeper.com/b/AD51"

    print("Ввведите имя игрока")
    name = input()

    player = Player(name)
    basic_word = load_random_word(URL)

    print(f"Привет, {player.name}!")
    print(f"Составьте {basic_word.count_subwords()} слов из слова {basic_word.word.upper()}")
    print('Чтобы закончить игру, угадайте все слова или напишите "stop"')
    print("Поехали, ваше первое слово?")

    while player.count_user_subwords() != basic_word.count_subwords():
        user_input = input().lower()
        if user_input in ('stop', 'стоп'):
            break
        elif len(user_input) < 3:
            print("слишком короткое слово")
        elif not basic_word.is_correct(user_input):
            print("неверно")
        elif player.is_used(user_input):
            print("уже использовано")
        else:
            player.add_to_subwords(user_input)
            print("верно")

    print(f"Игра завершена, вы угадали {player.count_user_subwords()} слов!")


if __name__ == '__main__':
    main()
