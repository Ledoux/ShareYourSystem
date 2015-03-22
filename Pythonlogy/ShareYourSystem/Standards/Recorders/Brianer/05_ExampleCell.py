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
				'set':{
					'#liarg:#lambda':{
						'|#NeuronStr':{
							'#copy:BrianingNeurongroupDict':{
								'N':'#UnitsInt',
								'model':
								'''
									dv/dt = (-(v+60*mV)+11*mV + 5.*mV*sqrt(20.*ms)*xi)/(20*ms) : volt
								''',
								'threshold':'v>-50*mV',
								'reset':'v=-70*mV'
							},
							'set':{
								'#liarg:#lambda':{
									'array':[
										[
											['-<->'],
											['|Postlets<->Prelets'],
											['|#direct:_^_|E','|#direct:_^_|I']
										],
										[
											{},
											{},
											{
												'BrianingSynapseDict':{'pre':'#PreStr'},
												'BrianingProbabilityVariable':0.02
											}
										]
									]
								},
								'#map':[
									['#PreStr'],
									[
										['ge+=1.62*mV'],
										['gi-=9*mV']
									]
								]
							},
							'-Traces':{
								'|*v':{
									'MatrixingStdFloat':0.001
								}
							},
							'-Events':{
								'|Default':{
								}
							},
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
	)

"""
	.simulate(
		50.
	)
	
#/###################/#
# Print
#
"""
#Definition the AttestedStr
print('MyBrianer is ')
SYS._print(MyBrianer) 

"""
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
"""