#ImportModules
import ShareYourSystem as SYS

#Definition of a Simulater instance
MyTracer=SYS.TracerClass(
	).mapSet(
		{
			'FirstArray':SYS.numpy.array([[1,2,5,6],[3,5,7,8]]),
			'SecondArray':SYS.numpy.array([[0.1,0.6,0.4,10]]),
			'-Traces':{
				'|*FirstArray':{},
				'|*SecondArray':{},
			}
		}
	).record(
	)
		
#Define
print('MyTracer is ')
SYS._print(MyTracer)

#Define
print("MyTracer['/-Traces/|*FirstArray'] is ")
SYS._print(MyTracer['/-Traces/|*FirstArray'].TracedInitFloatsArray)



