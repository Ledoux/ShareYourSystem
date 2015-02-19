
#ImportModules
import ShareYourSystem as SYS

#Define
MyGetter=SYS.GetterClass()
MyGetter.MyInt=1
		
#print
print('MyGetter[{"GetKeyVariable":"MyInt"}] is ')
SYS._print(MyGetter[{"GetKeyVariable":"MyInt"}])

#print
print('MyGetter[{"SetKeyVariable":"MyDict"}] is ')
SYS._print(MyGetter[{"SetKeyVariable":"MyDict"}])
