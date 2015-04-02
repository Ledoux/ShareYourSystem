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
							#'LeakingWeigthVariable':'#scalar:3.*mV',
							'LeakingWeigthVariable':5.,
							#'LeakingWeigthVariable':5.*SYS.brian2.mV
							#'LeakingWeigthVariable':[1.,3.],
							#'LeakingWeigthVariable':SYS.getKrenelFloatsArray(),
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

MyLeaker['/-Populations/|Default'].pyplot()
SYS.matplotlib.pyplot.show()
