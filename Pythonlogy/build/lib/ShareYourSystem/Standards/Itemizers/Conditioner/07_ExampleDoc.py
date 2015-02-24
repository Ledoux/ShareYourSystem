
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

#get with a filter on the __dict__ values
MyConditioner.get(
		{
			'#filter':
			[
				(type,SYS.operator.eq,SYS.ConditionerClass),
				('SetKeyStr',str.startswith,'#direct:First'),
				SYS.GetClass(lambda self:'Child' in self['SetKeyStr']),			
			],
			'#scan':'>>self.__dict__.values()'
		}
	)

#print
print('get only the FirstChildConditionner gives')
SYS._print(MyConditioner.GettedValueVariable)

#get with a filter on items in a dict
MyConditioner.set(
		'MyDict',
		{
			'FirstObject':SYS.ObjectClass(),
			'SecondObject':SYS.ObjectClass()
		}
	).get(
		{
			'#filter':
			[
				(0,str.startswith,'First')
				#(type,SYS.operator.eq,SYS.ConditionerClass),
				#('SetKeyStr',str.startswith,'#direct:First'),
				#SYS.GetClass(lambda self:'Child' in self['SetKeyStr']),			
			],
			'#scan':'>>self.MyDict.items()'
		}
	)

#print
print('get only the FirstObject gives')
SYS._print(MyConditioner.GettedValueVariable)
