
#ImportModules
import ShareYourSystem as SYS

#Definition of a Familiarizer instance
MyFamiliarizer=SYS.FamiliarizerClass(
	).familiarize(
		'Children'
	).command(
		['Children'],
		
	)

#print
print('MyFamiliarizer is ')
SYS._print(MyFamiliarizer)

