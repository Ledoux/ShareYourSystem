
#ImportModules
import ShareYourSystem as SYS

#define and team
MyManager=SYS.ManagerClass(
	)['map*set'](
		{
			'$First':{
				'MyInt':0
			},
			'$Second':{
				'MyFloat':5.
			}
		}
	)


#print
print('MyManager is ')
SYS._print(MyManager)


