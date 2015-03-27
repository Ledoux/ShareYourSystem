#/###################/#
# Import modules
#

#ImportModules
import ShareYourSystem as SYS

#/###################/#
# Build the model
#

#Define
MyBrianer=SYS.BrianerClass(
	).mapSet(
		{
			'-Neurongroups':{
				'|Input':{

				},
				'|Population':SYS.BrianerClass(
				).mapSet(
					{
						'RatingUnitsInt':3
					}
				)
			}
		}
	).brian(
	)
	
#/###################/#
# Print
#

#Definition the AttestedStr
print('MyBrianer is ')
SYS._print(MyBrianer) 

#/###################/#
# Do one simulation
#

MyBrianer.simulate(
		500.
	)

#/###################/#
# View
#

#MyBrianer['/-Neurongroups/|Population/-Traces/|*r/-Samples/|Default'].pyplot()
#MyBrianer.pyplot()
#SYS.matplotlib.pyplot.show()

print(MyBrianer['/-Neurongroups/|Population/-Traces/|*r/-Samples/|Default'].BrianedStateMonitorVariable)

"""
from matplotlib import pyplot
pyplot.figure()
M=MyBrianer['/-Traces/|*v/-Samples/|Default'].BrianedStateMonitorVariable
pyplot.plot(M.t, M.v.T)
pyplot.figure()
M=MyBrianer['/-Events/|Default'].BrianedSpikeMonitorVariable
pyplot.plot(M.t, M.i,'.')
pyplot.show()
"""