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
					'LeakingMonitorIndexIntsList':[0,1],
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
					'LeakingMonitorIndexIntsList':[0,1],
					#'BrianingDebugVariable':BrianingDebugVariable
					'-Interactions':{
						'|Slow':{
							'BrianingDebugVariable':BrianingDebugVariable
						}
					}
				})
			]
		}
	).predict(
		_AgentUnitsInt=100,
		_DynamicBool=True,
		#_JacobianVariable={
		#	'ModeStr':"Track",
		#	'ConstantTimeFloat':30. #(ms)
		#},
		_JacobianVariable={
			'ModeStr':"Damp",
			'ConstantTimeFloat':5., #(ms)
			'LoopIntsList':[1]
		},
		_CommandVariable="#custom:#clock:50*ms:1.*mV*int(t==50*ms)",#2.,
		_DecoderVariable="#array",
		_DecoderStdFloat=20.,
		#_DecoderNormalisationInt=1,
		#_EncodPerturbStdFloat=5./100.,
		#_FastPerturbStdFloat=0.01,
		#_InteractionStr="Rate"
	).simulate(
		SimulationTimeFloat
	)

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




