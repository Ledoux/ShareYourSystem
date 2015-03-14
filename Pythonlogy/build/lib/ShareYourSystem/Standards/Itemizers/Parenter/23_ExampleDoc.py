#ImportModules
import ShareYourSystem as SYS

#define structure
MyParenter=SYS.ParenterClass(
	)['#map@set'](
		[
			(
				'-Outlets',
				[
					('|A',{
							'MyStr':"hello"
						})
				]
			)
		]
	)

#print
print('MyParenter is ')
SYS._print(MyParenter)


