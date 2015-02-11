#ImportModules
import ShareYourSystem as SYS

#Define and set
MySetter=SYS.SetterClass(
	).set(
		SYS.MapListClass(
			[
				('MyInt',0),
				('MyStr',"hello")
			]
		)
	)
		
#print
print('MySetter is ')
SYS._print(MySetter)
