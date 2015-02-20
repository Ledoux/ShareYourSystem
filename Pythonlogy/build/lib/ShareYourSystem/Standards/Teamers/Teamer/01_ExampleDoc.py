
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
		SYS.PointerClass()
	)

#With a set
MyTeamer['&Clients']=SYS.PointerClass()

#print
print('MyTeamer is ')
SYS._print(MyTeamer)

#Shortcut for getting all the teamed instances
print("MyTeamer['$'] is ")
SYS._print(MyTeamer['$'])

