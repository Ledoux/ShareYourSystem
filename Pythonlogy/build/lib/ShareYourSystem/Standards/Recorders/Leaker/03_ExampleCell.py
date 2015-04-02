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
							'LeakingWeigthVariable':'#scalar:5.*mV',
							#'LeakingWeigthVariable':SYS.getKrenelFloatsArray(),
							#'LeakingWeigthVariable':5.	
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
