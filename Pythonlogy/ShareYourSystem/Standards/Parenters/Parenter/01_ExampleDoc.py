#ImportModules
import ShareYourSystem as SYS

#Define and parent
MyParenter=SYS.ParenterClass(
	).parent(
		'FirstFamiliarizer',
		SYS.FamiliarizerClass()
	)

#Print
print('MyParenter is ')
SYS._print(MyParenter)