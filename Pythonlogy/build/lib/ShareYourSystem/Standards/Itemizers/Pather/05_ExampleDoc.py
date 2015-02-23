
#ImportModules
import ShareYourSystem as SYS

#Explicit expression
MyPather=SYS.PatherClass(
	).get(
		'ChildPather'
	)

MyPather.ChildPather.set(
		'/</MyDict.__setitem__',
		[
			'#direct:MyChildPather',
			'>>self'
		]
	)

#print
print('MyPather is ')
SYS._print(MyPather)


