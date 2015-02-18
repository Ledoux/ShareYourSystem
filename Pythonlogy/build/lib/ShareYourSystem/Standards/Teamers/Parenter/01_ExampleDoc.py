#ImportModules
import ShareYourSystem as SYS

#define structure
MyParenter=SYS.ParenterClass(
	).get(
		'/&Children/$Loup'
	)

#print
print('MyParenter is ')
SYS._print(MyParenter)

#get faster the parent
print("Get the parent of MyParenter['/&Children/$Loup'] gives ")
SYS._print(MyParenter['/&Children/$Loup']['^'])