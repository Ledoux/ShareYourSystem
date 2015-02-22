#ImportModules
import ShareYourSystem as SYS

#Definition 
MyInterfacer=SYS.InterfacerClass()
	
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

