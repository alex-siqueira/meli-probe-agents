import datetime
import flask
from flask import request

app = flask.Flask(__name__)

@app.route('/', methods=['POST'])
def save():
  payload = request.get_json()

  now = datetime.datetime.now()

  filename = payload['localIP'] + "_" + str(now.year) + "-" + str(now.month) + "-" + str(now.day) + ".csv"


  f = open(filename, "w")
  f.write(payload['processor'] + "," + payload['osname'] + "," +  payload['version'] + "," + str(payload['sessions']) + "," + str(payload['processes']) )
  f.close()

  return "OK"

app.run()
