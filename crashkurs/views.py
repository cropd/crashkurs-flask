from crashkurs import app
from flask import render_template, request, json
from random import randint
    
@app.route('/')
def start():
    return render_template('start.html')

@app.route('/roll-dice/<number>', methods=['GET'])
def roll_dice(number):
	roll = [randint(1, 6)]
	i = 1
	while i < int(number):
		roll.append(randint(1, 6))
		i+=1	
	dices ={"dices": roll}
	return json.dumps(dices)