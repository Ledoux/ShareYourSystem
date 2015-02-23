#ImportModules
import ShareYourSystem as SYS

a=SYS.ParenterClass().set(
		'MyDict.__setitem__',
		['#direct:u',4]
	)

print(a.MyDict)


"""
#define structure
MyParenter=SYS.ParenterClass(
	).command(
		'/&Children/$Child/&GrandChildren',
		('.../--^','#call:parent')
	)

#get faster the top parent
'''
MyParenter['/&Children/$Child/&GrandChildren'].set(
	'/Top/MyDict.__setitem__',
	{
		'#set':['ManagementKeyStr','>>self']
	}
)
'''

MyParenter['/&Children/$Child/&GrandChildren'].set(
	'MyDict.__setitem__',
	['u',3]
)	
"""

#print
'''
print('MyParenter.MyDict is ')
SYS._print(MyParenter.MyDict)
'''

