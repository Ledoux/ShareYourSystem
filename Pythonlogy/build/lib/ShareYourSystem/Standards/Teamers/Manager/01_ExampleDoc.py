#ImportModules
import ShareYourSystem as SYS

#Define and manage
MyManager=SYS.ManagerClass(
	).manage(
		{
			"$update":{
			'First':SYS.FamiliarizerClass()
			}
		}
	)

#Set with a setitem access
MyManager['$Second']=SYS.FamiliarizerClass()

#Print
print('MyManager is ')
SYS._print(MyManager)