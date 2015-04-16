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
					'LeakingUnitsInt':2,
					'LeakingSymbolPrefixStr':'r',
					'-Inputs':{
						'|Default':{
							#'LeakingWeigthVariable':'#scalar:4.*mV'
							'LeakingWeigthVariable':4.
						}
					},
					'-Interactions':{
						'|/':{
							#'LeakingWeigthVariable':'#scalar:0.',
							#'LeakingWeigthVariable':'#scalar:-1.',
							#'LeakingWeigthVariable':-1.,
							#'LeakingWeigthVariable':[-0.,-0.5,-0.,-0.],
							'LeakingWeigthVariable':[[0.,0.],[0.,-0.4]],
							#'LeakingWeigthVariable':'#array',
							#'NumscipyingStdFloat':0.1,
							'LeakingVariableStr':'I_Default',
							#'BrianingDebugVariable':0.1,
						}
					},
					#'BrianingDebugVariable':0.1,
					'LeakingMonitorIndexIntsList':[0,1]
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

MyLeaker['/-Populations/|Default'].view(
	).pyplot()
#print(MyLeaker['/-Populations/|Default/-Interactions/|/'].BrianedSynapsesVariable.J[:])
SYS.matplotlib.pyplot.show()
