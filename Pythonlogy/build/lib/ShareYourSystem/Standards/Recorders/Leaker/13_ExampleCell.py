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
					'LeakingSymbolPrefixStr':'V',
					'-Inputs':{
						'|Rest':{
							'LeakingWeigthVariable':'#scalar:-60*mV'
						},
						'|External':{
							'LeakingWeigthVariable':'#scalar:11*mV'
						}
					},
					'LeakingNoiseStdVariable':0.1,
					'LeakingThresholdVariable':'#scalar:V>-50*mV',
					'LeakingResetVariable':'#scalar:V=-70*mV',
					'-Interactions':{
						'|/':{
							'BrianingDebugVariable':100,
							'LeakingWeigthVariable':[[0.,-1.],[-2.,0.]],
							'LeakingInteractionStr':"Spike",
							#'LeakingDelayVariable':5., #ms
							#'LeakingDelayVariable':[[0.,1.],[5.,0.]], #ms
						}
					},
					'BrianingMonitorIndexIntsList':[0,1],
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



