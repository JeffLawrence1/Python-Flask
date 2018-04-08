from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():
    
    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form["comment"]

    if len(request.form['name']) < 1:
        flash("name must be longer than 1 char")
        return redirect('/')
    elif len(request.form['comment']) < 1:
        flash("comments can't be blank")
        return redirect('/')
    elif len(request.form['comment']) > 120:
        flash("comments can't be longer than 120 chars")
        return redirect('/')
    else:
        flash("Success!")

    
    return render_template("result.html", name=name, location=location, language=language, comment=comment)
app.run(debug=True)