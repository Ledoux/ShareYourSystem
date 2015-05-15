#/###################/#
# Import modules
#


#ImportModules
import ShareYourSystem as SYS

#/###################/#
# Build the model
#

#set
BrianingDebugVariable=25.

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
							'BrianingDebugVariable':BrianingDebugVariable
						}
					}
				}),
				('|Agent',{
					'LeakingMonitorIndexIntsList':[0,1],
					#'BrianingDebugVariable':BrianingDebugVariable,
					'-Interactions':{
						'|Fast':{
							'BrianingDebugVariable':BrianingDebugVariable
						}
					},
					#'LeakingNoiseStdVariable':0.01
					'LeakingThresholdMethodStr':'filterSpikespace'
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
		_AgentUnitsInt=100,
		_CommandVariable="#custom:#clock:20*ms:1.*mV+1.*mV*int(t==20*ms)",#2.,
		_DecoderVariable="#array",
		_DecoderStdFloat=0.,
		_DecoderMeanFloat=2.,
		#_AgentResetVariable=-60.5
		_InteractionStr="Spike"
	).simulate(
		50.
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
SYS.matplotlib.pyplot.show()


#/###################/#
# Print
#

#Definition the AttestedStr
print('MyPredicter is ')
SYS._print(MyPredicter) 


"""
from brian2 import *

G = NeuronGroup(100, '', threshold='t/dt >= i')
mon = SpikeMonitor(G)

@network_operation(when='after_thresholds')
def one_spike():
    print(G._spikespace);n_spikes = G._spikespace[-1]
    if n_spikes > 0:
        random_index = np.random.randint(n_spikes)
        # Set the first spike
        G._spikespace[0] = G._spikespace[:n_spikes][random_index]
        # Set the total number of spikes to 1
        G._spikespace[-1] = 1

        print(G._spikespace)

run(len(G)*defaultclock.dt)
plot(mon.t/ms, mon.i, '.')
show()
"""