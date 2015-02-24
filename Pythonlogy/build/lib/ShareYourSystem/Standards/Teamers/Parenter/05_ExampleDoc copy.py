#ImportModules
import ShareYourSystem as SYS


#define structure
MyParenter=SYS.ParenterClass(
	).command(
		'/&Children/$Aurelie/&GrandChildren/$Loup',
		('.../--^','#call:parent')
	)


#get faster the top parent
a=MyParenter['/&Children/$Aurelie/&GrandChildren/$Loup']

#SYS._print(a)

SYS._print('\n\n\nRRRRRR\n\n')


a.set(
	'/Top/MyDict.__setitem__',
	{
		'#map@get':['ManagementKeyStr','>>self']
	}
)


#print
print('MyParenter.MyDict is ')
SYS._print(MyParenter.MyDict)

