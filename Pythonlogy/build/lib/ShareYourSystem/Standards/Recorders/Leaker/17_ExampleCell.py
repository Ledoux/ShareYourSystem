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
					#'LeakingThresholdVariable':'#scalar:V>-50*mV',
					'LeakingThresholdVariable':-50.,
					'LeakingResetVariable':'#scalar:V=-70*mV',
					'-Interactions':{
						'|/':{
							'BrianingDebugVariable':100,
							'LeakingWeigthVariable':[[0.,0.],[0.,0.]],
							'LeakingInteractionStr':"Spike",
							'LeakingPlasticVariable':"J+=(((V_post+60.*mV)/volt)+((1.+1.)/2.)*J)",
							#'LeakingPlasticVariable':"J-=0.5*J",
							'RecordingLabelVariable':[1,2]
						}
					},
					'RecordingLabelVariable':[0,1],
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

#MyLeaker.view(
#	).pyplot(
#	)

MyLeaker['/-Populations/|P'].view(
	).pyplot(
	)

SYS.matplotlib.pyplot.show()

#/###################/#
# Print
#

#print
print('MyLeaker is ')
SYS._print(MyLeaker) 


