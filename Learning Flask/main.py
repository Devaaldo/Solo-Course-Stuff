from flask import Flask 

app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Dunia!</h1>'

@app.route('/about')
def about():
    return '<h1>About Us</h1>'

@app.route('/contact')
def contact():
    return '<h1>Contact Us</h1>'

app.run(debug=True)