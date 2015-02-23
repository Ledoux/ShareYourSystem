
#ImportModules
import ShareYourSystem as SYS

#Define and append in a list
MyExecuter=SYS.ExecuterClass(
	).get(
		'MyList'
	).set(
		'MyList.append',
		{
			'#map:get':[6]
		}
	)

#print
print('MyExecuter is ')
SYS._print(MyExecuter)	
