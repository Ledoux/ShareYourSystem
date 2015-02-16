
#ImportModules
import ShareYourSystem as SYS

#Define
MyConditioner=SYS.ConditionerClass()
MyConditioner.MyInt=1
		
#print
print('MyConditioner[{"GetKeyVariable":"MyInt"}] is ')
SYS._print(MyConditioner[{"GetKeyVariable":"MyInt"}])

#map get
MyConditioner['map*get'](
	'FirstChildConditioner',
	'SecondChildConditioner',
	'FirstChildItemizer'
)

#get
MyConditioner.get(
		{
			'ConditionTuplesList':
			[
				('DictKeyStr',str.startswith,'First'),
				(type,SYS.operator.eq,SYS.ConditionerClass)
			]
		}
	)

#print
print('get only the FirstChildConditionner gives')
SYS._print(MyConditioner.GettedValueVariable)

