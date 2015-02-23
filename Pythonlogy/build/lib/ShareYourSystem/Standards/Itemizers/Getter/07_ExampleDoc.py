
#ImportModules
import ShareYourSystem as SYS

#Define
MyGetter=SYS.GetterClass()
MyGetter.MyInt=1
MyGetter.MyStr="hello"
		
#print
print('MyGetter[{"#get":"MyInt"}] is ')
SYS._print(MyGetter[{"#get":"MyInt"}])

#print
print("MyGetter[{'#map:get':['MyStr','MyInt']}] is ")
SYS._print(MyGetter[{'#map:get':['MyStr','MyInt']}])

#print
print("MyGetter['#get:MyStr'] is ")
SYS._print(MyGetter['#get:MyStr'])

