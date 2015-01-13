#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Interfacers import Interfacer

#Definition 
MyInterfacer=Interfacer.InterfacerClass()
	
#Definition the AttestedStr
SYS._attest(
	[
		'MyInterfacer is '+SYS._str(
			MyInterfacer,
			**{
			'RepresentingAlineaIsBool':False
			})
	]
) 

#Print

