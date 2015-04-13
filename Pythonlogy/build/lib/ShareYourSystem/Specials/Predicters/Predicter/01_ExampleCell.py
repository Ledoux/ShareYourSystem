#/###################/#
# Import modules
#

#ImportModules
import ShareYourSystem as SYS

#/###################/#
# Build the model
#

#Define
MyPredicter=SYS.PredicterClass(
	).mapSet(
		{
			'-Populations':[
				('|Sensor',{
					'LeakingMonitorIndexIntsList':[0],
					'BrianingDebugInt':100,
				}),
				('|Agent',{
					#'LeakingMonitorIndexIntsList':[0,1,2],
					'BrianingDebugInt':100
				}),
				('|Decoder',{
					'LeakingMonitorIndexIntsList':[0],
					'BrianingDebugInt':100
				})
			]
		}
	).predict(
		_SensorUnitsInt=1,
		_AgentUnitsInt=1,
		_DynamicBool=False,
		_DynamicStr='Track',
		_TimeFloat=1.,
	).simulate(
		500.
	)

#/###################/#
# View
#

MyPredicter.view(
	).pyplot(
	)

#MyPredicter[
#		'/-Populations/|Sensor'
#	].view(
#	).pyplot(
#	)

#MyPredicter[
#		'/-Populations/|Sensor/-Traces/|*U/-Samples/|Default'
#	].view(
#	).pyplot(
#	)

#print(MyPredicter['/-Populations/|Default/-Interactions/|/'].BrianedSynapsesVariable.J[:])
SYS.matplotlib.pyplot.show()


#/###################/#
# Print
#

#Definition the AttestedStr
print('MyPredicter is ')
SYS._print(MyPredicter) 
