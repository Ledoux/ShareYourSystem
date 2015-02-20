
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


#get a dict
"""
MyGetter.get(
	{
		"SetKeyVariable":"MyDict",
		'MyStr':"hello"
	}
)

#init
ChildGetter=SYS.GetterClass()
ChildGetter.SetKeyVariable="MyGetter"

#get an instance Getter
MyGetter.get(
	ChildGetter
)

#print
print('MyGetter is ')
SYS._print(MyGetter)
"""