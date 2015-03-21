#ImportModules
import ShareYourSystem as SYS

#Define
MyMoniter=SYS.MoniterClass(
	).mapSet(
		{
			'FirstArray':SYS.numpy.array([[1,2,5,6],[3,5,7,8]]),
			'SecondArray':SYS.numpy.array([[1,2,5,6],[3,5,7,8]]),
			'-Traces':{
				'|*FirstArray':{
					'-Samples':{
								'|Run':{
									'MoniteringLabelIndexIntsArray':[0,1]
								}
							}
				}
			}
		}
	).record(
	)
		
#Define
print('MyMoniter is ')
SYS._print(MyMoniter)

#print
print(MyMoniter['/-Traces/|*FirstArray/-Samples/|Run'].MoniteredTraceFloatsArray)
