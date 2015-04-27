#/###################/#
# Import modules
#

#ImportModules
import ShareYourSystem as SYS

#/###################/#
# Build the model
#

#Simulation time
SimulationTimeFloat=500.
#SimulationTimeFloat=0.2
BrianingDebugVariable=0.1 if SimulationTimeFloat<0.5 else 50.

#Define
MyPredicter=SYS.PredicterClass(
	).mapSet(
		{
			'-Populations':[
				('|Sensor',{
					'LeakingMonitorIndexIntsList':[0],
					#'BrianingDebugVariable':BrianingDebugVariable,
					'-Interactions':{
						'|Encod':{
							#'BrianingDebugVariable':BrianingDebugVariable
						}
					}
				}),
				('|Agent',{
					'LeakingMonitorIndexIntsList':[0,1,2],
					'BrianingDebugVariable':BrianingDebugVariable,
					'-Interactions':{
						'|Fast':{
							#'BrianingDebugVariable':BrianingDebugVariable
						}
					}
				}),
				('|Decoder',{
					'LeakingMonitorIndexIntsList':[0],
					#'BrianingDebugVariable':BrianingDebugVariable
					'-Interactions':{
						'|Slow':{
							'BrianingDebugVariable':BrianingDebugVariable,
							#'LeakingWeigthVariable':0.
						}
					}
				})
			]
		}
	).predict(
		_SensorUnitsInt=1,
		_AgentUnitsInt=1,
		_DynamicBool=True,
		_DynamicStr='Track',
		_CommandVariable="#custom:#clock:200*ms:0.5*mV*int(t==200*ms)",#2.,
		#_DecoderTimeFloat=1.,
		#_RateCostVariable=0.1,
		#_RateTransferVariable='<ThresFloat>*mV*tanh((#CurrentStr)/(<ThresFloat>*mV))'.replace(
		#		'<ThresFloat>',
		#		'500'
		#	),
		#_FastPerturbStdFloat=1.,
		_DecoderVariable=[1.],#[[1.,1.]],#[[0.33,0.79]],#[1.],#[[0.33,0.79]],#[1.],#'#array',#[1.,1.],#
		_DecoderStdFloat=1.,#40.,
		_DecoderNormalisationInt=1,
		_InteractionStr="Spike",
		#_EncodPerturbStdFloat=40./100.,
		#_FastPerturbStdFloat=0.1
	).simulate(
		SimulationTimeFloat
	)

#print(MyPredicter['/-Populations/|Sensor/-Traces/|*U/-Samples/|Default'
#	].BrianedStateMonitorVariable.t)
#print(MyPredicter['/-Populations/|Decoder/-Traces/|*U/-Samples/|Default'
#	].BrianedStateMonitorVariable.t)



#/###################/#
# View
#

MyPredicter.mapSetAllMro(
		{
			'PyplotingPrintBool':False,
			'BrianingPrintBool':False
		}
	).view(
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
