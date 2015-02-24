
#ImportModules
import ShareYourSystem as SYS

#Define
MyGetter=SYS.GetterClass()

#set	
MyGetter.MyInt=1
MyGetter.HelloStr="hello"
MyGetter.FirstRedirectStr="HelloStr"
MyGetter.SecondRedirectStr="FirstRedirectStr"

#print an attribute get
print('Get "MyInt" returns '+str(MyGetter['MyInt']))

#print a method get
print('Get "itemize" returns '+SYS._str(MyGetter['itemize']))

#print a direct non str get
YourGetter=SYS.GetterClass()
print('Get YourGetter returns '+SYS._str(MyGetter[YourGetter]))

#print a direct str get
print('Get #direct:salut returns '+SYS._str(MyGetter["#direct:salut"]))

#print a one level recursive get 
print('Get #get:FirstRedirectStr returns '+SYS._str(MyGetter["#get:FirstRedirectStr"]))

#print a two levels recursive get 
print('Get #get:#get:SecondRedirectStr returns '+SYS._str(
	MyGetter["#get:#get:SecondRedirectStr"])
)

#print a method get
print('Get GetClass(lambda self:self.MyInt+2) returns '+SYS._str(
	MyGetter[SYS.GetClass(lambda self:self.MyInt+2)]))

#bound
SYS.GetterClass.printHello=lambda _SelfVariable:SYS._print(_SelfVariable.HelloStr)
print("Doing MyGetter['#call:printHello'] gives ")
MyGetter['#call:printHello']
