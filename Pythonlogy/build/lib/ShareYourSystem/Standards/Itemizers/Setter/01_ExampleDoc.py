
#ImportModules
import ShareYourSystem as SYS

#Define and set a simple Int
MySetter=SYS.SetterClass(
	).set(
		'MyInt',
		0
	)

#print
print('MySetter is ')
SYS._print(MySetter)

#We can call a bound method and the value of the set is the Liarg
MySetter.set(
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

#Note that we can call also a direct explicit function
MySetter.get(
		'MyList'
	)

MySetter.set(
		MySetter.MyList.append,
		[3]
	)

#print
print('MySetter is ')
SYS._print(MySetter)

