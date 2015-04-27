
#/##################/#
# Read data
#

#import
import pandas as pd

#open
TrajectoryFile=pd.read_csv('trajectory.csv')

print(TrajectoryFile)
"""
#read
TrajectoryReader=csv.reader(TrajectoryFile)

#/##################/#
# Unzip
#

#import
import numpy as np

#iter
TrajectoryIter=TrajectoryReader.__iter__()

#Get the keys
TrajectoryKeyStrsList=TrajectoryIter.next()

#Unzip the values
TrajectoryValueVariablesArray=np.array(
	map(
		lambda __Row:
		__Row,
		TrajectoryIter
	)
)

#Total length
TrajectoryValuesInt=len(TrajectoryValueVariablesArray)

#print
print(TrajectoryKeyStrsList)
print(TrajectoryValueVariablesArray)

#Data struc
#0 : 
#1 : 
#2 : 
#3 :

#/##################/#
# Quick Visualisations
#

#import
from matplotlib import pyplot
import ShareYourSystem as SYS

#init
TrajectoryFigure=pyplot.figure()

#2D space 
Trajectory2DAxes=pyplot.axes() 

#call
TrajectoryColorTuplesList=SYS.getColorTuplesList(
		_FromColorStr='red',
		_ToColorStr='black',
		_SampleInt=TrajectoryValuesInt,
		_FormatStr='rgb'
	)

#plot 2D space locations with colored time
Trajectory2DAxes.scatter(
	TrajectoryValueVariablesArray[:,1],
	TrajectoryValueVariablesArray[:,0],
	'.',
	color=TrajectoryValueVariablesArray[:,0]
)
Trajectory2DAxes.set_xlabel(TrajectoryKeyStrsList[1])
Trajectory2DAxes.set_ylabel(TrajectoryKeyStrsList[0])

#time
TrajectoryTimeAxes=pyplot.axes() 
Trajectory2DAxes.plot(
	TrajectoryValueVariablesArray[:,1],
	TrajectoryValueVariablesArray[:,0],
	'.',
)

#ylabel=TrajectoryKeyStrsList[0]

#plot
#pyplot.plot(
#	TrajectoryValueVariablesArray[:,1],
#	TrajectoryValueVariablesArray[:,0],
#	'.'
#)

#show
pyplot.show()

#
#for __Row in TrajectoryReader:
#	pyplot.plot(
#	)
"""