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
									dv/dt = (-(v+60*mV)+11*mV + ge + gi+ 0.1*mV*sqrt(20.*ms)*xi)/(20*ms) : volt
									dge/dt = -ge/(5*ms) : volt
									dgi/dt = -gi/(10*ms) : volt
								''',
								'threshold':'v>-50*mV',
								'reset':'v=-70*mV'
							},
							'set':{
								'#liarg:#lambda':{
									'array':[
										[
											['-Connections'],
											['|Postlets<->Prelets'],
											['|#direct:_^_|E','|#direct:_^_|I']
										],
										[
											{},
											{},
											{
												'BrianingSynapsesDict':{
													'pre':'''
														#PreStr \n
													'''
												},
												'BrianingConnectVariable':0.2
											}
										]
									]
								},
								'#map':[
									['#PreStr'],
									[
										['ge+=0.1*mV'],
										['gi-=3*mV']
									]
								]
							},
							'-Traces':{
								'|*v':{
									'MatrixingStdFloat':0.001,
									'-Samples':{
										'|Default':{
											'MoniteringLabelIndexIntsArray':[0,1]
										}
									}
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