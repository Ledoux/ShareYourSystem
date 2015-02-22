#ImportModules
import ShareYourSystem as SYS

#define structure
MyParenter=SYS.ParenterClass(
	).get(
		'/&Children/$Aurelie/&GrandChildren/$Loup'
	).command(
				['TeamDict.values','ManagementDict.values'],
				('parent',[]),
				_AfterWalkBool=True
			)

#get faster the parent
'''
print("Get the parent of MyParenter['/&Children/$Loup'] gives ")
SYS._print(MyParenter['/&Children/$Loup']['^'])
'''

#print
print('MyParenter is ')
SYS._print(MyParenter)
