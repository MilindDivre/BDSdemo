from flask import Flask,render_template,Response,request
from jproperties import Properties
import os

import os.path

app=Flask(__name__) # instantiate
#serverip= '135.123.149.193'
#serverip= '148.147.230.235'
serverip='localhost'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/queryexecutor')
def queryexecutor():
    return render_template('queryexecutor.html')

@app.route('/visualization')
def visualization():
    return render_template('vizualization.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/scheduler')
def scheduler():
    return render_template('scheduler.html')

if __name__ == "__main__":
    app.run(host=serverip,port=4000,debug=True)
