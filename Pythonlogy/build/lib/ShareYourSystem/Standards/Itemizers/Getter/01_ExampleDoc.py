
#ImportModules
import ShareYourSystem as SYS

#Define
MyGetter=SYS.GetterClass()

#set	
MyGetter.MyInt=1

#print an attribute get
print('Get "MyInt" returns '+str(MyGetter['MyInt']))

#print a method get
print('Get "itemize" returns '+SYS._str(MyGetter['itemize']))

#print a direct non str get
YourGetter=SYS.GetterClass()
YourGetter.MyStr="hello"
print('Get YourGetter returns '+SYS._str(MyGetter[YourGetter]))

#print a direct str get
print('Get <Direct>salut returns '+SYS._str(MyGetter["<Direct>salut"]))
