
#ImportModules
import ShareYourSystem as SYS

#Define and set a dict
MySetter=SYS.SetterClass(
	).set(
		{
			'#set':"MyStr"
		},
		"hello"
	)

#Define and set a dict
MySetter.set(
		"MyDict",
		{'#set':{'MyInt':0}}
	)

#Define and set a dict
MySetter.set(
		"MyCloneStr",
		{'#get':'MyStr'}
	)

#Define and set a dict
MySetter.set(
		"MyList",
		{'#map:get':['MyStr','MyInt']}
	)

#print
print('MySetter is ')
SYS._print(MySetter)
