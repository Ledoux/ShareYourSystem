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

#print the Setter that has setted 
print('MySetter.ChildSetter.DictDeriveSetter is ')
SYS._print(MySetter.ChildSetter.DictDeriveSetter)