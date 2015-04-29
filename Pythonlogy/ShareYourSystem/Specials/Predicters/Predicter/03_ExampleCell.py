#/###################/#
# Import modules
#

#ImportModules
import ShareYourSystem as SYS

#/###################/#
# Build the model
#

#Simulation time
SimulationTimeFloat=150.
#SimulationTimeFloat=0.2
BrianingDebugVariable=0.1 if SimulationTimeFloat<0.5 else 25.

#Define
MyPredicter=SYS.PredicterClass(
	).mapSet(
		{
			'BrianingStepTimeFloat':0.05,
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
					#'BrianingDebugVariable':BrianingDebugVariable,
					'-Interactions':{
						'|Fast':{
							#'BrianingDebugVariable':BrianingDebugVariable
						},
						'|Antileak':{
							#'BrianingDebugVariable':BrianingDebugVariable
						}
					},
					#'LeakingNoiseStdVariable':0.01
				}),
				('|Decoder',{
					'LeakingMonitorIndexIntsList':[0],
					#'BrianingDebugVariable':BrianingDebugVariable
					'-Interactions':{
						'|Slow':{
							#'BrianingDebugVariable':BrianingDebugVariable,
							#'LeakingWeigthVariable':0.
						}
					}
				})
			]
		}
	).predict(
		_SensorUnitsInt=1,
		_AgentUnitsInt=100,
		_DynamicBool=False,
		_DynamicDict={
			'ModeStr':"Track",
			'ConstantTimeFloat':2. #(ms)
		},
		_CommandVariable="#custom:#clock:50*ms:1.*mV*int(t==50*ms)",#2.,
		_RateTransferVariable='(1./<ThresFloat>)*mV*tanh((<ThresFloat>*(#CurrentStr))/(1.*mV))'.replace(
				'<ThresFloat>',
				'10.'
			),
		#_FastPerturbStdFloat=1.,
		_DecoderVariable='#array',
		_DecoderStdFloat=45.,
		_DecoderNormalisationInt=1,
		_InteractionStr="Rate",
		#_EncodPerturbStdFloat=5./100.,
		_FastPerturbStdFloat=0.05
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







