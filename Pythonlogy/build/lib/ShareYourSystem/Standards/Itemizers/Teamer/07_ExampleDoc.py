
#ImportModules
import ShareYourSystem as SYS

#define
class ChildrenClass(SYS.TeamerClass):pass

#define
MyTeamer=SYS.TeamerClass(
	).team(
		'Children',
		{
			'MyInt':0
		},
		_AfterSetVariable={
			'MyStr':"hello"
		}
	)

#print
print("MyTeamer is ")
SYS._print(MyTeamer)


