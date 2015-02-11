
#ImportModules
import ShareYourSystem as SYS

#Definition a Getter
MyGetter=SYS.GetterClass()
MyGetter.MyInt=1
		
#print
print('Get the MyInt returns '+str(MyGetter['MyInt']))

#print
print('Get the MyStr returns '+str(MyGetter['MyStr']))

