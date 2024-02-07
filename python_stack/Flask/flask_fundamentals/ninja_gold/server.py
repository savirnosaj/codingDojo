from flask import Flask, render_template, request, redirect, session # Import Flask to allow us to create our app.
# We imported the Flask module that is used to create our "app" variable. You will need this line in every application you build with Flask.
import random
from datetime import datetime

app = Flask(__name__)
# We used the flask module to create an "app" variable which represents our web application. We will be using this variable to attach routing rules for our application. You will need this line in every application you build with Flask.
# Global variable __name__ tells Flask whether or not we are running the file directly, or importing it as a module.

app.secret_key = 'ThisIsSecret' # when using flask, it's mandatory to set a secret key for security purposes
# Variables:
total_gold = 0
message = ""

# We set up a routing rule using the "@" symbol and running the app.route function. The @ symbol specifies that the function that follows this rule will be triggered any time that route is triggered. In this case, we are attaching the hello_world function to the '/' route.
@app.route("/")
# The "@" symbol designates a "decorator" which attaches the following function to the '/' route. This means that whenever we send a request to localhost:5000/ we will run the following "hello_world" function.
def index():
    message = session['message']
    return render_template("index.html", message = session['message'])

@app.route('/process_money', methods=['POST'])
def process_money():
    total_gold = session['gold']
    session['gold'] = total_gold

    message = session['message']
    session['message'] = message

    date = datetime.now()

    if(request.form['building'] == 'farm'):
        print(f"\nSearching for Gold in the Old ({request.form['building']}):")
        print(f"Current Total of Gold: {total_gold}")

        farm_gold = random.randrange(10, 21)
        print(f"\nYou Found {farm_gold} Gold in the ({request.form['building']})")

        message += f"<p class='font-grn'>Earned {farm_gold} Gold from the Old ({request.form['building']}) | ({date})</p>"
        session['message'] = message

        total_gold += farm_gold
        session['gold'] = total_gold
        print(f"Total Gold: {session['gold']}\n")

    elif(request.form['building'] == 'cave'):
        print(f"\nSearching for Gold in the Ancient ({request.form['building']}):")
        print(f"Current Total of Gold: {total_gold}")

        cave_gold = random.randrange(5, 11)
        print(f"\nYou Found {cave_gold} Gold in the ({request.form['building']})")

        message += f"<p class='font-grn'>Earned {cave_gold} Gold from the Ancient ({request.form['building']}) | ({date})</p>"
        session['message'] = message

        total_gold += cave_gold
        session['gold'] = total_gold
        print(f"Total Gold: {session['gold']}\n")

    elif(request.form['building'] == 'house'):
        print(f"\nSearching for Gold in the Haunted ({request.form['building']}):")
        print(f"Current Total of Gold: {total_gold}")

        house_gold = random.randrange(2, 6)
        print(f"\nYou Found {house_gold} Gold in the ({request.form['building']})")

        message += f"<p class='font-grn'>Earned {house_gold} Gold from the Haunted ({request.form['building']}) | ({date})</p>"
        session['message'] = message
        
        total_gold += house_gold
        session['gold'] = total_gold
        print(f"Total Gold: {session['gold']}\n")

    elif(request.form['building'] == 'casino'):
        if(total_gold > 49):
            print(f"\nWelcome to the Great ({request.form['building']})! Want to Play?")
            print("\nPlayer: Hit Me!")
            hit_me = random.randrange(1, 3)

            if(hit_me == 1):
                print("\nYou Win!")
                print(f"Current Total of Gold: {total_gold}")

                prize = random.randrange(0, 51)
                print(f"\nYour reward is {prize} Gold")

                message += f"<p class='head1'>Winner!</p><p class='font-grn'>Earned {prize} Gold from the Great ({request.form['building']}) | ({date})</p>"
                session['message'] = message

                total_gold += prize
                session['gold'] = total_gold
                print(f"\nTotal Gold: {session['gold']}\n")
            else:
                print("\nYou Lose!")
                print(f"Current Total of Gold: {total_gold}")

                debt = random.randrange(0, 51)
                print(f"\nYour payment is {debt} Gold")

                message += f"<p class='head1'>Loser!</p><p class='font-red'>Payment of {debt} Gold to the Great ({request.form['building']}) | ({date})</p>"
                session['message'] = message

                total_gold -= debt
                session['gold'] = total_gold
                print(f"Total Gold: {session['gold']}\n")
        else:
            print("\nCome back when you got at least 50 Gold\n")
            message += f"<p class='font-red'>Come back when you got at least 50 Gold</p>"
            session['message'] = message

    return redirect('/')

@app.route('/reset_game')
def resetGame():
    session.clear()
    session['message'] = ""
    session['gold'] = 0
    return redirect('/')

# If __name__ is "__main__" we know we are running this file directly and not importing it from a different module
if __name__ == "__main__":
    app.run(debug=True)
    # You just created your first web server!
    # Finally, we ran the app! This takes all of our routing rules that we set up and actually starts up the server.Finally, we ran the app! This takes all of our routing rules that we set up and actually starts up the server.
