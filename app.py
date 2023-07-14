from flask import Flask, render_template, request, redirect
from util import Predictor
import random

app = Flask(__name__)

INITIAL_GAME_CHOICE = 0
MIN_ALLOWED_LENGTH = 30
DATA = {
    'baccarat': {
        'datatype': 'shoe',
        'symbols': ['banker', 'player', 'tie']
    },
    'roulette': {
        'datatype': 'spin chart',
        'symbols': ['red', 'black', 'zero']
    },
    'andar_bahar': {
        'datatype': 'gameplay chart',
        'symbols': ['andar', 'bahar']
    },
    'binary_options': {
        'datatype': 'stock chart',
        'symbols': ['higher', 'lower']
    },
}


def stylize_string(keys):
    return [' '.join(k.split("_")).title() for k in keys]


@app.route("/")
def index():
    games = stylize_string(DATA.keys())
    selected_game = list(DATA.keys())[INITIAL_GAME_CHOICE]

    return render_template("form.html", games=games, selected_game=selected_game)


@app.route("/generate", methods=["GET", "POST"])
def generate():

    if request.method == "POST":

        game = request.form.get("game")
        game_data = list(
            map(lambda x: int(x), list(request.form.get("game_data"))))

        if len(game_data) == 0:
            return render_template("error.html")

        P = Predictor(minimum_bet=1, bet_format=0, switch_number=1, game_symbols=list(map(
            lambda x: x[0], list(DATA[game]['symbols']))))
        D = P.run(testing_shoe=game_data)

        print(D)

    return redirect("/")
