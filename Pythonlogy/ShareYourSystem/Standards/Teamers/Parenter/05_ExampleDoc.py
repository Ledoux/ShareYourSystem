#ImportModules
import ShareYourSystem as SYS

#define structure
MyParenter=SYS.ParenterClass(
	).command(
		'/&Children/$Child/&GrandChildren',
		('.../--^','#call:parent')
	)

#get faster the top parent
print("Get the top parent of MyParenter['/&Children/$Child/&GrandChildren'] gives ")
SYS._print(MyParenter['/&Children/$Child/&GrandChildren']['Top'])