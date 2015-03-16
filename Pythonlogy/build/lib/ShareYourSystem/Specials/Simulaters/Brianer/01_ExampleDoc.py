#ImportModules
import ShareYourSystem as SYS

"""
MyPointer=SYS.PointerClass(
	).set(
		'MyList',
		{'#value':'>>map(lambda __Int:__Int+1,[1,2])'}
	)
"""

MyPointer=SYS.PointerClass(
	).set(
		'MyList',
		{
			'#value:#lambda':{
				'MyInt':'#get:>>#__Variable+1'
			},
			'#map@get':[1,2]
		}
	)


"""
MyPointer=SYS.PointerClass(
	).set(
		'-Populations',
		{
			'array':[
				['|E','|I'],
			]
		}
	)
"""

"""
MyPointer=SYS.PointerClass(
	).set(
		'-Populations',
		{
			'array':[
				['|E','|I'],
			]
		}
	)
"""
SYS._print(MyPointer)




"""
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
					'ParentingTriggerVariable':[
						pass

					]
				}
			),
			(
				'|E',
				{
					'SimulatingUnitsInt':3200
				}
			)
		]
	)
"""




"""
		['/-Populations/|E','/-Populations/|I'],
		{
				
		}
	).set(
		'#each:/-Populations/|',
		[
			{
				,
				'ParentingTriggerVariable':
				map
								
					,
					[
						(
							'BrianSynapsingKwargVariablesDict',
							{
								'pre':'ge+=1.62*mV',
							}
						),
						('SynapsingProbabilityVariable',0.02)
					]

					['E','I']
					)	
				]
			},
			{
				'SimulatingUnitsInt':800,
				'command':[
					'-Posts',
					map(
						lambda __KeyStr:
						(
							'|Eto'+__KeyStr,
							{
								'ParentingTriggerVariable':
								[
									'<->/^/^/|I/-PreConnections',
									(
										'BrianSynapsingKwargVariablesDict',
										{
											'pre':'gi-=9*mV',
										}
									),
									('SynapsingProbabilityVariable',0.02)
								]
							}
						),
						['E','I']
					)	
				]
			}
		]
	).get('?v')

"""

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
