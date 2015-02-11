
#ImportModules
import ShareYourSystem as SYS

#define and team
MyManager=SYS.ManagerClass()

#Note that just a get will create a Manager
print("MyManager['$First'] is ")
SYS._print(MyManager['$First'])

#print
print('MyManager is ')
SYS._print(MyManager)

