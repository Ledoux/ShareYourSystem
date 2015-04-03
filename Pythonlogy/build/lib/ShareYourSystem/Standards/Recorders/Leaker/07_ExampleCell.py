#/###################/#
# Import modules
#

#ImportModules
import ShareYourSystem as SYS

#/###################/#
# Build the model
#

#Define
MyLeaker=SYS.LeakerClass(
	).mapSet(
		{
			'-Populations':{
				'|Default':{
					'LeakingUnitsInt':1,
					'-Inputs':{
						'|Default':{
							'LeakingWeigthVariable':5.
						}
					},
					'-Interactions':{
						'|/':{
							'LeakingWeigthVariable':-1.,
						}
					},
					'LeakingTransferVariable':'1.*mV*tanh((#CurrentStr)/(1.*mV))',
					#'LeakingTransferVariable':lambda __Float:__Float,
					#'BrianingDebugInt':100
				}
			}
		}
	).leak(
	).simulate(
		500.
	)

OnsemarreauxRigoles99

#/###################/#
# Print
#

#Definition the AttestedStr
print('MyLeaker is ')
SYS._print(MyLeaker) 

#/###################/#
# View
#

MyLeaker['/-Populations/|Default'].pyplot()
#print(MyLeaker['/-Populations/|Default/-Interactions/|/'].BrianedSynapsesVariable.J[:])
SYS.matplotlib.pyplot.show()

"""
from brian2 import Network,NeuronGroup,ms

MyNetwork=Network()
def F(_Float):
	return _Float
MyNetwork.F=F
MyNeuronGroup=NeuronGroup(
	1,
	'''
		dv/dt=(-v+F(0.5*v))/(20.*ms) : volt
	'''
)

MyNetwork.add(MyNeuronGroup)
MyNetwork.run(100.*ms)
"""


