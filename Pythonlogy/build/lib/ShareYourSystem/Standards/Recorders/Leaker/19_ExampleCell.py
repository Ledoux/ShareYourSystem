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
					'LeakingMonitorIndexIntsList':[0,1,2],
					'LeakingTransferVariable':'mV*tanh((#CurrentStr)/mV)',
					'-Interactions':{
						'|/':{
							'LeakingWeigthVariable':'#array',
						}
					},
					'LeakingGlobalBool':True
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


