
#ImportModules
import ShareYourSystem as SYS

#define structure
MyParenter=SYS.ParenterClass(
	).get(
		'/-Children/|Erwan/-GrandChildren',
		
	).parent(_DownBool=True)

#print
print('MyParenter is ')
SYS._print(MyParenter)

#define structure
MyParenter=SYS.ParenterClass(
	).get(
		'/-Children/|Erwan/-GrandChildren',
		
	)['/-Children/|Erwan/-GrandChildren'].parent(_UpBool=True)

#print
print('MyParenter is ')
SYS._print(MyParenter)
