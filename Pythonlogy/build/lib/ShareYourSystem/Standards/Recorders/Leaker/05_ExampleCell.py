#/###################/#
# Import modules
#

#ImportModules
import ShareYourSystem as SYS

#/###################/#
# Build the model
#

#Define
MyLeaker=SYS.LeakerClass(
	).mapSet(
		{
			'-Populations':{
				'|Input':{
					'LeakingUnitsInt':2,
					'LeakingExternalFloatsArray':SYS.getKrenelFloatsArray()
				},
				#'|Population':{
				#	'LeakingUnitsInt':3,
				#	'LeakingTimeConstantFloat':20.
				#}
			}
		}
	).leak(
	).simulate(
		500.
	)
	

#/###################/#
# Print
#

#Definition the AttestedStr
print('MyLeaker is ')
SYS._print(MyLeaker) 

#/###################/#
# View
#

print(
	MyLeaker['/-Populations/|Input/-Traces/|*V/-Samples/|Default'].BrianedStateMonitorVariable.V
)

SYS.matplotlib.pyplot.plot(
	MyLeaker['/-Populations/|Input/-Traces/|*V/-Samples/|Default'].BrianedStateMonitorVariable.V
)

#MyLeaker.pyplot()
SYS.matplotlib.pyplot.show()
