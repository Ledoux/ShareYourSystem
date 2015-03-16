
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