
#ImportModules
import ShareYourSystem as SYS

#Define and set with #key dict for the KeyVariable
MySetter=SYS.SetterClass(
	).set(
		'MyStr',
		'HelloStr'
	).set(
		{'#key':"MyStr"},
		"hello"
	)

#Define and set with a #value dict for the ValueVariable
MySetter.set(
		"MyDict",
		{'#value':{'MyInt':0}}
	)

#Define and set with a #value:#get dict for the ValueVariable
MySetter.set(
		"MyCloneStr",
		{'#value:#get':'MyStr'}
	)

#Define and set with a #value:#map@get dict for the ValueVariable
MySetter.set(
		"MyList",
		{'#value:#map@get':['MyStr','MyInt','#direct:FooStr']}
	)

#print
print('MySetter is ')
SYS._print(MySetter)
