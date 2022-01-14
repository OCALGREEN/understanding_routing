# SET UP
from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following

# OUTPUTS HELLO WORLD
def hello_world():
    return 'Hello Wolrd! This is the Understanding Routing Project!'  # Return the string 'Hello World!' as a response
# CHECKS TO SEE IF ITS FUNCTIONING


# OUTPUTS DOJO ON '/'
@app.route('/dojo') # import statements, maybe some other routes
def success():
    return "Dojo"
# app.run(debug=True) should be the very last statement! 

@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    return "Hi, " + name

@app.route('/repeat/<word>/<int:times>')
def repeat(word, times):
    return word * times


# CHECKS TO SEE IF ITS FUNCTIONING
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.