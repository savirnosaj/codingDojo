from flask import Flask, render_template, request, redirect, session, flash # Import Flask to allow us to create our app.
# We imported the Flask module that is used to create our "app" variable. You will need this line in every application you build with Flask.
import re # the "re" module will let us perform some regular expression operations

# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
# We used the flask module to create an "app" variable which represents our web application. We will be using this variable to attach routing rules for our application. You will need this line in every application you build with Flask.
# Global variable __name__ tells Flask whether or not we are running the file directly, or importing it as a module.

app.secret_key = 'ThisIsSecret' # when using flask, it's mandatory to set a secret key for security purposes

# We set up a routing rule using the "@" symbol and running the app.route function. The @ symbol specifies that the function that follows this rule will be triggered any time that route is triggered. In this case, we are attaching the hello_world function to the '/' route.
@app.route("/")
# The "@" symbol designates a "decorator" which attaches the following function to the '/' route. This means that whenever we send a request to localhost:5000/ we will run the following "hello_world" function.
def index():
    return render_template("index.html")

@app.route('/result')
def success():
    return render_template('confirmation.html')

@app.route('/process', methods=['POST'])
def submit():

    if(len(request.form['survey_name']) < 1):
        flash("Name field can't be empty")
    else:
        session['name'] = request.form['survey_name']
    
    if(len(request.form['survey_location']) < 1):
        flash("Location field can't be empty")
    else:
        session['location'] = request.form['survey_location']

    if(len(request.form['survey_language']) < 1):
        flash("Language field can't be empty")
    else:
        session['language'] = request.form['survey_language']

    if(len(request.form['survey_comment']) < 1):
        flash("Comment field can't be empty")
    elif(len(request.form['survey_comment']) > 120):
        flash("Comment field can't have more than 120 characters")
        session['comment'] = request.form['survey_comment']
    else:
        session['comment'] = request.form['survey_comment']

    if('_flashes' in session.keys()):
        return redirect('/')
    else:
        return redirect('/result')
    
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

# If __name__ is "__main__" we know we are running this file directly and not importing it from a different module
if __name__ == "__main__":
    app.run(debug=True)
    # You just created your first web server!
    # Finally, we ran the app! This takes all of our routing rules that we set up and actually starts up the server.Finally, we ran the app! This takes all of our routing rules that we set up and actually starts up the server.
