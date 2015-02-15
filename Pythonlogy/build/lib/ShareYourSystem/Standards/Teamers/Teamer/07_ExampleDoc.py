
#ImportModules
import ShareYourSystem as SYS

#define and team
MyTeamer=SYS.TeamerClass(
	).command(
		'*Children',
		map(
			lambda __ChildKeyStr:
			(
				__ChildKeyStr,
				{
					'MyInt':0
				}
			),
			['$First','$Second']
		)	
	)

#define and team
MyTeamer=SYS.TeamerClass(
	)['produce*Children'](
		['First','Second'],
		{
			'MyInt':0
		}
	)

#print
print('MyTeamer is ')
SYS._print(MyTeamer)