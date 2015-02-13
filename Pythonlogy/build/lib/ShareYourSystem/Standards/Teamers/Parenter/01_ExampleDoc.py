#ImportModules
import ShareYourSystem as SYS

#define structure
MyParenter=SYS.ParenterClass(
	).get(
		'/*Children/$Child/*GrandChildren/$GrandChild'
	).set('MyStr','hello')

#parent then
MyParenter['/*Children/$Child/*GrandChildren/$GrandChild'].parent(
		#ParentingTopGetVariable
		['MyStr']
	)

#print
print('MyParenter is ')
SYS._print(MyParenter)


