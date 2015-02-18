#ImportModules
import ShareYourSystem as SYS

#define structure
MyParenter=SYS.ParenterClass(
	).set('MyStr','hello')

#parent by a command (CommandingWalkBool is set to True by default in Parenter)
MyParenter['/&Children/$Child/&GrandChildren'].command(
		'^',
		('parent',[])
	)

#print
print('MyParenter is ')
SYS._print(MyParenter)

#get faster the top parent
print("Get the top parent of MyParenter['/&Children/$Child/&GrandChildren'] gives ")
SYS._print(MyParenter['/&Children/$Child/&GrandChildren']['Top'])