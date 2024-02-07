from flask import Flask, render_template, request, redirect, session # Import Flask to allow us to create our app.
# We imported the Flask module that is used to create our "app" variable. You will need this line in every application you build with Flask.
import random

app = Flask(__name__)
# We used the flask module to create an "app" variable which represents our web application. We will be using this variable to attach routing rules for our application. You will need this line in every application you build with Flask.
# Global variable __name__ tells Flask whether or not we are running the file directly, or importing it as a module.

app.secret_key = 'ThisIsSecret' # Set a secret key for security purposes

# variables:
varRand = random.randrange(1, 101)

# We set up a routing rule using the "@" symbol and running the app.route function. The @ symbol specifies that the function that follows this rule will be triggered any time that route is triggered. In this case, we are attaching the hello_world function to the '/' route.
@app.route("/")
# The "@" symbol designates a "decorator" which attaches the following function to the '/' route. This means that whenever we send a request to localhost:5000/ we will run the following "hello_world" function.
def index():
    #session['status'] = False
    if 'won' in session:
        varRand = random.randrange(1, 101)
        session['rand'] = varRand
        session.pop('won')
        return render_template("index.html", rand = session['rand'])
    else:
        print(f"\nCurrent Session: {session}\n")
        return render_template("index.html", rand = session['rand'])

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    session['status'] = False
    session['active'] = True
    if(session['guess'] == session['rand']):
        print(f"\nYou Guessed the Right Number! Congratulations!...\n")
        session['status'] = True
        return render_template('index.html', status = session['status'])
    else:
        print('\nWrong Answer! - Please Try Again ...\n')
        return redirect('/')

@app.route('/restart')
def restart():
    session.clear()
    session['status'] = False
    session['won'] = True
    return redirect('/')

# If __name__ is "__main__" we know we are running this file directly and not importing it from a different module
if __name__ == "__main__":
    app.run(debug=True)
    # You just created your first web server!
    # Finally, we ran the app! This takes all of our routing rules that we set up and actually starts up the server.Finally, we ran the app! This takes all of our routing rules that we set up and actually starts up the server.
