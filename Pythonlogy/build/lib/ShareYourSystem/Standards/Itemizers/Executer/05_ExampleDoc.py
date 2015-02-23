
#ImportModules
import ShareYourSystem as SYS

#Definition and update with an exec Str
MyExecuter=SYS.ExecuterClass(
	).get(
		'MyList'
	).set(
		'MyList.append',
		{
			'#set':[6]
		}
	)

#print
print('MyExecuter is ')
SYS._print(MyExecuter)	
