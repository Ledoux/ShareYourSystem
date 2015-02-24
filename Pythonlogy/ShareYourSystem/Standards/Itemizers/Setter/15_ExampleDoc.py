
#ImportModules
import ShareYourSystem as SYS

#Define and set a dict
MySetter=SYS.SetterClass(
	).set(
		'set',
		{
			'#value':('MyInt',0)
		}
	)

#print
print('MySetter is ')
SYS._print(MySetter)