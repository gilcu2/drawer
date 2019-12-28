import flask
from subprocess import Popen
import drawer
import json
import sys

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    data=json.dumps(drawer.generateCircles(),default=drawer.obj_dict)
    env={}
    env["DRAWER_INPUT"]=data
    Popen([sys.executable,"drawer.py"],env=env)
    return data

app.run()