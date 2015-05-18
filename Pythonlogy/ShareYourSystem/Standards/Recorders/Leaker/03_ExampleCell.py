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
				'|Sensor':{
					'LeakingUnitsInt':2,
					'LeakingSymbolPrefixStr':'r',
					'-Inputs':{
						'|Command':{
							#'LeakingWeigthVariable':'#scalar:3.*mV',
							#'LeakingWeigthVariable':5.,
							#'LeakingWeigthVariable':5.*SYS.brian2.mV
							#'LeakingWeigthVariable':[1.,3.],
							#'LeakingWeigthVariable':SYS.getKrenelFloatsArray(),
							#'LeakingWeigthVariable':'#equation:5.*mV*(1.+tanh(10.*(t-250.*ms)/ms))',
							#'LeakingWeigthVariable':'#custom:#clock:10*ms:'''
							#	change=int(t>250*ms)
							#	#SymbolStr:5.*mV*change
							#''',
							#'LeakingWeigthVariable':'#custom:5.*mV*(ms/(t+1*ms))',
							#'LeakingWeigthVariable':'#custom:#clock:200*ms:5.*mV*(t==200*ms)*(i==0)',
							#'LeakingWeigthVariable':'#custom:#clock:200*ms:5.*mV*(t==200*ms)*(i==0)',
							'LeakingWeigthVariable':(
								'#custom:#clock:100*ms',
								[
									'5.*mV*int(t==200*ms)',
									'-2.*mV*int(t==100*ms)'
								]
							),
							#'LeakingWeigthVariable':(
							#	'#network:#clock:200*ms',
							#	lambda _ActivityQuantity,_TimeQuantity:
							#	5.*SYS.brian2.mV 
							#	if _TimeQuantity==200.*SYS.brian2.ms
							#	else 0.*SYS.brian2.mV
							#),
							#'LeakingWeigthVariable':(
							#	'#network:#clock:1*ms',
							#	lambda _ActivityQuantity,_TimeQuantity:
							#	SYS.scipy.stats.norm.rvs(size=2)*SYS.brian2.mV
							#),
							'RecordingLabelVariable':[0,1]
						}
					},
					'RecordingLabelVariable':[0,1]
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

#MyLeaker[
#		'/-Populations/|Sensor/-Traces/|*I_Command/-Samples/|Default'
#	].view(
#	).pyplot(
#	)

#MyLeaker[
#		'/-Populations/|Sensor/-Traces/|*U/-Samples/|Default'
#	].view(
#	).pyplot(
#	)

MyLeaker[
		'/-Populations/|Sensor'
	].view(
	).pyplot(
	)
SYS.matplotlib.pyplot.show()

#/###################/#
# Print
#

#Definition the AttestedStr
print('MyLeaker is ')
SYS._print(MyLeaker) 



