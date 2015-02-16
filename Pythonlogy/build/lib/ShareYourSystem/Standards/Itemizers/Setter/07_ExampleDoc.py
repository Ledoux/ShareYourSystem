#ImportModules
import ShareYourSystem as SYS
import collections

#Define and set child setters in a child dict
MySetter=SYS.SetterClass(
	)['set'](
		'MyDict',
		collections.OrderedDict(
			{
			'FirstSetter':SYS.SetterClass(),
			'SecondSetter':SYS.SetterClass()
			}
		)
	).set(
		'all*MyDict',
		{
			'MyStr':"hello",
			'MyInt':0
		}
	)


#print
print('MySetter is ')
SYS._print(MySetter)
