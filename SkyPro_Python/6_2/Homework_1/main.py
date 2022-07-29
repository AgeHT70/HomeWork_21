from functions import *


def main():
    HISTORY_TXT = 'history.txt'
    WORDS_TXT = 'words.txt'
    score = 0
    word_list = get_wordlist(WORDS_TXT)

    print("Введите Ваше имя")
    user_name = input()

    for question in word_list:
        print(f'Угадайте слово: {to_shake_word(question)}')
        answer = input().lower()
        if answer == question:
            print(f'Верно! Вы получаете 10 очков.')
            score += 10
        else:
            print(f'Неверно! Верный ответ – {question}.')

    write_statistic(user_name, score, HISTORY_TXT)
    stat = read_statistic(HISTORY_TXT)

    print(f'Всего игр сыграно:{stat[0]}')
    print(f'Максимальный рекорд:{stat[1]}')


if __name__ == "__main__":
    main()
