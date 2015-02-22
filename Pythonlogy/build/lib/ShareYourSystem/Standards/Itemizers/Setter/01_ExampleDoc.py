
#ImportModules
import ShareYourSystem as SYS

#Define and set
MySetter=SYS.SetterClass(
	).set(
		'MyInt',
		0
	).set(
		'get',
		'MyInt'
	)
		
#print
print('MySetter.GettedValueVariable is ')
SYS._print(MySetter.GettedValueVariable)

#we can set ... a set
MySetter.set(
		'set',
		('MyStr',"hello")
	)

#print
print('MySetter is ')
SYS._print(MySetter)
