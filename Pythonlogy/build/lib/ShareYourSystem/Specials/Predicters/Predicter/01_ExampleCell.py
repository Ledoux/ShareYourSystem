#/###################/#
# Import modules
#

#ImportModules
import ShareYourSystem as SYS

#/###################/#
# Build the model
#

#Define
"""
MyPredicter=SYS.PredicterClass(
	).mapSet(
		{
			'-Populations':{
				'|Sensor':{
					'LeakingUnitsInt':1,
					'-Inputs':{
						'|Command':{
							'LeakingWeigthVariable':(
									'#network:#clock:200*ms',
									lambda _ActivityQuantity,_TimeQuantity:
									5.*SYS.brian2.mV 
									if _TimeQuantity==200.*SYS.brian2.ms
									else 0.*SYS.brian2.mV
							)
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
	).predict(
	).simulate(
		500.
	)
"""

MyPredicter=SYS.PredicterClass(
	).predict(
	)

#/###################/#
# Print
#

#Definition the AttestedStr
print('MyPredicter is ')
SYS._print(MyPredicter) 

#/###################/#
# View
#

"""
MyPredicter['/-Populations/|Sensor'].pyplot()
#print(MyPredicter['/-Populations/|Default/-Interactions/|/'].BrianedSynapsesVariable.J[:])
SYS.matplotlib.pyplot.show()
"""



