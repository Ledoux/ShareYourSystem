#ImportModules
import ShareYourSystem as SYS

#define structure
MyParenter=SYS.ParenterClass(
	).set('MyStr','hello')

#parent then
MyParenter['/&Children/$Child/&GrandChildren'].walk(
		'^',
		('parent',[])
	)

#print
print('MyParenter is ')
SYS._print(MyParenter)

#get faster the top parent
print("Get the top parent of MyParenter['/&Children/$Child/&GrandChildren'] gives ")
SYS._print(MyParenter['/&Children/$Child/&GrandChildren']['Top'])