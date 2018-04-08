from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def user():
    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form["comment"]

    return landing(name, location, language, comment)

@app.route("/landing")
def landing(name, location, language, comment):
    return render_template("landing.html", name=name, location=location, language=language, comment=comment)

app.run(debug=True)

