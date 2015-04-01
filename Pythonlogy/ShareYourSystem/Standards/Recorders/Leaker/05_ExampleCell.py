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
					'LeakingTimeVariable':'#scalar:20.*ms',
					'-Inputs':{
						'|Default':{
							#'LeakingWeigthVariable':SYS.getKrenelFloatsArray()
							#'LeakingWeigthVariable':5.
							'LeakingWeigthVariable':'#scalar:5.*mV'
						}
					},
					'-Interactions':{
						'|/':{
							'LeakingWeigthVariable':'#scalar:0.',
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
