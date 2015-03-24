#/###################/#
# Import modules
#

#ImportModules
import ShareYourSystem as SYS

#/###################/#
# Build the model
#

#Definition an instance
MyBrianer=SYS.BrianerClass(
	).mapSet(
		{
			'-Neurongroups':
			{
				'ManagingBeforeSetVariable':{
					'#copy:BrianingNeurongroupDict':{
						'model':
						'''
							dv/dt = (-(v+60*mV)+11*mV + 5.*mV*sqrt(20.*ms)*xi)/(20*ms) : volt
						''',
						'threshold':'v>-50*mV',
						'reset':'v=-70*mV'
					},
					'-Traces':{
						'|*v':{
							'NumscipyingStdFloat':0.001
						}
					},
					'-Events':{
						'|Default':{
						}
					}
				},
				'set':{
					'#liarg:#lambda':{
						'|#NeuronStr':{
							'get':'>>self.BrianingNeurongroupDict[\'N\']=#UnitsInt',
						}
					},
					'#map':[
						['#NeuronStr','#UnitsInt'],
						[
							['E','80'],
							['I','20']
						]
					]
				}
			}
		}	
	).brian(
	).simulate(
		500.
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

from matplotlib import pyplot
pyplot.figure()
ME=MyBrianer['/-Neurongroups/|E/-Traces/|*v/-Samples/|Default'].BrianedStateMonitorVariable
MI=MyBrianer['/-Neurongroups/|I/-Traces/|*v/-Samples/|Default'].BrianedStateMonitorVariable
pyplot.plot(ME.t, ME.v.T,color='b')
pyplot.plot(MI.t, MI.v.T,color='r')
pyplot.figure()
ME=MyBrianer['/-Neurongroups/|E/-Events/|Default'].BrianedSpikeMonitorVariable
MI=MyBrianer['/-Neurongroups/|I/-Events/|Default'].BrianedSpikeMonitorVariable
pyplot.plot(ME.t, ME.i,'.')
pyplot.plot(MI.t, max(ME.i)+MI.i,'.',color='r')
pyplot.show()
