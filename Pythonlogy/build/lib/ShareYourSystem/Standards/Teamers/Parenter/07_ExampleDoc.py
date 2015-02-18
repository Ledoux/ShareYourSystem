
#ImportModules
import ShareYourSystem as SYS

#define and team
MyTeamer=SYS.TeamerClass(
	).command(
		'&Children',
		(
			'array',
			[
				['$First','$Second'],
				{
					'MyInt':0
				}
			]
		)
	)

#print
print('MyTeamer is ')
SYS._print(MyTeamer)