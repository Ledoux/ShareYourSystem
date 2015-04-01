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
					'LeakingTimeConstantVariable':'#scalar:20.*ms',
					'-Inputs':{
						'|Default':{
							#'LeakingInputExternalVariable':SYS.getKrenelFloatsArray()
							#'LeakingInputExternalVariable':5.
							'LeakingInputExternalVariable':'#scalar:5.*mV'
						}
					}
				},
				#'|Population':{
				#	'LeakingUnitsInt':3,
				#	'LeakingTimeConstantFloat':20.
				#}
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
