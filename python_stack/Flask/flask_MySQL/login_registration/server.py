from flask import Flask, render_template, request, redirect, session, flash # Import Flask to allow us to create our app.
# We imported the Flask module that is used to create our "app" variable. You will need this line in every application you build with Flask.
from mysqlconnection import connectToMySQL
# Import the function connectToMySQL from the file mysqlconnection.py
from flask_bcrypt import Bcrypt
import re # The "re" module will let us perform some regular expression operations

# Create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
SPEC_CHAR = re.compile(r'[!@#$%^&*?<>(){}/|~:;,`[+]')

app = Flask(__name__)
# We used the flask module to create an "app" variable which represents our web application. We will be using this variable to attach routing rules for our application. You will need this line in every application you build with Flask.
# Global variable __name__ tells Flask whether or not we are running the file directly, or importing it as a module.
bcrypt = Bcrypt(app)
# We are creating an object called bcrypt, which is made by invoking the function Bcrypt with our app as an argument

# Invoke the connectToMySQL function and pass it the name of the database we're using
# ConnectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL("loginREG")

app.secret_key = 'ThisIsSecret' # when using flask (specifically 'Session'), it's mandatory to set a secret key for security purposes

# We set up a routing rule using the "@" symbol and running the app.route function. The @ symbol specifies that the function that follows this rule will be triggered any time that route is triggered. In this case, we are attaching the hello_world function to the '/' route.
@app.route('/')
# The "@" symbol designates a "decorator" which attaches the following function to the '/' route. This means that whenever we send a request to localhost:5000/ we will run the following "hello_world" function.
def index():
    if 'userid' in session:
        return redirect('/success')
    else:
        return render_template('index.html')

@app.route('/register_user', methods=['POST'])
def registerNewUser():
    print('\nRegister-User Form Submission .. Processing - Standby ..\n')
    # Variables
    passUpper = False
    passSpecChar = False
    passNum = False

    if len(request.form['fName']) < 1:
        flash(u"First Name Field Can't Be Empty", 'error')
    elif len(request.form['fName']) < 2:
        flash(u'First Name Must Be at Least 2 Characters Long', 'error')
    elif str.isalpha(request.form['fName']) == False:
        flash(u"First Name Can't Contain Numbers", 'error')
    else:
        session['reg_fName'] = str.capitalize(request.form['fName'])
    
    if len(request.form['lName']) < 1:
        flash(u"Last Name Field Can't Be Empty", 'error')
    elif len(request.form['lName']) < 2:
        flash(u'Last Name Must Be at Least 2 Characters Long', 'error')
    elif str.isalpha(request.form['lName']) == False:
        flash(u"Last Name Can't Contain Numbers", 'error')
    else:
        session['reg_lName'] = str.capitalize(request.form['lName'])

    if len(request.form['email']) < 1:
        flash(u"Email Field Can't Be Empty", 'error')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash(u'Invalid Email Address Entered', 'error')
    else:
        session['reg_email'] = request.form['email']

    if len(request.form['passwd']) < 1:
        flash(u"Password Field Can't Be Empty", 'error')
    elif len(request.form['passwd']) < 8:
        flash(u'Password Must Be at Least 8 Characters', 'error')
    elif str.isalpha(request.form['passwd']) == True:
        flash(u'Password Must Contain at Least One Number', 'error')
    elif str.isnumeric(request.form['passwd']) == True:
        flash(u'Password Must Contain at Least One Letter', 'error')
    else:
        for char in request.form['passwd']:
            if char.isupper():
                passUpper = True
                print(f'\nHIT! Upper Char: {char}\n')
            
            if char.isnumeric():
                passNum = True

            if SPEC_CHAR.search(char) == None:
                print(f'{char}: No Special Char -- Still Searching ..')
            else:
                print(f'\nHIT! Special Char:{char}\n')
                passSpecChar = True

        if passUpper == False:
            flash('Password Must Contain at Least One Uppercase Letter', 'error')
        if passSpecChar == False:
            flash('Password Must Contain at Least One Special Character', 'error')
        if passNum == False:
            flash('Password Must Contain at Least One Number/Special Character', 'error')

    if len(request.form['confirm_Pass']) < 1:
        flash("Confirm Password Field Can't Be Empty", 'error')
    elif request.form['passwd'] != request.form['confirm_Pass']:
        flash("Passwords Didn't Match", 'error')

    if '_flashes' in session.keys():
        return redirect("/")
    elif passUpper == True and passSpecChar == True and passNum == True:
        pw_hash = bcrypt.generate_password_hash(request.form['passwd'])
        # print(f'\nHashed Password: {pw_hash}\n')
        query = 'INSERT INTO `loginREG`.`users` (first_name, last_name, email, hashed_password) VALUES (%(firstName)s, %(lastName)s, %(email)s, %(password_hash)s);'

        data = {
            'firstName' : str.capitalize(request.form['fName']),
            'lastName' : str.capitalize(request.form['lName']),
            'email' : request.form['email'],
            'password_hash' : pw_hash
        }

        locateId_query = mysql.query_db(f'SELECT * FROM `loginREG`.`users` WHERE email = "{ request.form["email"] }";')

        if locateId_query:
            flash('This Email Is Already Registered', 'error')
            return redirect('/')
        else:
            mysql.query_db(query, data)
            flash(u'You Have Successfully Registered', 'success')

            locateId_query = mysql.query_db(f'SELECT * FROM `loginREG`.`users` WHERE email = "{ request.form["email"] }";')
            print(locateId_query[0]['id'])
            session['userid'] =  locateId_query[0]['id'] # Keep Track of User Login Status

            print('\nRegistration Successful - Redirecting ..\n')
            return redirect('/next_steps')

