#ImportModules
import ShareYourSystem as SYS

#define structure
MyParenter=SYS.ParenterClass(
	).get(
		'/-Children/|Aurelie/-GrandChildren/|Loup'
	).command(
		['TeamDict.values','ManagementDict.values'],
		[
			(
				'ParentingTriggerVariable',
				{'DeepInt':'#get:>>self[\'DeepInt\']+len(self.ParentedTotalPathStr.split("/"))'}
			),
			'#call:parent',
			('setSwitch',['parent']),
			'#call:parent',
		],
		_AfterWalkBool=True,
		_BeforeSelfBool=True
	)

#print
print('MyParenter is ')
SYS._print(MyParenter)

