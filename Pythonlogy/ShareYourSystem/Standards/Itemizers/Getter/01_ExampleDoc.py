
#ImportModules
import ShareYourSystem as SYS

#Define
MyGetter=SYS.GetterClass()

#set	
MyGetter.MyInt=1

#print
print('Get "MyInt" returns '+str(MyGetter['MyInt']))

#print
print('Get "MyStr" returns '+str(MyGetter['MyStr']))

#print
print('Get "itemize" returns '+SYS._str(MyGetter['itemize']))
