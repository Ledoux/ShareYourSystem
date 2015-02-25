#ImportModules
import ShareYourSystem as SYS

#define structure
MyParenter=SYS.ParenterClass(
	).get(
		'/&Children/$Aurelie/&GrandChildren/$Loup'
	).command(
		['TeamDict.values','ManagementDict.values'],
		[
			(
				'ParentingTriggerVariable',
				{'DeepInt':'#get:>>len(self.ParentedTotalPathStr.split("/"))'}
			),
			('parent',[])
		],
		_AfterWalkBool=True,
		_BeforeSelfBool=True
	)

#print
print('MyParenter is ')
SYS._print(MyParenter)
