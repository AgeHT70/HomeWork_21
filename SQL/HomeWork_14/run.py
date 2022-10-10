from flask import Flask, jsonify

from functions import get_movie_by_title, get_movie_by_year, \
    get_movie_by_rating, get_movie_by_genre

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/movie/<title>')
def movie_by_title_page(title):
    result = get_movie_by_title(title)
    return jsonify(result)


@app.route('/movie/<int:year_from>/to/<int:year_to>')
def movie_by_year_page(year_from, year_to):
    result = get_movie_by_year(year_from, year_to)
    return jsonify(result)


@app.route('/rating/children') #(включаем сюда рейтинг G)
def children_page():
    result = get_movie_by_rating('G')
    return jsonify(result)


@app.route('/rating/family')   #(G, PG, PG-13)
def family_page():
    result = get_movie_by_rating(('G', 'PG', 'PG-13'))
    return jsonify(result)


@app.route('/rating/adult')    #(R, NC-17)
def adult_page():
    result = get_movie_by_rating(('R', 'NC-17'))
    return jsonify(result)


@app.route('/genre/<genre>')
def genre_page(genre):
    result = get_movie_by_genre(genre)
    return jsonify(result)


if __name__ == '__main__':
    app.run()
