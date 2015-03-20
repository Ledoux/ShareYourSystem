
#ImportModules
import ShareYourSystem as SYS

#Definition an instance
MyRecorder=SYS.RecorderClass(
	).mapSet(
		{
			''
			'-Traces':{
				'|*v':{
				}
			},
			'-Events':{

			}
		}
	).record(
	)

#Definition the AttestedStr
print('MyRecorder is ')
SYS._print(MyRecorder)


