#ImportModules
import ShareYourSystem as SYS

#Definition of a Packager instance and module
MyPackager=SYS.PackagerClass().package(
	'ShareYourSystem.Standards.Objects.Printer'
)

#Definition the AttestedStr
SYS._attest(
	[
		'MyPackager'+SYS._str(MyPackager)
	]
) 

#Print

