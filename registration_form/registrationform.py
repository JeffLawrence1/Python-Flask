# import Flask
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
    
    if len(request.form['email']) < 1:
        flash("input Email!")
    # else if email doesn't match regular expression display an "invalid email address" message
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    elif len(request.form['first_name']) < 1:
        flash("name must have more than 1 char")
    elif not request.form['first_name'].isalpha():
        flash("name must have letters")
    elif len(request.form['last_name']) < 1:
        flash("name must have more than 1 char")
    elif not request.form['last_name'].isalpha():
        flash("name must have letters")
    elif len(request.form['password']) < 8:
        flash("must input password that is 8 chars or longer")
    elif len(request.form['confirm']) < 8:
        flash("must confirm password")
    elif request.form['password'] != request.form['confirm']:
        flash("passwords must match!")
    else:
        flash("Success!")
    return redirect('/')
app.run(debug=True)