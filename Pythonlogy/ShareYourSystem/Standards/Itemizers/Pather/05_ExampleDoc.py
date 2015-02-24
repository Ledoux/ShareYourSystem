
#ImportModules
import ShareYourSystem as SYS

#Explicit expression
MyPather=SYS.PatherClass(
	).get(
		'ChildPather'
	)

MyPather.ChildPather.set(
		'/</IdIntsDict.__setitem__',
		(
			'#direct:MyChildPather',
			'/~/IdInt'
		)
	)

#print
print('MyPather is ')
SYS._print(MyPather)


