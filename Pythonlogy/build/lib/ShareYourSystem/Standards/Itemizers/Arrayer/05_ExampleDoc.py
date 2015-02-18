
#ImportModules
import ShareYourSystem as SYS

#array original
MyArrayer=SYS.ArrayerClass(
	).array(
		["AArrayer","BArrayer"],
		[{'MyStr':"hello"},{}]
	)

#array identical
MyArrayer.array(
		["aArrayer","bArrayer"],
		{'MyInt':1}
	)

#Definition the AttestedStr
print('MyArrayer is ')
SYS._print(MyArrayer)

