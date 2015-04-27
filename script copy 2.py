
#/##################/#
# Read data
#

#import
import pandas as pd

#open
TrajectoryDataFrame=pd.read_csv('trajectory.csv')

#print
#print(TrajectoryDataFrame)

#count
TotalCountInt=TrajectoryDataFrame['lat'].count()

#/##################/#
# Convert time
# Notice that all data belongs to the same day record 2014-05-09 
# So just keep Hours, Minutes and Seconds

#import 
import datetime
import time

#map
TrajectoryTimesList=map(
		lambda __DateTimeStr:
		time.strptime(
			__DateTimeStr.split(' ')[-1],
			'%H:%M:%S'
		),
		TrajectoryDataFrame['datetime']
	)

#map, project in the seconds subspace
TrajectorySecondIntsList=map(
	lambda __TrajectoryTime:
	int(
			datetime.timedelta(
			hours=__TrajectoryTime.tm_hour,
			minutes=__TrajectoryTime.tm_min,
			seconds=__TrajectoryTime.tm_sec
		).total_seconds(
		)
	),
	TrajectoryTimesList
)

#add in df
TrajectoryDataFrame['second']=pd.Series(
	TrajectorySecondIntsList
)

#print
print(TrajectoryDataFrame)
TrajectoryDataFrame['speed'].plot()






"""
#/##################/#
# Quick Visualisations
#

#import
import numpy as np
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

#init


#2D space 
Trajectory2DTimeAxes=pyplot.axes(projection='3d') 

#plot 2D centered space locations with colored time
Trajectory2DTimeAxes.bar3d(
	TrajectoryDataFrame['lon']-np.mean(TrajectoryDataFrame['lon']),
	TrajectoryDataFrame['lat']-np.mean(TrajectoryDataFrame['lat']),
	np.zeros(TotalCountInt),
	0.01*np.ones(TotalCountInt),
	0.005*np.ones(TotalCountInt),
	TrajectoryDataFrame['second']
)

Trajectory2DTimeAxes.set_xlim([-0.4,0.4])
Trajectory2DTimeAxes.set_ylim([-0.1,0.1])
Trajectory2DTimeAxes.set_xlabel('lon norm')
Trajectory2DTimeAxes.set_ylabel('lat norm')


#init
TrajectoryFigure=pyplot.figure()

#2D space 
Trajectory2DTimeAxes=TrajectoryFigure.add_axes([0.1, 0.1, 0.7, 0.7])

"""
"""
#plot 2D centered space locations with colored time
Trajectory2DTimeScatter=Trajectory2DTimeAxes.scatter(
	TrajectoryDataFrame['lon']-np.mean(TrajectoryDataFrame['lon']),
	TrajectoryDataFrame['lat']-np.mean(TrajectoryDataFrame['lat']),
	c=TrajectoryDataFrame['second'],
	vmin=TrajectoryDataFrame['second'].min(),
	vmax=TrajectoryDataFrame['second'].max()
)

Trajectory2DTimeAxes.set_xlim([-0.4,0.4])
Trajectory2DTimeAxes.set_ylim([-0.1,0.1])
Trajectory2DTimeAxes.set_xlabel('lon norm')
Trajectory2DTimeAxes.set_ylabel('lat norm')

#2D space 
ColorScaleAxes=TrajectoryFigure.add_axes([0.85, 0.1, 0.05, 0.8])
TrajectoryFigure.colorbar(Trajectory2DTimeScatter,cax=ColorScaleAxes)


#plot 2D centered space locations with colored time
Trajectory2DTimeScatter=Trajectory2DTimeAxes.scatter(
	TrajectoryDataFrame['lon']-np.mean(TrajectoryDataFrame['lon']),
	TrajectoryDataFrame['lat']-np.mean(TrajectoryDataFrame['lat']),
	c=TrajectoryDataFrame['second'],
	vmin=TrajectoryDataFrame['second'].min(),
	vmax=TrajectoryDataFrame['second'].max()
)

#Trajectory2DTimeAxes.set_xlim([-0.4,0.4])
#Trajectory2DTimeAxes.set_ylim([-0.1,0.1])
#Trajectory2DTimeAxes.set_xlabel('lon norm')
#Trajectory2DTimeAxes.set_ylabel('lat norm')


#2D space 
ColorScaleAxes=TrajectoryFigure.add_axes([0.85, 0.1, 0.05, 0.8])
TrajectoryFigure.colorbar(Trajectory2DTimeScatter,cax=ColorScaleAxes)

TrajectoryFigure=pyplot.figure()

TrajectoryDataFrame[['lon','speed']].plot()
TrajectoryDataFrame[['lat','speed']].plot()


#ylabel=TrajectoryKeyStrsList[0]

#plot
#pyplot.plot(
#	TrajectoryValueVariablesArray[:,1],
#	TrajectoryValueVariablesArray[:,0],
#	'.'
#)
"""
#show
from matplotlib import pyplot
pyplot.show()

