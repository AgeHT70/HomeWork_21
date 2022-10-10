import json
import sqlite3
from itertools import count
from pprint import pprint
from typing import Dict, Any

from flask import jsonify

DB_PATH = 'netflix.db'


def cursor_fetchall(db_path, query):
    with sqlite3.connect(db_path) as con:
        cursor = con.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result


def get_movie_by_title(title: str) -> list[dict]:
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


def count_actors(actor_first, actor_second):
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


def get_movie_by_query(type_movie, year, genre):
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


