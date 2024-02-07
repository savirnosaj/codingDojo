from flask import Flask, render_template, request, redirect, session, flash # Import Flask to allow us to create our app.
# We imported the Flask module that is used to create our "app" variable. You will need this line in every application you build with Flask.
import re # the "re" module will let us perform some regular expression operations

# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
SPEC_CHAR = re.compile(r'[!@#$%^&*?<>(){}/|~:;,`[+]')

app = Flask(__name__)
# We used the flask module to create an "app" variable which represents our web application. We will be using this variable to attach routing rules for our application. You will need this line in every application you build with Flask.
# Global variable __name__ tells Flask whether or not we are running the file directly, or importing it as a module.

app.secret_key = 'ThisIsSecret' # when using flask (specifically session), it's mandatory to set a secret key for security purposes

# We set up a routing rule using the "@" symbol and running the app.route function. The @ symbol specifies that the function that follows this rule will be triggered any time that route is triggered. In this case, we are attaching the hello_world function to the '/' route.
@app.route("/")
# The "@" symbol designates a "decorator" which attaches the following function to the '/' route. This means that whenever we send a request to localhost:5000/ we will run the following "hello_world" function.
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    capCheck = False
    s_charCheck = False
    if len(request.form['email']) < 1:
        flash(u"Email Field Can't Be Empty", "error")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash(u'Invalid Email Address Entered', "error")
    else:
        session['email'] = request.form['email']

    if len(request.form['f_name']) < 1:
        flash(u"First Name Field Can't Be Empty", "error")
    elif str.isalpha(request.form['f_name']) == False:
        flash(u"Name Cannot Contain Numbers or Special Characters", "error")
    else:
        session['f_name'] = request.form['f_name']

    if len(request.form['l_name']) < 1:
        flash(u"Last Name Field Can't Be Empty", "error")
    elif str.isalpha(request.form['l_name']) == False:
        flash(u"Name Cannot Contain Numbers or Special Characters", "error")
    else:
        session['l_name'] = request.form['l_name']

    if len(request.form['tm_month']) < 1:
        flash('Please Select a Month', 'error')
    else:
        session['tm_month'] = request.form['tm_month']

    if len(request.form['tm_day']) < 1:
        flash('Please Select a Day', 'error')
    else:
        session['tm_day'] = request.form['tm_day']

    if len(request.form['tm_year']) < 1:
        flash('Please Select a Year', 'error')
    elif (2023 - int(request.form['tm_year'])) < 18:
        flash("You're Too Young to Create an Account", 'error')
    else:
        session['tm_year'] = request.form['tm_year']

    if len(request.form['password']) < 1:
        flash(u"Password Field Can't Be Empty", "error")
    elif len(request.form['password']) < 8:
        flash(u"Password Has to Be Greater or Equal to 8 Characters", "error")
    elif str.isnumeric(request.form['password']) == True:
        flash(u"Password Must Contain at Least One Number and Special Character", "error")
    elif str.isalpha(request.form['password']) == True:
        flash(u"Password Must Contain at Least One Number and Special Character", "error")
    else:
        for char in request.form['password']:
            if char.isupper():
                capCheck = True
            if SPEC_CHAR.search(char) == None:
                print("Still searching for a Spec. Char -- standby ..")
            else:
                print(f"Hit! Spec. Char: {char}")
                s_charCheck = True

        if capCheck == False:
            flash(u"Password Must Contain at Least One Number and Special Character and Captial Letter", "error")
        elif s_charCheck == False:
            flash("Password Must Have A Special Character", "error")

    if len(request.form['confirm_pass']) < 1:
        flash(u"Confirm Password Field Can't Be Empty", "error")
    elif request.form['confirm_pass'] != request.form['password']:
        flash(u"Passwords Did Not Match", "error")

    if '_flashes' in session.keys():
        return redirect("/")
    elif capCheck == True and s_charCheck == True:
        flash(u"Thank You for Your Information", "success")
        return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

# If __name__ is "__main__" we know we are running this file directly and not importing it from a different module
if __name__ == "__main__":
    app.run(debug=True)
    # You just created your first web server!
    # Finally, we ran the app! This takes all of our routing rules that we set up and actually starts up the server.Finally, we ran the app! This takes all of our routing rules that we set up and actually starts up the server.
