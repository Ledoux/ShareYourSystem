#ImportModules
import ShareYourSystem as SYS
import collections

#Define and automatically set in a child setter
MySetter=SYS.SetterClass(
	).set(
		'MyChildSetter',
		{
			'MyStr':"hello"
		}
	)

#print
print('MySetter is ')
SYS._print(MySetter)