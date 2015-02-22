
#ImportModules
import ShareYourSystem as SYS

#Definition a Getter
MyGetter=SYS.GetterClass()
MyGetter.MyInt=1
		
#print
print("MyGetter['MyFloat'] is ")
print(MyGetter['MyFloat'])

#print
print("MyGetter['MyObject'] is ")
print(MyGetter['MyObject'])

#print
print('MyGetter is ')
SYS._print(MyGetter)

