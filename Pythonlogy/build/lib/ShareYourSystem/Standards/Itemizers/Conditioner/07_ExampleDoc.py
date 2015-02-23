
#ImportModules
import ShareYourSystem as SYS

#Define
MyConditioner=SYS.ConditionerClass()
		
#map get
MyConditioner['#map:get'](
	'FirstChildConditioner',
	'SecondChildConditioner',
	'FirstChildItemizer'
)

#get with the explicit key str
MyConditioner.get(
		{
			'#if':
			[
				(type,SYS.operator.eq,SYS.ConditionerClass),
				('DictKeyStr',str.startswith,'#direct:First'),
				SYS.GetClass(lambda self:'Child' in self['DictKeyStr']),			
			]
		}
	)


#print
print('get only the FirstChildConditionner gives')
SYS._print(MyConditioner.GettedValueVariable)
