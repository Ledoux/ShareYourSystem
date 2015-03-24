#ImportModules
import ShareYourSystem as SYS

#array
MyArray=SYS.numpy.array([[1,2,5,6],[3,5,7,8]])

#Definition of a Tracer instance
MyTracer=SYS.TracerClass(
	).trace(
		MyArray
	)
		
#print
print('MyTracer is ')
SYS._print(MyTracer)

#print
print('MyTracer.TracedInitFloatsArray is ')
print(MyTracer.TracedInitFloatsArray)