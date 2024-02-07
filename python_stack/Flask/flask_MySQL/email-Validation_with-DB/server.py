from flask import Flask, render_template, request, redirect, session, flash # Import Flask to allow us to create our app.
# We imported the Flask module that is used to create our "app" variable. You will need this line in every application you build with Flask.
from mysqlconnection import connectToMySQL
# Import the function connectToMySQL from the file mysqlconnection.py
import re # The "re" module will let us perform some regular expression operations

# Create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
# We used the flask module to create an "app" variable which represents our web application. We will be using this variable to attach routing rules for our application. You will need this line in every application you build with Flask.
# Global variable __name__ tells Flask whether or not we are running the file directly, or importing it as a module.

# Invoke the connectToMySQL function and pass it the name of the database we're using
# ConnectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL("social_media")

app.secret_key = 'ThisIsSecret' # when using flask (specifically 'Session'), it's mandatory to set a secret key for security purposes

# We set up a routing rule using the "@" symbol and running the app.route function. The @ symbol specifies that the function that follows this rule will be triggered any time that route is triggered. In this case, we are attaching the hello_world function to the '/' route.
@app.route('/')
# The "@" symbol designates a "decorator" which attaches the following function to the '/' route. This means that whenever we send a request to localhost:5000/ we will run the following "hello_world" function.
def index():
    return render_template('index.html')

@app.route('/add_user', methods=['POST'])
def addUser():
    if len(request.form['email']) < 1:
        flash("Email Field Can't Be Empty", 'error')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash(u'Invalid Email Address Entered', 'error')
    else:
        mysql.query_db(f'INSERT INTO `social_media`.`users` (email, created_at) VALUES ("{ request.form["email"] }", now())')
        print('Success! The User was added to the database ...')
        flash(f'The Email Address You Entered ({ request.form["email"] }) is a Valid Email! Thank You!', 'success')
        return redirect('/success')

    return redirect('/')

@app.route('/success')
def showAllUsers():
    all_users = mysql.query_db('SELECT * FROM users')
    return render_template('success.html', users = all_users)

@app.route('/delete', methods=['POST'])
def deleteUser():
    print(request.form['userID'])
    mysql.query_db(f'DELETE FROM `social_media`.`users` WHERE id = { request.form["userID"]}')
    flash(f'You Have Successfully Deleted ({ request.form["userEMAIL"] })', 'success')
    return redirect('/success')

@app.route('/reset') # used to clear Session
def reset():
    session.clear()
    return redirect('/')

# If __name__ is "__main__" we know we are running this file directly and not importing it from a different module
if __name__ == "__main__":
    app.run(debug=True)
    # You just created your first web server!
    # Finally, we ran the app! This takes all of our routing rules that we set up and actually starts up the server.Finally, we ran the app! This takes all of our routing rules that we set up and actually starts up the server.
