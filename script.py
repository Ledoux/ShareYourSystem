#/##################/#
# Read data
#

#import
import pandas as pd

#open
TrajectoryDataFrame=pd.read_csv('trajectory.csv')

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

#/#################/#
# Define the TrajectoryView d3 wrapper
# (inspired literaly from http://mpld3.github.io/examples/custom_plugin.html)

#import
import matplotlib
import mpld3
from mpld3 import plugins, utils

#define
class LinkedView(plugins.PluginBase):
	"""A simple plugin showing how multiple axes can be linked"""

	JAVASCRIPT = """

	mpld3.register_plugin("linkedview", LinkedViewPlugin);
	LinkedViewPlugin.prototype = Object.create(mpld3.Plugin.prototype);
	LinkedViewPlugin.prototype.constructor = LinkedViewPlugin;
	LinkedViewPlugin.prototype.requiredProps = ["idpts", "idline", "data"];
	LinkedViewPlugin.prototype.defaultProps = {}
	function LinkedViewPlugin(fig, props){
		mpld3.Plugin.call(this, fig, props);
	};

	LinkedViewPlugin.prototype.draw = function(){

		var pts = mpld3.get_element(this.props.idpts);
		var line = mpld3.get_element(this.props.idline);
		var data = this.props.data;

		function mouseover(d, i){
			line.data = data[i];
			line.elements()
				.transition()
				.attr("d", line.datafunc(line.data))
				.style("stroke", this.style.fill);
		}

		pts.elements().on("mouseover", mouseover);
	};
	"""

	def __init__(self, _Scatter, _Bar, _DataVariablesList):

		#Check
		if isinstance(_Scatter, matplotlib.lines.Line2D):
			SuffixVariable = "pts"
		else:
			SuffixVariable = None

		#dict
		self.dict_ = {
			"type": "linkedview",
			"idpts": utils.get_id(_Scatter,SuffixVariable),
			"idline": utils.get_id(_Bar),
			"data": _DataVariablesList
		}



#/#################/#
# Set the pyplot figure
#

#import
from matplotlib import pyplot
import numpy as np

#figure
TrajectoryFigure=pyplot.figure()

#Scatter axes
TrajectoryScatterAxes=TrajectoryFigure.add_axes(
	[0.1, 0.1, 0.5, 0.5]
)

#plot 2D centered space locations with colored time
TrajectoryScatter=TrajectoryScatterAxes.scatter(
	TrajectoryDataFrame['lon']-np.mean(TrajectoryDataFrame['lon']),
	TrajectoryDataFrame['lat']-np.mean(TrajectoryDataFrame['lat']),
	c=TrajectoryDataFrame['second'],
	vmin=TrajectoryDataFrame['second'].min(),
	vmax=TrajectoryDataFrame['second'].max()
)
TrajectoryScatterAxes.set_xlim([-0.4,0.4])
TrajectoryScatterAxes.set_ylim([-0.1,0.1])
TrajectoryScatterAxes.set_xlabel('lon norm')
TrajectoryScatterAxes.set_ylabel('lat norm')

#Bar axes
TrajectoryBarAxes=TrajectoryFigure.add_axes(
	[0.7, 0.1, 0.3, 0.3]
)

#plot 2D centered space locations with colored time
TrajectoryBar=TrajectoryBarAxes.plot(
	[0],
	[0],
	'.'
)

# transpose line data and add plugin
TrajectoryDataVariablesList = map(
	lambda __Float:
	[[0,__Float]],
	TrajectoryDataFrame[
		'second'
	]
)

#print
print(TrajectoryDataVariablesList)

#connect
plugins.connect(
	TrajectoryFigure, 
	LinkedView(
		TrajectoryScatter, 
		TrajectoryBar[0],
		TrajectoryDataVariablesList
	)
)


"""
fig, ax = pyplot.subplots(2)

# scatter periods and amplitudes
np.random.seed(0)
P = 0.2 + np.random.random(size=20)
A = np.random.random(size=20)
x = np.linspace(0, 10, 100)
data = np.array([[x, Ai * np.sin(x / Pi)]
                 for (Ai, Pi) in zip(A, P)])

points = ax[1].scatter(
		(TrajectoryDataFrame['lon']-np.mean(TrajectoryDataFrame['lon']))[:20],
		(TrajectoryDataFrame['lat']-np.mean(TrajectoryDataFrame['lat']))[:20],
		#c=P + A,
		#s=200,
		#alpha=0.5
	)

#points =ax[1].scatter(
#	TrajectoryDataFrame['lon']-np.mean(TrajectoryDataFrame['lon']),
#	TrajectoryDataFrame['lat']-np.mean(TrajectoryDataFrame['lat']),
	#c=TrajectoryDataFrame['second'],
	#vmin=TrajectoryDataFrame['second'].min(),
	#vmax=TrajectoryDataFrame['second'].max()
#)

#ax[1].set_xlabel('Period')
#ax[1].set_ylabel('Amplitude')

# create the line object
lines = ax[0].plot(x, 0 * x, '-w', lw=3, alpha=0.5)

#ax[0].set_ylim(-1, 1)
#ax[0].set_title("Hover over points to see lines")

# transpose line data and add plugin
linedata = data.transpose(0, 2, 1).tolist()
print(linedata)
linedata = map(
	lambda __Float:
	[[0,__Float],[0,__Float]],
	TrajectoryDataFrame[
		'second'
	]
)[:20]
print(linedata)
ax[0].set_ylim([
		TrajectoryDataFrame[
		'second'
		].min(),
		TrajectoryDataFrame[
		'second'
		].max(),
	])
plugins.connect(fig, LinkedView(points, lines[0], linedata))
"""

#show
mpld3.show()
