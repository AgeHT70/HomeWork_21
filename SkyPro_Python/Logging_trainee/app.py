import logging
from flask import Flask

app = Flask(__name__)


@app.route('/', )
def page_index():
    print("Главная страница запрошена")
    return "Главная страница"


@app.route('/store')
def page_store():
    print("Страница магазина запрошена")
    return "Страница магазина "


@app.route('/store/<cat>')
def page_cat(cat):
    print(f"Страница категории {cat} запрошена")
    return f"Страница категории {cat} "


#app.run()

logger_one = logging.getLogger("one")
logger_two = logging.getLogger("two")

logger_one.warning("Логгер первый работает")
logger_two.warning("Логгер второй работает")

new_logger = logging.getLogger()

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("log.txt")

new_logger.addHandler(console_handler)
new_logger.addHandler(file_handler)

new_logger.warning("Все работает")

logger_one = logging.getLogger("one")
logger_two = logging.getLogger("two")

file_handler_one = logging.FileHandler("log_one.txt")
file_handler_two = logging.FileHandler("log_two.txt")

logger_one.addHandler(file_handler_one)
logger_two.addHandler(file_handler_two)

logger_one.warning("Запись для логгера один")
logger_two.warning("Запись для логгера два")