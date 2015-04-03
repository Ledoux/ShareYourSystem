#/###################/#
# Import modules
#

#ImportModules
import ShareYourSystem as SYS

#/###################/#
# Build the model
#

#Definition an instance
MyLeaker=SYS.LeakerClass(
	).mapSet(
		{
			'LeakingUnitsInt':3,
			#'LeakingTimeVariable':'#scalar:20.*ms',
			#'LeakingTimeVariable':20.,
			#'LeakingTimeVariable':20.*SYS.brian2.ms,
			#'LeakingTimeVariable':[10.,20.,10.],

			'RecordingLabelVariable':[0,1]
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

MyLeaker['/-Traces/|*U/-Samples/|Default'].pyplot()
#MyLeaker['/-Events/|Default'].pyplot()
#MyLeaker.pyplot()
SYS.matplotlib.pyplot.show()

