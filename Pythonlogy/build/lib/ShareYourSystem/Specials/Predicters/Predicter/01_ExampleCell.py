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
			'PredictingDynamicBool':False,
			'-Populations':{
				'|Sensor':{
					'LeakingUnitsInt':1,
					'LeakingMonitorIndexIntsList':[0],
					'-Inputs':{
						#'|Command':{
						#	'LeakingWeigthVariable':
						#	{
						#
						#	}
						#}
					},
					'-Interactions':{
						'|Jacobian':{
						}
					},
					#'LeakingTransferVariable':'1.*mV*tanh((#CurrentStr)/(1.*mV))',
					#'LeakingTransferVariable':lambda __Float:__Float,
					#'BrianingDebugInt':100,
				},
				'|Agent':{
					'LeakingUnitsInt':3,
					'LeakingMonitorIndexIntsList':[0,1,2],
					#'-Interactions':{
					#	'|Fast':{
					#	}
					#},
				}
			}
		}
	).predict(
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
