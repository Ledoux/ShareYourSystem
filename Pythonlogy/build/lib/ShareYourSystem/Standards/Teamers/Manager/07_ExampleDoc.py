
#ImportModules
import ShareYourSystem as SYS

#define and get two children
MyManager=SYS.ManagerClass(
	)['#map@get']('$First','$Second')

MyManager['#each:$']=[
	{
		'MyInt':0
	},
	{
		'MyStr':"hello"
	}
]

#print
print('MyManager is ')
SYS._print(MyManager)


