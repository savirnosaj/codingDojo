from flask import Flask, render_template, request, redirect # Import Flask to allow us to create our app.
# We imported the Flask module that is used to create our "app" variable. You will need this line in every application you build with Flask.
from datetime import datetime # using datetime module

app = Flask(__name__)
# We used the flask module to create an "app" variable which represents our web application. We will be using this variable to attach routing rules for our application. You will need this line in every application you build with Flask.
# Global variable __name__ tells Flask whether or not we are running the file directly, or importing it as a module.

# We set up a routing rule using the "@" symbol and running the app.route function. The @ symbol specifies that the function that follows this rule will be triggered any time that route is triggered. In this case, we are attaching the hello_world function to the '/' route.
@app.route("/")
# The "@" symbol designates a "decorator" which attaches the following function to the '/' route. This means that whenever we send a request to localhost:5000/ we will run the following "hello_world" function.
def index():
    return render_template("index.html")

# We define the route below such that the route matches the action of our form - '/users'
# Similarly we need to allow specific methods - 'POST' in this case
@app.route('/checkout', methods=['POST'])
def place_order():
    print('Got Post Info')
    # We can access form data with this syntax:
    strawberry = request.form['strawberry']
    raspberry = request.form['raspberry']
    apple = request.form['apple']
    name = request.form['name']
    student_id = request.form['student_id']
    total_items = (int(strawberry) + int(raspberry) + int(apple))
    date_charged = datetime.now()
    # Recall the name attributes we added to our form inputs to access the data that the user input into the fields we use request.form['name_of_input']
    #print(f"\n{request.form}")
    return render_template('order_confirmation.html', total_items = total_items, date_charged = date_charged)

# If __name__ is "__main__" we know we are running this file directly and not importing it from a different module
if __name__ == "__main__":
    app.run(debug=True)
    # You just created your first web server!
    # Finally, we ran the app! This takes all of our routing rules that we set up and actually starts up the server.Finally, we ran the app! This takes all of our routing rules that we set up and actually starts up the server.
