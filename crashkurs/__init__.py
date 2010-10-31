from flask import Flask
import settings

app = Flask('crashkurs')
app.config.from_object('crashkurs.settings')

import views