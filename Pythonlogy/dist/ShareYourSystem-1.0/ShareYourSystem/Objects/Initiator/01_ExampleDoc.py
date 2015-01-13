
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Attester
from ShareYourSystem.Objects import Initiator

#Definition of an Initiator instance
MyInitiator=Initiator.InitiatorClass()
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyInitiator is '+SYS._str(MyInitiator)
	]
) 

#Print

