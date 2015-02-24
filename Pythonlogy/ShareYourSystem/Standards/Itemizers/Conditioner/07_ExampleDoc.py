
#ImportModules
import ShareYourSystem as SYS

#Define
MyConditioner=SYS.ConditionerClass()
		
#map get
MyConditioner['#map@get'](
	'FirstChildConditioner',
	'SecondChildConditioner',
	'FirstChildItemizer'
)

#get with the explicit key str
MyConditioner.get(
		{
			'#filter':
			[
				(type,SYS.operator.eq,SYS.ConditionerClass),
				('SetKeyStr',str.startswith,'#direct:First'),
				SYS.GetClass(lambda self:'Child' in self['SetKeyStr']),			
			],
			'#scan':'__dict__.values'
		}
	)


#print
print('get only the FirstChildConditionner gives')
SYS._print(MyConditioner.GettedValueVariable)
