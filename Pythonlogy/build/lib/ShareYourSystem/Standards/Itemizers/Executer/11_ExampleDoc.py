
#ImportModules
import ShareYourSystem as SYS

#Just one translated word but that is getted
MyExecuter=SYS.ExecuterClass(
	)['#map@set'](
		[
			(
				'MyList',[]
			),
			(
				'MyList.extend',
				[
					{
						'#value:#lambda':{
							'MyStr':'#__Variable Erwan'
						},
						'#map':[
							'HelloStr',
							'ByeStr'
						]
					}
				]
			)
		]
	)

#print
print('MyExecuter is ')
SYS._print(MyExecuter)
