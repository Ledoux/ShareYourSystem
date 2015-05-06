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
					#'LeakingThresholdVariable':[-55.,-52.5],
					#'LeakingThresholdVariable':{
					#	'MethodsList':[
					#		SYS.Leaker.detectThreshold
					#	],
					#	'ThresholdVariable':[-55.,-52.5,-50.]
					#},
					#'LeakingResetVariable':'#scalar:V=-70*mV',
					'LeakingResetVariable':-70.,
					'-Interactions':{
						'|/':{
							'BrianingDebugVariable':100,
							'LeakingWeigthVariable':[[0.,0.],[-2.,0.]],#[[0.,-0.01],[0.,0.]]
							'LeakingInteractionStr':"Spike"
						}
					},
					'BrianingMonitorIndexIntsList':[0,1]
					#'BrianingDebugVariable':100
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


