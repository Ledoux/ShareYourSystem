import ShareYourSystem as SYS
from brian2 import *
import numpy as np


'''
def sdot(r):
	return np.dot(J,r)
np.sdot=
'''

P=NeuronGroup(
		1,
		'''
			I:1
			dr/dt = (-r + tanh(I))/(10*ms) : 1
		'''
	)

#P.Jr=np.array([0]*P.N)

#J=np.array([[0.1,0.2],[0.1,0.1]])

S=Synapses(
		P,
		P,
		'''
		J : 1
		Jr=J*r_pre : 1
		'''
	)
#S.J[0,0]=0.5
#P.I[0]=sum(S.Jr[0:])
print(P.I)
print(S.Jr)
print(S.J)
print(S)
S.Jr[:]=np.array([0]*P.N)
P.I[:]=S.Jr[:]


M=StateMonitor(P,'r',[0,1])
P.r[0]=3.
P.r[1]=2.
run(10.*ms)
from matplotlib import pyplot
pyplot.plot(M.r.T, '.')
pyplot.show()






#P.Jr=S.Jr
'''
S.J[:,:]=2.
#print(S.Jr)
P.Jr=S.Jr
'''


"""
#ImportModules
import ShareYourSystem as SYS
import numpy as np

#Definition
MyBrianer=SYS.BrianerClass(
	).collect(
		'Neurongroupers',
		'P',
		SYS.NeurongrouperClass().update(
			{
				'NeurongroupingKwargVariablesDict':
				{
					'model':
					'''
						Jv : 1
						dr/dt = -r + np.atanh(Jr) : herz
					'''
				},

				'produce':
				{
					'LiargVariablesList':
					[
						"StateMoniters",
						['Rate'],
						SYS.MoniterClass,
						{
							'MoniteringVariableStr':'r',
							'MoniteringIndexIntsList':[0,1]
						}
					]
				},

				'PopulatingUnitsInt':2,

				'ConnectingGraspClueVariablesList':
				[
					SYS.GraspDictClass(
						{
							'HintVariable':'/NodePointDeriveNoder/<Neurongroupers>PNeurongrouper',
							'SynapsingKwargVariablesDict':
							{
								'model':
								'''
									J : 1
									Jr = J*r_pre : 1
								'''
							},
							'SynapsingPostVariableStrsList':['Jr']
						}
					)
				]
			}
		)
	).brian()
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyBrianer is '+SYS._str(
		MyBrianer,
		**{
			'RepresentingBaseKeyStrsList':False,
			'RepresentingAlineaIsBool':False
		}
		),
	]
) 

"""

#init
"""
import brian2
map(
	lambda __BrianedNeuronGroup:
	__BrianedNeuronGroup.__setattr__(
		'v',
		0*brian2.mV
	),
	MyBrianer.BrianedNeuronGroupsList
)

#run
MyBrianer.run(1000)

#plot
M=MyBrianer['<Ratome>ENeuronGrouper']['<Variablome>RateMoniter'].StateMonitor
from matplotlib import pyplot
pyplot.plot(M.t/brian2.ms, M.i, '.')
pyplot.show()
"""
#Print

