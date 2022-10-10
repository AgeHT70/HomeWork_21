import sqlite3

DB_PATH = 'netflix.db'


def cursor_fetchall(db_path, query):
    """
    Подключение к БД
    :param db_path: путь до файла БД.
    :param query: SQL запрос.
    :return: результат выполнения SQL запроса.
    """
    with sqlite3.connect(db_path) as con:
        cursor = con.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result


def get_movie_by_title(title: str) -> list[dict]:
    """
    Получаем фильм по названию.
    :param title: название фильма.
    :return: список фильмов.
    """
    query = f"""
        SELECT title, country, release_year, listed_in,
                description
        FROM netflix
        WHERE title = {title}
        ORDER BY date_added desc
        LIMIT 1
                """

    result = cursor_fetchall(DB_PATH, query)
    print(result)
    movie_list = [{'title': raw[0], 'country': raw[1], 'release_year': raw[2],
                   'genre': raw[3], 'description': raw[4]} for raw in result]

    return movie_list


def get_movie_by_year(year_from: int, year_to: int) -> list[dict]:
    """
    Получаем список фильмов по дате релиза.
    :param year_from: год релиза "с".
    :param year_to: год релиза "по".
    :return: список фильмов.
    """
    query = f"""
        SELECT title, release_year
        FROM netflix
        WHERE release_year BETWEEN {year_from} AND {year_to}
        LIMIT 100
                """
    result = cursor_fetchall(DB_PATH, query)
    movie_list = [{'title': raw[0], 'release_year': raw[1]} for raw in
                  result]
    return movie_list


def get_movie_by_rating(age: tuple | str) -> list[dict]:
    """
    Получаем список фильмов по возрастному рейтингу.
    :param age: Возрастной рейтинг.
    :return: Список фильмов.
    """
    if len(age) == 1:
        query = f"""
        SELECT title, rating, description
        FROM netflix
        WHERE rating = '{age}'
    """
    else:
        query = f"""
            SELECT title, rating, description
            FROM netflix
            WHERE rating in {age}
        """
    result = cursor_fetchall(DB_PATH, query)
    movie_list = [{'title': raw[0], 'rating': raw[1], 'description': raw[2]}
                  for raw in result]
    return movie_list


def get_movie_by_genre(genre: str) -> list[dict]:
    """
    Получаем список фильмов по жанру.
    :param genre: жанр.
    :return: список фильмов.
    """
    query = f"""
    SELECT title, description
    FROM netflix
    WHERE upper(listed_in) like upper('%{genre}%')
    ORDER BY date_added desc
    LIMIT 10
    """

    result = cursor_fetchall(DB_PATH, query)
    movie_list = [{'title': raw[0], 'description': raw[1]}
                  for raw in result]

    return movie_list


def count_actors(actor_first: str, actor_second: str) -> list[dict]:
    """
    Задание №5
    :param actor_first:
    :param actor_second:
    :return:
    """
    query = f"""
        SELECT "cast" FROM netflix
        WHERE "cast" LIKE ('%{actor_first}%{actor_second}%') or "cast" LIKE 
        ('%{actor_second}%{actor_first}%')
        """
    all_actors = []
    result = cursor_fetchall(DB_PATH, query)

    for raw in result:
        for actor in raw:
            all_actors.extend(actor.split(', '))

    keys_for_count_dict = list(set(all_actors) - {actor_first, actor_second})
    count_dict = {actor: all_actors.count(actor) for actor in
                  keys_for_count_dict}

    out_list = [key for key, value in count_dict.items() if value > 1]
    return out_list


def get_movie_by_query(type_movie: str, year: int, genre: str) -> list[dict]:
    """
    Задание №6
    :param type_movie:
    :param year:
    :param genre:
    :return:
    """
    query = f"""
        SELECT title, description
        FROM netflix
        WHERE upper(listed_in) like upper('%{genre}%')
        AND release_year = {year}
        AND type = '{type_movie}'
        """
    result = cursor_fetchall(DB_PATH, query)
    movie_list = [{'title': raw[0], 'description': raw[1]}
                  for raw in result]

    return movie_list


