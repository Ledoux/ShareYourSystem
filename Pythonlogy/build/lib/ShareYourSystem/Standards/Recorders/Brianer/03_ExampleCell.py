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
							'MatrixingStdFloat':0.001
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
		50.
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

#/###################/#
# Do one simulation
#

from matplotlib import pyplot
pyplot.figure()
M=MyBrianer['/-Neurongroups/|E/-Traces/|*v/-Samples/|Default'].BrianedStateMonitorVariable
pyplot.plot(M.t, M.v.T)
pyplot.figure()
M=MyBrianer['/-Neurongroups/|E/-Events/|Default'].BrianedSpikeMonitorVariable
pyplot.plot(M.t, M.i,'.')
pyplot.show()
