
#ImportModules
import ShareYourSystem as SYS

#define and get two children
MyConnecter=SYS.ConnecterClass(
	).array(
		[['-Children'],['|Aurelie','|Erwan']]
	).set(
		'-Outlets',
		{		
			'|EtoI':{
				'PointingToGetVariable':'/^/^/|I/-PreConnections'
			}
		}
	)

#print
print('MyConnecter is ')
SYS._print(MyConnecter)

