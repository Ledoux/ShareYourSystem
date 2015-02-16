
#ImportModules
import ShareYourSystem as SYS

#Define
MyGetter=SYS.GetterClass()
MyGetter.MyInt=1
		
#print
print('MyGetter[{"GetKeyVariable":"MyInt"}] is ')
SYS._print(MyGetter[{"GetKeyVariable":"MyInt"}])

#map get
MyGetter['map*get'](
	'FirstChildGetter',
	'SecondChildGetter',
	'FirstChildItemizer'
)

#print
print('get only the child getter gives')
SYS._print(
	MyGetter[
		{
			'ConditionTuplesList':
			[
				('__class__',SYS.operator.eq,SYS.GetterClass)
			]
		}
	]
)