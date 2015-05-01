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
				'|P':{
					'LeakingUnitsInt':2,
					'LeakingSymbolPrefixStr':'r',
					'LeakingMonitorIndexIntsList':[0,1],
					'-Interactions':{
						'|/':{
							#'BrianingDebugVariable':10,
							'LeakingWeigthVariable':[[0.,-2.],[0.,0.]],
							'LeakingDelayVariable':5., 
						}
					}
				}
			}
		}
	).leak(
	).simulate(
		50.
	)

#/###################/#
# View
#

MyLeaker.view(
	).pyplot(
	)

SYS.matplotlib.pyplot.show()

#/###################/#
# Print
#

#print
print('MyLeaker is ')
SYS._print(MyLeaker) 

