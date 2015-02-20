
#ImportModules
import ShareYourSystem as SYS

#Define
MyConditioner=SYS.ConditionerClass()
		
#map get
MyConditioner['map*get'](
	'FirstChildConditioner',
	'SecondChildConditioner',
	'FirstChildItemizer'
)

#get with the explicit key str
MyConditioner.get(
		{
			'ConditionTuplesList':
			[
				('DictKeyStr',str.startswith,'<Direct>First'),
				(type,SYS.operator.eq,SYS.ConditionerClass)
			]
		}
	)

#print
print('get only the FirstChildConditionner gives')
SYS._print(MyConditioner.GettedValueVariable)

#get with the short str
MyConditioner.get(
		{
			'#if':
			[
				('DictKeyStr',str.startswith,'<Direct>Second'),
				(type,SYS.operator.eq,SYS.ConditionerClass)
			]
		}
	)

#print
print('get only the SecondChildConditionner gives')
SYS._print(MyConditioner.GettedValueVariable)

