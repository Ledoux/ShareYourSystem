#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Objects import Packager

#Definition of a Packager instance and module
MyPackager=Packager.PackagerClass().package(
	'ShareYourSystem.Objects.Printer'
)

#Definition the AttestedStr
SYS._attest(
	[
		'MyPackager'+SYS._str(MyPackager)
	]
) 

#Print

