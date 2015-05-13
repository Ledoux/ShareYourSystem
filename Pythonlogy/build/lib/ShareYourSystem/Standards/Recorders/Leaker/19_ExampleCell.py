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
					'LeakingUnitsInt':100,
					'LeakingTransferVariable':'mV*tanh((#CurrentStr)/mV)',
					'-Interactions':{
						'|/':{
							'LeakingWeigthVariable':'#array',
							'LeakingEigenBool':True
						}
					},
					#'LeakingGlobalBool':True,
					'RecordingLabelVariable':[0,1,2]
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
	).show()

#/###################/#
# Print
#

#print
print('MyLeaker is ')
SYS._print(MyLeaker) 


