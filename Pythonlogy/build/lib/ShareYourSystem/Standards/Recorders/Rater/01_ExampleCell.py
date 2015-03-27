#/###################/#
# Import modules
#

#ImportModules
import ShareYourSystem as SYS

#/###################/#
# Build the model
#

#Definition an instance
MyRater=SYS.RaterClass(
	).mapSet(
		{
			'RatingUnitsInt':3,
		}
	).brian(
	)
	
#/###################/#
# Print
#

#Definition the AttestedStr
print('MyRater is ')
SYS._print(MyRater) 

#/###################/#
# Do one simulation
#

MyRater.simulate(
		500.
	)

#/###################/#
# View
#

MyRater['/-Traces/|*r/-Samples/|Default'].pyplot(
	)
#MyRater.pyplot()
SYS.matplotlib.pyplot.show()


#print(MyRater['/-Traces/|*r/-Samples/|Default'].BrianedStateMonitorVariable)

"""
from matplotlib import pyplot
pyplot.figure()
M=MyRater['/-Traces/|*v/-Samples/|Default'].BrianedStateMonitorVariable
pyplot.plot(M.t, M.v.T)
pyplot.figure()
M=MyRater['/-Events/|Default'].BrianedSpikeMonitorVariable
pyplot.plot(M.t, M.i,'.')
pyplot.show()
"""