@app.route('/login_user', methods=['POST'])
def loginUser():
    print('\nLogin Form Submission .. Processing - Standby ..\n')

    # See if the email provided exists in the database
    query = 'SELECT * FROM `loginREG`.`users` WHERE email = %(email)s;'
    data = { 'email' : request.form['email'] }
    result = mysql.query_db(query, data)

    if len(request.form['email']) < 1:
        flash('Enter Email Address', 'error')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash(u'Invalid Email Address', 'error')
    else:
        session['log_email'] = request.form['email']
    
    if len(request.form['passwd']) < 1:
        flash('Enter Password', 'error')

    if result:
        if bcrypt.check_password_hash(result[0]['hashed_password'], request.form['passwd']):
            session['userid'] = result[0]['id'] # Keep track of User Login Status
            session['log_fName'] = result[0]['first_name']
        else:
            flash('You Entered The Wrong Password', 'error')
    else:
        flash('This Email Does Not Exists', 'error')

    if '_flashes' in session.keys():
        flash("You Could Not Be Logged In", 'error')
        return redirect("/")
    else:
        flash('You Have Successfully Logged In', 'success')
        print('Login Successful - Redirecting ..\n')
        return redirect('/success')

@app.route('/success')
def logReg_success():
    return render_template('success.html')
    
@app.route('/next_steps')
def nextSteps():
    return render_template('next_steps.html')

@app.route('/userInfo', methods=['POST'])
def insertInfo():
    if (2023 - int(request.form['bd-year'])) < 18:
        flash("You're Too Young To Create A Profile", 'error')

    checkBox = request.form.getlist('favLang')

    if not checkBox:
        flash('You Need To Choose At Least One of Your Favorite Languages', 'error')

    if not request.form.get('gender'):
        flash('You Must Choose A Gender', 'error')
    
    
    if '_flashes' in session.keys():
        return redirect("/next_steps")
    else:
        for entry in checkBox:
            mysql.query_db(f'INSERT INTO `loginREG`.`favorite_language` (`favorite_language`, `users_id`) VALUES ("{entry}", "{session["userid"]}");')
            # print(f'\nFav: {entry}\n')
        
        mysql.query_db(f'UPDATE `loginREG`.`users` SET birthday = "{request.form["bd-year"]}-{request.form["bd-month"]}-{request.form["bd-day"]}", gender = "{request.form["gender"]}" WHERE id = {session["userid"]};')
        flash('Thank You for Updating Your Profile', 'success')
        return redirect('/success')


@app.route('/logout_user') # used to clear Session
def logoutUser():
    print('\nUser Requested to Logout - Initializing .. Standby ..')
    session.clear()
    print('Session Cleared .. Done\n')
    return redirect('/')

# If __name__ is "__main__" we know we are running this file directly and not importing it from a different module
if __name__ == "__main__":
    app.run(debug=True)
    # You just created your first web server!
    # Finally, we ran the app! This takes all of our routing rules that we set up and actually starts up the server.Finally, we ran the app! This takes all of our routing rules that we set up and actually starts up the server.
