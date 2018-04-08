from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja')
def ninja():
    return render_template("ninja.html")

@app.route('/ninja/<color>')
def color(color):
    if color == "blue":
        turtle = "leonardo"
    elif color == "orange":
        turtle = "michelangelo"
    elif color == "red":
        turtle = "raphael"
    elif color == "purple":
        turtle = "donatello"
    else:
        turtle = "notapril"
    return render_template("turtle.html", turtle=turtle)

app.run(debug=True)
