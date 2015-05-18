
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
					'LeakingUnitsInt':1,
					'LeakingSymbolPrefixStr':'r',
					'-Inputs':{
						'|External':{
							'LeakingWeigthVariable':'#custom:1.*mV*cos(2.*pi*t*0.1/ms)'
						}
					},
					'LeakingMaxBool':True
					#'BrianingDebugVariable':100
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
	).show(
	)

#/###################/#
# Print
#

#print
print('MyLeaker is ')
SYS._print(MyLeaker) 



