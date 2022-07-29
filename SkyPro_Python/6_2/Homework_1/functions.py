from random import shuffle


def get_wordlist(filename) -> list:
    """
    This function reads words from file
    :return:
    """
    with open(filename, 'r', encoding='utf-8') as file:
        word_list = []
        for data in file:
            word_list.append(data.rstrip())
    return word_list


def to_shake_word(word: str) -> str:
    """
    This function shake symbols in word
    :param word:
    :return:
    """
    shuffle_word = list(word)
    shuffle(shuffle_word)
    return ''.join(shuffle_word)


def write_statistic(user_name: str, result: int, filename: str) -> bool:
    """
    This function write result of game into file
    :param user_name: name of user
    :param result: result of game
    :param filename: name of file
    :return:
    """
    with open(filename, 'a', encoding='utf-8') as history:
        history.write(f'{user_name}:{result}\n')
    return True


def read_statistic(filename: str) -> tuple:
    """
    This function read statistics from file. Return tuple which contain count of games and maximum result
    :param filename: name of file
    :return:
    """
    with open(filename, 'r', encoding='utf-8') as file:
        players = []
        results = []
        for lines in file:
            player, result = lines.split(':')
            players.append(player)
            results.append(int(result))
    out_tuple = (len(players), max(results))
    return out_tuple
