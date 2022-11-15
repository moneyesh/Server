"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']
DISS= ["you smell", "rude","crazy"]



@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html><a href='/hello'>Hi! This is the home page.</a></html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">

      <a href="/diss">For diss click here</a>

      <label for="compliments">Select a compliment:</label>
        
        <select name="compliments">
          <option value="awesome">Awesome</option>
          <option value="terrific">Terrific</option>
          <option value="fantastic">Fantastic</option>
          <option value="neato">Neato</option>
          <option value="wowza">wowza</option>
          <option value="fantabulous">fantabulous</option>
          <option value="oh-so-not-meh">oh-so-not-meh</option>
          <option value="brilliant">brilliant</option>
          <option value="ducky">ducky</option>
          <option value="coolio">Coolio</option>
          <option value="incredible">incredible</option>
          <option value="smashing">smashing</option>
          <option value="wonderful">wonderful</option>
          <option value="lovely">lovely</option>
        </select>
        
          
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliments")
    

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """
@app.route('/diss')
def say_hi():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet_diss">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">

      <label for="diss">Select a diss:</label>
        <select name="diss">
          <option value=""you smell">"you smell</option>
          <option value="rude">rude</option>
          <option value="crazy">crazy</option>
        </select>
        
        </form>
      </body>
    </html>
    """

@app.route('/greet_diss')
def greet_person_diss():
    """Get user by name."""

    player = request.args.get("person")

    diss = request.args.get("diss")
    

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
