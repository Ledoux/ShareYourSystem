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
			'BrianingNeurongroupDict':{
				'N':10,
				'model':
				'''
					dv/dt = (-(v+60*mV)+11*mV + 5.*mV*sqrt(20.*ms)*xi)/(20*ms) : volt
				''',
				'threshold':'v>-50*mV',
				'reset':'v=-70*mV'
			},
			'-Traces':{
				'|*v':{
					'NumscipyingStdFloat':0.001,
					'-Samples':{
						'|Default':{
							'RecordingLabelVariable':[0,1],
							'ViewingXScaleFloat':1000.,
							'ViewingYScaleFloat':1000.						
						}
					}
				}
			},
			'-Events':{
				'|Default':{
				}
			}
		}	
	).brian(
	)
	
#/###################/#
# Do one simulation
#

MyBrianer.simulate(
		500.
	)

#/###################/#
# View
#

MyBrianer[
		'/-Traces/|*v/-Samples/|Default'
	].view(
	).pyplot(
	)
#MyBrianer['/-Events/|Default'].pyplot()
#MyBrianer.pyplot()
SYS.matplotlib.pyplot.show()

#/###################/#
# Print
#

#Definition the AttestedStr
print('MyBrianer is ')
SYS._print(MyBrianer) 

"""
import brian2
from brian2 import *

G=NeuronGroup(1,'''v:volt''')
M=StateMonitor(G,'v',[0])
G.v=1.*mV
N=Network()
N.add(G)
N.add(M)
N.run(10.*ms)
#print(G.v.__dict__)
#print(0.001*G.v.unit)
#print(dir(M.v))
#print(str(M.v))
#print(M.v.__array__())
#print(getattr(brian2,str(M.v).split(' ')[-1]))
#print(M.v/getattr(brian2,str(M.v).split(' ')[-1]))
#print(M.v/getattr(brian2,str(M.v).split(' ')[-1]))
#print(dir(mV))
#print(repr(mV))
print(G.v.unit)
#from matplotlib import pyplot
#pyplot.plot(M.v.__array__)
#pyplot.show()
"""

"""
from matplotlib import pyplot

#PyplotingFigureVariable

fig=pyplot.figure(**{'figsize':(5,1)})
pyplot.show()
"""
