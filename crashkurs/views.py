from crashkurs import app
from flask import render_template, request, json
from models import Dicerolls
from random import randint
    
@app.route('/')
def start():
    return render_template('list_rooms.html')
    
@app.route('/roll-dice/<room>')
def show_room(room):
	dicerolls = Dicerolls.all()
	return render_template('room.html', dicerolls=dicerolls, room=room)

@app.route('/roll-dice/<room>/<number>', methods=['GET'])
def roll_dice(room, number):
	roll = [randint(1, 6)]
	i = 1
	while i < int(number):
		roll.append(randint(1, 6))
		i+=1	
	dice ={"dice": roll}
	dicerolls = Dicerolls(dice_roll = str(dice), room = room)
	dicerolls.put()
	return json.dumps(dice)
	
