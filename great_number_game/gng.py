from flask import Flask, render_template, request, redirect, session
from random import randint

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def index(message ="", newGame = False):
    if newGame is True or len(session) < 2:
        session['rando'] = randint(1, 100)

    if newGame is False:
        button = "Submit"
        hide = ""
    else:
        button = "New Game"
        hide = "hidden"
    return render_template("index.html", hide=hide, message=message, button=button)

@app.route("/guess", methods=["POST"])
def guess():
    if len(request.form["guess"]) > 0:
        session['guess'] = int(request.form['number'])
        if session['guess'] < session['rando']:
            return index("Too low")
        if session['guess'] > session['rando']:
            return index("Too high")
        else:
            return index("Good guess!", True)
    else:
        return index("make a valid guess")


app.run(debug=True)