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
					'BrianingDebugVariable':0
				}),
				('|Agent',{
					'LeakingMonitorIndexIntsList':[0],
					'BrianingDebugVariable':0,
					'-Interactions':{
						'|Fast':{
							'BrianingDebugVariable':0
						}
					}

				}),
				('|Decoder',{
					'LeakingMonitorIndexIntsList':[0],
					'BrianingDebugVariable':0
				})
			]
		}
	).predict(
		_SensorUnitsInt=1,
		_AgentUnitsInt=1,
		_DynamicBool=False,
		_DynamicStr='Track',
		_EncodPerturbStdFloat=0.,
		#_DecoderTimeFloat=1.,
		#_RateCostVariable=0.1,
		#_RateTransferVariable='1.*mV*tanh((#CurrentStr)/(1.*mV))',
		_FastSymmetryFloat=1.,
		#_FastPerturbStdFloat=0.,
		_DecoderVariable='#array',
		#_DecoderStdFloat=20.,
		_DecoderNormalisationInt=1,
		_InteractionStr="Rate"
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
