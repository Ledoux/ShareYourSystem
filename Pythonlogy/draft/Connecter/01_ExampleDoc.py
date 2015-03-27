
#ImportModules
import ShareYourSystem as SYS

#define and get two children
MyConnecter=SYS.ConnecterClass(
	).array(
		[['-Children'],['|Aurelie','|Erwan']]
	).set(
		'/-Children/|Erwan/-Outlets',
		{		
			'|EtoI':{
				'PointingToGetVariable':'/^/^/^/|Aurelie/-PreConnections/'
			}
		}
	)['?v']

#print
print('MyConnecter is ')
SYS._print(MyConnecter)

