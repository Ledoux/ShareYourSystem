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

#/###################/#
# View
#

MyLeaker['/-Populations/|Default'].view(
	).pyplot()
SYS.matplotlib.pyplot.show()

#/###################/#
# Print
#

#Definition the AttestedStr
print('MyLeaker is ')
SYS._print(MyLeaker) 


