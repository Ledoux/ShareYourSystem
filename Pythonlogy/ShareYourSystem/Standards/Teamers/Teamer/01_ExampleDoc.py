
#ImportModules
import ShareYourSystem as SYS

#define and team
MyTeamer=SYS.TeamerClass(
	).team(
		#TeamingKeyStr
		"Employees"
	)

#Define and team with specifying the Variable
MyTeamer.team(
		#TeamingKeyStr
		'Partners',
		#TeamingValueVariable
		SYS.TeamerClass()
	)

#With a set
MyTeamer['*Clients']=SYS.ManagerClass()

#print
print('MyTeamer is ')
SYS._print(MyTeamer)

