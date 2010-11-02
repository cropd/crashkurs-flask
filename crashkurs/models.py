from google.appengine.ext import db

class Dicerolls(db.Model):
	dice_roll = db.StringProperty(required=True)
	room = db.StringProperty()