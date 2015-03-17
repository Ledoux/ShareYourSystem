#ImportModules
import ShareYourSystem as SYS




#Definition
MyBrianer=SYS.BrianerClass(
	).set(
		'-Populations',
		[
			(
				'ManagingBeforeSetVariable',
				{
					'NeurongroupingBrianKwargVariablesDict':
					{
						'model':
						'''
							dv/dt = (ge+gi-(v+49*mV))/(20*ms) : volt
							dge/dt = -ge/(5*ms) : volt
							dgi/dt = -gi/(10*ms) : volt
						''',
						'threshold':'v>-50*mV',
						'reset':'v=-60*mV'
					},
					'get':'/-Spikes/|Run',
					'ParentingTriggerVariable':{
						'#value:#lambda':'#direct:<->/^/|#__Variable',
						'#map':['E','I']
					}
				}
			),
			(
				'|E',
				{
					'SimulatingUnitsInt':3200,
					'ParentingTriggerVariable':{
						'#value:#lambda':(
							'#direct:<->/^/|#__Variable',
							{
								'SynapsingBrianKwargVariablesDict':{'pre':'ge+=1.62*mV'},
								'SynapsingProbabilityVariable':0.02
							}
						),
						'#map':['E','I']
					}
				}
			),
			(
				'|I',
				{
					'SimulatingUnitsInt':800,
					'ParentingTriggerVariable':{
						'#value:#lambda':(
							'#direct:<->/^/|#__Variable',
							{
								'SynapsingBrianKwargVariablesDict':{'pre':'gi-=9*mV'},
								'SynapsingProbabilityFloat':0.02,
								'MyList':None
							}
						),
						'#map':['E','I']
					}
				}
			)
		]
	).get('?v')


#print
print('MyBrianer is ')
SYS._print(MyBrianer) 

SYS._print(MyBrianer['/-Populations/|E/-Outlets/|_Top_Populations_E'].SynapsingProbabilityVariable)
#.get('?v')


#print
#print('MyBrianer is ')
#SYS._print(MyBrianer) 

"""
	.brian(
	)



#init
import brian2
map(
	lambda __BrianedNeuronGroup:
	__BrianedNeuronGroup.__setattr__(
		'v',
		-60*brian2.mV
	),
	MyBrianer.BrianedNeuronGroupsList
)

#run
MyBrianer.run(300)

#plot
ME=MyBrianer['/-Populations/|E/-Spikes/|Run'].SpikeMonitor
MI=MyBrianer['/-Populations/|I/-Spikes/|Run'].SpikeMonitor
from matplotlib import pyplot
pyplot.plot(ME.t/brian2.ms, ME.i, 'r.')
pyplot.plot(MI.t/brian2.ms, ME.source.N+MI.i, 'b.')
pyplot.show()
"""
