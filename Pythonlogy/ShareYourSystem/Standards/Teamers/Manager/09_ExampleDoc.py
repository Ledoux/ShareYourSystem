
#ImportModules
import ShareYourSystem as SYS

#define and get two children
MyTeamer=SYS.TeamerClass(
	).array(
		['&Neurons/$First','&Neurons/$Second']
	).command(
		'&Clients/$First',
		(
			'point',
			[
				'/^/&Neurons/$Second',
				'/&Connections/'
			]
		)
	)

#print
print('MyTeamer is ')
SYS._print(MyTeamer)

