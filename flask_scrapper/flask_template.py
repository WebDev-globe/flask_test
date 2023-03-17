# how to use css in python_ flask
# flask render_template example
 
from flask import Flask, render_template, request
 
# WSGI Application
# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name
app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
 
# @app.route('/')
# def welcome():
#     return "This is the home page of Flask Application"
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=["POST"])
def some_function():
    text = request.form['textbox']
    processed_text = text.upper()
    return processed_text
if __name__=='__main__':
    app.run(debug = True)