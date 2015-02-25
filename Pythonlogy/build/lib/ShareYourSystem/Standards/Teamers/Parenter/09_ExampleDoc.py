
#ImportModules
import ShareYourSystem as SYS

#define and get two children
MyParenter=SYS.ParenterClass(
	).get(
		'/&Children/$Aurelie/&GrandChildren/$Anton'
	).parent(
		_DownBool=True
	)


#print
print('MyParenter is ')
SYS._print(MyParenter)

