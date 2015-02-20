
#ImportModules
import ShareYourSystem as SYS

#Define
MyGetter=SYS.GetterClass()
MyGetter.MyInt=1
		
#print
print('MyGetter[{"GetVariable":"MyInt"}] is ')
SYS._print(MyGetter[{"GetVariable":"MyInt"}])

#print
print('MyGetter[{"#get":"MyInt"}] is ')
SYS._print(MyGetter[{"#get":"MyInt"}])

