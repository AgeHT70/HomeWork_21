from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def form_page():
    return render_template('form.html')


@app.route('/in')
def form_index_page():
    return render_template('index.html')


@app.route('/search')
def search_page():
    s = request.args['s']
    return f'Вы ввели слово {s}'


@app.route('/add', methods=["POST"])
def add_page():
    task = request.form['task_name']
    return f'Вы добавили задачу {task}'


app.run()
