
#ImportModules
import ShareYourSystem as SYS

#define and parent from the top
MyParenter=SYS.ParenterClass(
	).get(
		'/&Children/$Aurelie/&GrandChildren/$Anton'
	).parent(
		_DownBool=True
	)

#print
print('MyParenter is ')
SYS._print(MyParenter)

#define and parent from the ground
MyParenter=SYS.ParenterClass(
	)[
		'/&Children/$Aurelie/&GrandChildren/$Anton'
	].parent(
		_UpBool=True
	)

#print
print('MyParenter is ')
SYS._print(MyParenter)