from crashkurs import app
from flask import render_template, request, json
from random import randint
    
@app.route('/')
def start():
    return render_template('start.html')

@app.route('/roll-dice', methods=['GET'])
def roll_dice():
	dices ={"dices": [randint(1, 6),randint(1, 6)]}
	return json.dumps(dices)