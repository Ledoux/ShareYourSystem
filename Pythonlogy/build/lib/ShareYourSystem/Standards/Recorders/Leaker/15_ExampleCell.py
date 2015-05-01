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
					'-Inputs':{
						'|External':{
							'LeakingWeigthVariable':'#scalar:11*mV'
						}
					},
					'LeakingNoiseStdVariable':0.1,
					'-Interactions':{
						'|/':{
							'BrianingDebugVariable':100,
							'LeakingWeigthVariable':[[0.,-1.],[-2.,0.]],
							#'LeakingDelayVariable':5., #ms
							#'LeakingDelayVariable':[[0.,1.],[5.,0.]], #ms
						}
					}
					#'BrianingDebugVariable':100
				}
			}
		}
	).leak(
	).simulate(
		200.
	)

#/###################/#
# View
#

MyLeaker.view(
	).pyplot(
	)

#MyLeaker['/-Populations/|P'].view(
#	).pyplot(
#	)

SYS.matplotlib.pyplot.show()

#/###################/#
# Print
#

#print
print('MyLeaker is ')
SYS._print(MyLeaker) 

