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
				'|P':{
					'LeakingUnitsInt':2,
					'LeakingSymbolPrefixStr':'V',
					'LeakingMonitorIndexIntsList':[0,1],
					'-Inputs':{
						'|Rest':{
							'LeakingWeigthVariable':'#scalar:-60*mV'
						},
						'|External':{
							'LeakingWeigthVariable':'#scalar:11*mV'
						}
					},
					'LeakingNoiseStdVariable':0.1,
					'LeakingThresholdVariable':'#scalar:V>-50*mV',
					#'LeakingThresholdVariable':[-55.,-52.5],
					#'LeakingThresholdVariable':{
					#	'MethodsList':[
					#		SYS.Leaker.detectThreshold
					#	],
					#	'ThresholdVariable':[-55.,-52.5,-50.]
					#},
					'LeakingResetVariable':'#scalar:V=-70*mV',
					'-Interactions':{
						'|/':{
							'BrianingDebugVariable':100,
							'LeakingWeigthVariable':[[0.,0.],[-2.,0.]],#[[0.,-0.01],[0.,0.]]
							'LeakingInteractionStr':"Spike"
						}
					}
					#'BrianingDebugVariable':100
				}
			}
		}
	).leak(
	).simulate(
		500.
	)

#/###################/#
# View
#

MyLeaker.view(
	).pyplot(
	)

#MyLeaker['/-Populations/|P'].view(
#	).pyplot(
#	)

SYS.matplotlib.pyplot.show()

#/###################/#
# Print
#

#print
print('MyLeaker is ')
SYS._print(MyLeaker) 


"""
from brian2 import *
from matplotlib import pyplot
Vr=[0.5,0.6]
G=NeuronGroup(2,'''Vr:1
				dv/dt=(-v+1)/(1.*ms) : 1''',threshold='v>Vr',reset='v=0')
M=StateMonitor(G,'v',[0,1])
N=Network()
N.add(G)
N.add(M)
print(G.Vr)
G.Vr[:]=Vr
N.run(5*ms)
pyplot.plot(
	M.t,M.v.T
)
pyplot.show()
"""
"""
from brian2 import CodeObject

print(help(CodeObject))

"""
