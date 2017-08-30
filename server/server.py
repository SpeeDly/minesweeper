import json

from flask import render_template
from flask import Flask, request, abort

app = Flask(__name__, static_url_path='/static')

STATUS = {
    -1: 'Defeated',
    0: 'In Progress',
    1: 'Completed'
}
GAMES = {}


@app.route("/")
def home():
    games = []
    for k, v in GAMES.items():
        status = STATUS[v['status']]
        games.append({'id': k, 'status': status})
    return render_template('index.html', games=games)


@app.route('/update/<int:game_id>', methods=['POST'])
def update(game_id):
    if request.method == 'POST':
        GAMES[game_id] = request.json
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/create/<int:game_id>', methods=['POST'])
def create(game_id):
    if request.method == 'POST':
        GAMES[game_id] = request.json
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/state/<int:game_id>', methods=['GET'])
def state(game_id):
    game = GAMES.get(game_id)
    if not game:
        abort(404)
    return json.dumps(game), 200, {'ContentType': 'application/json'}


@app.route('/game/<int:game_id>', methods=['GET'])
def game(game_id):
    game = GAMES.get(game_id)
    if not game:
        abort(404)
    return render_template('game.html', game_id=game_id)


@app.route('/finish/<int:game_id>', methods=['POST'])
def finish(game_id):
    if request.method == 'POST':
        GAMES[game_id]['status'] = request.json['status']
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
