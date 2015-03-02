from energenie import switch_on, switch_off
from time import sleep
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/lightson")
def lights_on():
    i = int(request.args.get('l', '1'))
    switch_on(i)
    return "On"

@app.route("/lightsoff")
def lights_off():
    i = int(request.args.get('l', '1'))
    switch_off(i)
    return "Off"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

