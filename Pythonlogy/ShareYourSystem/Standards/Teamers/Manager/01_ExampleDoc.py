#ImportModules
import ShareYourSystem as SYS

#Define and manage without specifying the value class 
#which is PointerClass if Teamer not imported else TeamerClass
MyManager=SYS.ManagerClass(
	).manage(
		#ManagingKeyStr
		'First'
	)

#Define and manage with specifying the Variable
MyManager.manage(
		#ManagingKeyStr
		'Second',
		#ManagingValueVariable
		SYS.TeamerClass()
	)

#Set with a setitem access
MyManager['$Third']=SYS.TeamerClass()


#Print
print('MyManager is ')
SYS._print(MyManager)