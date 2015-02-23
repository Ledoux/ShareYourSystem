
#ImportModules
import ShareYourSystem as SYS

#Define
MyConditioner=SYS.ConditionerClass(
	).get(
		'MyList'
	).set(
		'MyList.append',
		{
			'#set':[4]
		}
	)

#print
print('MyConditioner is')
SYS._print(MyConditioner)

