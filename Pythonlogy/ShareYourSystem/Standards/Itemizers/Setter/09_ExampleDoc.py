#ImportModules
import ShareYourSystem as SYS
import collections

#Define and automatically set in a child setter
MySetter=SYS.SetterClass(
	).set(
		'ChildSetter',
		{
			'MyStr':"hello"
		}
	)

#print
print('MySetter is ')
SYS._print(MySetter)

#print the ChildSetter keystr with which it was setted
print('MySetter.ChildSetter.SetDeriveSetter is ')
SYS._print(MySetter.ChildSetter.SetDeriveSetter)

#print its setter
print("MySetter.ChildSetter['<'] is ")
SYS._print(MySetter.ChildSetter['<'])

