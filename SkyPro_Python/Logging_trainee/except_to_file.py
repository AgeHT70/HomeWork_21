import logging

from flask import Flask, request, render_template
formatter_one = logging.Formatter("%(asctime)s : %(message)s")
# add filemode="w" to overwrite
logging.basicConfig(filename="basic.log", format="(asctime) : (message)")

# logging.setFormatter(formatter_one)
app = Flask(__name__)

@app.route('/',)
def page_index():
    return "Главная страница"

@app.route('/store')
def page_store():
    return "Страница магазина "

@app.route('/store/<cat>')
def page_cat(cat):
    return f"Страница категории {cat} "

app.run()