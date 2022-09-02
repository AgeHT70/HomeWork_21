from flask import Flask
from utils import load_candidates, get_all, get_by_pk, get_by_skill

app = Flask(__name__)

FILENAME = "candidates.json"
IMG_URL = "https://s5.vcdn.biz/static/f/919223231/image.jpg"


@app.route("/")
def page_index():
    out_str = get_all(load_candidates(FILENAME))
    return f"<pre>{out_str}</pre>"


@app.route("/candidates/<int:pk>")
def page_candidate(pk):
    out_str = get_by_pk(load_candidates(FILENAME), pk)
    return f"<img src='{IMG_URL}'>\
    <pre>{out_str}</pre>"


@app.route("/skills/<skill>")
def page_skills(skill):
    out_str = get_by_skill(load_candidates(FILENAME), skill)
    return f"<pre>{out_str}</pre>"


app.run()
