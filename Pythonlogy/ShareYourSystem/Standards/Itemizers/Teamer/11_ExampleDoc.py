
#ImportModules
import ShareYourSystem as SYS

#define
MyTeamer=SYS.TeamerClass(
	).team(
		'Children',
		{
			'MyInt':0
		}
	).team(
		'Clients',
		{
			'MyStr':"hello"
		}
	)

#print
print("MyTeamer is ")
SYS._print(MyTeamer)





