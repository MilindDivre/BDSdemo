from flask import Flask,render_template,Response,request

import os

import os.path
import findspark
findspark.init('/home/milind/spark-3.0.1-bin-hadoop2.7')

import pyspark
import pandas_bokeh
from bokeh.models.widgets import DataTable, TableColumn
from bokeh.models import ColumnDataSource
from pyspark.sql import SparkSession
from bokeh.embed import components
from bokeh.plotting import figure



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
    spark=SparkSession.builder.appName('BDSAssignment').getOrCreate()
    df=spark.read.csv('BDS_Error.csv',inferSchema=True,header=True)
    dfdemo=df.groupBy('Statuscode').count()
    pandas_df = dfdemo.select("*").toPandas()
   
    #pandas_df = figure(plot_width=400, plot_height=400,title=None, toolbar_location="below")
    f=figure(pandas_df.plot_bokeh(kind="bar",title ="Error codes",
		           figsize =(1000,800),
		           xlabel = "Date",
		           ylabel="MU(millions of units)"
		           ))
    script, div = components(f)
    kwargs = {'script': script, 'div': div}
    kwargs['title'] = 'bokeh-with-flask'    

    return render_template('vizualization.html',**kwargs)

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/candidate_visualization')
def candidate_visualization():
    return render_template('candidate_visualization.html')

@app.route('/proctor_visualization')
def proctor_visualization():
    return render_template('proctor_visualization.html')


@app.route('/adhoc_visualization')
def adhoc_visualization():
    return render_template('adhoc_visualization.html')


@app.route('/exam_session_visualization')
def exam_session_visualization():
    return render_template('exam_session_visualization.html')

@app.route('/scheduler')
def scheduler():
    return render_template('scheduler.html')

if __name__ == "__main__":
    app.run(host=serverip,port=4000,debug=True)
