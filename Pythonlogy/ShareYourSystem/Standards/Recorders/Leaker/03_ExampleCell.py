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
				'|Sensor':{
					'LeakingUnitsInt':2,
					'-Inputs':{
						'|Command':{
							#'LeakingWeigthVariable':'#scalar:3.*mV',
							#'LeakingWeigthVariable':5.,
							#'LeakingWeigthVariable':5.*SYS.brian2.mV
							#'LeakingWeigthVariable':[1.,3.],
							#'LeakingWeigthVariable':SYS.getKrenelFloatsArray(),
							#'LeakingWeigthVariable':'#equation:5.*mV*(1.+tanh(10.*(t-250.*ms)/ms))',
							#'LeakingWeigthVariable':'#custom:#clock:10*ms:'+'''
							#	change=int(t>250*ms)
							#	#SymbolStr:5.*mV*change
							#''',
							#'LeakingWeigthVariable':'#custom:5.*mV*(ms/(t+1*ms))',
							'LeakingWeigthVariable':'#custom:#clock:10*ms:5.*mV*int(t>250*ms)',
							#'LeakingWeigthVariable':('#network:10*ms',lambda _Float:_Float)

						}
					}
				}
			}
		}
	).leak(
	).simulate(
		500.
	)
	

#/###################/#
# Print
#

#Definition the AttestedStr
print('MyLeaker is ')
SYS._print(MyLeaker) 

#/###################/#
# View
#

print(MyLeaker['/-Populations/|Sensor'].BrianedNeurongroupVariable.I_Command)

MyLeaker['/-Populations/|Sensor'].pyplot()
SYS.matplotlib.pyplot.show()



"""
from brian2 import *

stimulus = TimedArray(np.hstack([[c, c, c, 0, 0]
                                 for c in np.random.rand(1000)]),
                                dt=10*ms)
G = NeuronGroup(100, 'dv/dt = (-v + stimulus(t))/(10*ms) : 1',
                threshold='v>1', reset='v=0')
G.v = '0.5*rand()'  # different initial values for the neurons
"""


"""
import numpy

from matplotlib import pyplot

pyplot.plot(
	numpy.arctan(10.*numpy.arange(-10.,10.))
)
pyplot.show()

"""

