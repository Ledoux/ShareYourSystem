
#ImportModules
import ShareYourSystem as SYS

MySetter=SYS.SetterClass(
	).set(
		'MyList',
		{
			'#value:#lambda':{
				'MyStr':'#__Variable Erwan'
			},
			'#map':['Salut','Au revoir']
		}
	)

#print
print('MySetter is ')
SYS._print(MySetter)

MySetter=SYS.SetterClass(
	).set(
			'HelloStr',
			'Hello'
	).set(
		'ByeStr',
		'Bye'
	).set(
			'MyList',
			{
				'#value:#lambda':{
					'MyStr':'#__Variable Erwan'
				},
				'#map@get':['HelloStr','ByeStr']
			}
		)

#print
print('MySetter is ')
SYS._print(MySetter)