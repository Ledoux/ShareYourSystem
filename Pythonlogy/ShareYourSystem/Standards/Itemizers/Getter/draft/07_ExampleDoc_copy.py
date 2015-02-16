
#ImportModules
import ShareYourSystem as SYS

#Definition a Getter
MyGetter=SYS.GetterClass()
MyGetter.MyInt=0
MyGetter.MyStr="hello"

#print
print('MyGetter.__getitem__(["MyInt","MyStr"]) is ')
SYS._print(MyGetter.__getitem__(["MyInt","MyStr"]))

