#ImportModules
import ShareYourSystem as SYS

#Definition of a Packager instance and module
MyPackager=SYS.PackagerClass(
	).package(
		'ShareYourSystem.Standards.Interfacers.Printer'	
	)

#Definition the AttestedStr
print('MyPackager'+SYS._str(MyPackager))


