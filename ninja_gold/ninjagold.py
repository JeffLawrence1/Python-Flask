from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
from random import randint
from datetime import datetime

app.secret_key = 'ThisIsSecret' 

@app.route('/')
def index():
    if "gold" not in session.keys():
        session["gold"] = 0
    if "activities" not in session.keys():
        session["activities"] = ""
    return render_template("index.html", gold= session["gold"], activities= session["activities"])

@app.route('/process_money', methods=['POST'])
def money():
    time = datetime.now().strftime("%H:%M %p, %B %d, %Y")
    location = request.form["building"]
    gold = {
        "farm": randint(2, 15),
        "cave": randint(5, 25),
        "house": randint(3, 18),
        "casino": randint(-25, 25),
    }
    activities = "You went to the " + location + " and "

    if gold[location] >= 0:
        activities += "found "
    else:
        activities += "lost "
    activities += str(gold[location]) + " Gold " + time + "<br>"
    session["activities"] += activities
    session["gold"] += gold[location]
    return redirect('/')

@app.route("/reset", methods =['POST'])
def reset():
    session.clear()
    return redirect("/")

app.run(debug=True)
