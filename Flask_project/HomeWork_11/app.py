from flask import Flask, render_template

from utils import load_candidates, get_by_id, get_by_name, get_by_skill

FILENAME = 'candidates.json'
app = Flask(__name__)


@app.route('/')
def page_index():
    candidates = load_candidates(FILENAME)
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:uid>')
def page_by_uid(uid):
    data = load_candidates(FILENAME)
    candidate = get_by_id(data, uid=uid)
    return render_template('single.html', candidate=candidate)


@app.route('/search/<name>')
def page_by_name(name):
    data = load_candidates(FILENAME)
    candidates = get_by_name(data, name=name)
    candidates_len = len(candidates)
    return render_template('search.html', candidates=candidates, candidates_len=candidates_len)


@app.route('/skill/<skill_name>')
def page_by_skill(skill_name):
    data = load_candidates(FILENAME)
    candidates = get_by_skill(data, skill_name=skill_name)
    candidates_len = len(candidates)
    return render_template('search.html', candidates=candidates, candidates_len=candidates_len)


@app.route('/part_1/')
def page_part_1():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8001, debug=True)
