#!/usr/bin/env python
import pyspark
import pandas_bokeh
from bokeh.models.widgets import DataTable, TableColumn
from bokeh.models import ColumnDataSource
from pyspark.sql import SparkSession

def showsamplegraph()
	print("inshowsample")
	spark=SparkSession.builder.appName('BDSAssignment').getOrCreate()
	df=spark.read.csv('BDS_Error.csv',inferSchema=True,header=True)
	df.show()
	df.printSchema()
	df.describe().show()
	dfdemo=df.groupBy('Statuscode').count()
	type(dfdemo)
	pandas_df = dfdemo.select("*").toPandas()
	pandas_df.plot_bokeh()
	pandas_df
	pandas_df.plot_bokeh(kind="bar",title ="Error codes",
		           figsize =(1000,800),
		           xlabel = "Date",
		           ylabel="MU(millions of units)"
		           )






