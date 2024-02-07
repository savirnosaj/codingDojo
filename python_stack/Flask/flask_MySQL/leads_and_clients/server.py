from flask import Flask, render_template, request, redirect, session, flash # Import Flask to allow us to create our app.
# We imported the Flask module that is used to create our "app" variable. You will need this line in every application you build with Flask.
from mysqlconnection import connectToMySQL
# Import the function connectToMySQL from the file mysqlconnection.py
import itertools # iterate over multiple lists using zip function

app = Flask(__name__)
# We used the flask module to create an "app" variable which represents our web application. We will be using this variable to attach routing rules for our application. You will need this line in every application you build with Flask.
# Global variable __name__ tells Flask whether or not we are running the file directly, or importing it as a module.

# Invoke the connectToMySQL function and pass it the name of the database we're using
# ConnectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL("lead_gen_business")

app.secret_key = 'ThisIsSecret' # when using flask (specifically session), it's mandatory to set a secret key for security purposes

# We set up a routing rule using the "@" symbol and running the app.route function. The @ symbol specifies that the function that follows this rule will be triggered any time that route is triggered. In this case, we are attaching the hello_world function to the '/' route.
@app.route('/', methods=['GET'])
# The "@" symbol designates a "decorator" which attaches the following function to the '/' route. This means that whenever we send a request to localhost:5000/ we will run the following "hello_world" function.
def index():
    all_clients = mysql.query_db("SELECT * FROM clients")
    num_client_leads = [] # loop neccesary to determine amout of leads per client

    if 'updated_month' in session:
        for lead in all_clients:
            all_client_site_leads = mysql.query_db(f'SELECT * FROM leads LEFT JOIN sites ON leads.sites_id = sites.id LEFT JOIN clients ON sites.clients_id = clients.id WHERE clients.id = {lead["id"]} AND registered_datetime BETWEEN "2011-01-01 00:00:00" AND "{ session["updated_year"]}-{ session["updated_month"]}-30 23:59:59"')
            num_client_leads.append(len(all_client_site_leads))
    else:
        for lead in all_clients:
            all_client_site_leads = mysql.query_db(f"SELECT * FROM leads LEFT JOIN sites ON leads.sites_id = sites.id LEFT JOIN clients ON sites.clients_id = clients.id WHERE clients.id = {lead['id']}")
            num_client_leads.append(len(all_client_site_leads))


    client_lead_data = zip(all_clients, num_client_leads)
    data_list = list(client_lead_data) # since a zip object isn't subscriptable, I need to convert to list to query info in combined array/dict ()

    return render_template('index.html', client_lead_data = zip(all_clients, num_client_leads), client_info = data_list)

@app.route('/update_time', methods=['POST'])
def update_query():

    session['updated_month'] = request.form['tm_month']
    if session['updated_month'] == '01':
        session['chart_month'] = 'January'
    elif session['updated_month'] == '02':
        session['chart_month'] = 'February'
    elif session['updated_month'] == '03':
        session['chart_month'] = 'March'
    elif session['updated_month'] == '04':
        session['chart_month'] = 'April'
    elif session['updated_month'] == '05':
        session['chart_month'] = 'May'
    elif session['updated_month'] == '06':
        session['chart_month'] = 'June'
    elif session['updated_month'] == '07':
        session['chart_month'] = 'July'
    elif session['updated_month'] == '08':
        session['chart_month'] = 'August'
    elif session['updated_month'] == '09':
        session['chart_month'] = 'September'
    elif session['updated_month'] == '10':
        session['chart_month'] = 'October'
    elif session['updated_month'] == '11':
        session['chart_month'] = 'November'
    elif session['updated_month'] == '12':
        session['chart_month'] = 'December'
    
    session['updated_year'] = request.form['tm_year']

    return redirect('/')

@app.route('/reset') # used to clear session
def reset():
    session.clear()
    return redirect('/')    

# If __name__ is "__main__" we know we are running this file directly and not importing it from a different module
if __name__ == "__main__":
    app.run(debug=True)
    # You just created your first web server!
    # Finally, we ran the app! This takes all of our routing rules that we set up and actually starts up the server.Finally, we ran the app! This takes all of our routing rules that we set up and actually starts up the server.
