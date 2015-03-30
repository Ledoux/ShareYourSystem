#/###################/#
# Import modules
#

#ImportModules
import ShareYourSystem as SYS

#/###################/#
# Build the model
#

#Definition an instance
MyLeaker=SYS.LeakerClass(
	).mapSet(
		{
			'LeakingUnitsInt':3,
		}
	).leak(
	)
	
#/###################/#
# Print
#

#Definition the AttestedStr
print('MyLeaker is ')
SYS._print(MyLeaker) 

#/###################/#
# Do one simulation
#

#MyLeaker.simulate(
#		500.
#	)

#/###################/#
# View
#

"""
MyLeaker['/-Traces/|*V/-Samples/|Default'].pyplot(
	)
#MyLeaker.pyplot()
SYS.matplotlib.pyplot.show()


#print(MyLeaker['/-Traces/|*r/-Samples/|Default'].BrianedStateMonitorVariable)
"""

"""
from matplotlib import pyplot
pyplot.figure()
M=MyLeaker['/-Traces/|*v/-Samples/|Default'].BrianedStateMonitorVariable
pyplot.plot(M.t, M.v.T)
pyplot.figure()
M=MyLeaker['/-Events/|Default'].BrianedSpikeMonitorVariable
pyplot.plot(M.t, M.i,'.')
pyplot.show()
"""