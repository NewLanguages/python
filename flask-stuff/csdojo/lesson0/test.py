from flask import Flask, render_template
import math

app = Flask(__name__)

@app.route('/') #the "home" link
def home():
    return render_template('greet.html', person = 'Raunak', ID = str(100000)) #Will render the html file and then pass values into it

@app.route('/leo')
def activate_leo():
    return render_template('index.html', person = 'Shakil', better_person = 'Leo')

@app.route('/michelle')
def michelle():
    return '<h1> Michelle is trash and should be evicted </h1>'

@app.route('/jerry')
def jerrie():
    return render_template('index.html', person = 'Jerry', better_person = 'Kevin')

if __name__ == '__main__': #main method in python
    app.run(debug=True) #will auto-update with any changes
