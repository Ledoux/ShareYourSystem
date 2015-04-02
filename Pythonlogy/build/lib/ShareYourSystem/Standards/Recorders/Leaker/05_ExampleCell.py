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
					'-Inputs':{
						'|Default':{
							#'LeakingWeigthVariable':SYS.getKrenelFloatsArray()
							#'LeakingWeigthVariable':5.
							#'LeakingWeigthVariable':'#scalar:5.*mV'
						}
					},
					'-Interactions':{
						'|/':{
							#'LeakingWeigthVariable':'#scalar:0.',
							#'LeakingWeigthVariable':'#scalar:-0.2',
							'LeakingWeigthVariable':[0.1,-0.2,0.5,0.8],
							#'LeakingWeigthVariable':[[0.1,-0.2],[0.5,0.8]],
							#'LeakingWeigthVariable':'#array',
							'NumscipyingStdFloat':0.1,
							#'BrianingDebugInt':50
						}
					},
					'BrianingDebugInt':100
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

MyLeaker['/-Populations/|Default'].pyplot()
#print(MyLeaker['/-Populations/|Default/-Interactions/|/'].BrianedSynapsesVariable.J[:])
SYS.matplotlib.pyplot.show()
