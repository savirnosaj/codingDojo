from flask import Flask # Import Flask to allow us to create our app.
# We imported the Flask module that is used to create our "app" variable. You will need this line in every application you build with Flask.

app = Flask(__name__)
# We used the flask module to create an "app" variable which represents our web application. We will be using this variable to attach routing rules for our application. You will need this line in every application you build with Flask.
# Global variable __name__ tells Flask whether or not we are running the file directly, or importing it as a module.

# We set up a routing rule using the "@" symbol and running the app.route function. The @ symbol specifies that the function that follows this rule will be triggered any time that route is triggered. In this case, we are attaching the hello_world function to the '/' route.
@app.route("/")
# The "@" symbol designates a "decorator" which attaches the following function to the '/' route. This means that whenever we send a request to localhost:5000/ we will run the following "hello_world" function.
def index():
    return "Hello World"

@app.route("/success")
def success():
    return "Success"

@app.route("/hello/<name>")
def hello(name):
    print(name)
    return "hello " + name

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

# If __name__ is "__main__" we know we are running this file directly and not importing it from a different module
if __name__ == "__main__":
    app.run(debug=True)
    # You just created your first web server!
    # Finally, we ran the app! This takes all of our routing rules that we set up and actually starts up the server.Finally, we ran the app! This takes all of our routing rules that we set up and actually starts up the server.
