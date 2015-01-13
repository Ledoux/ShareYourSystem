
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Doer,Deriver,Attester
from ShareYourSystem.Objects import Initiator

#Definition of a MakerClass decorated by a DoerClass instance
@Doer.DoerClass()
class MakerClass(Initiator.InitiatorClass):
	pass

#Definition of a derived BuilderClass decorated by a Deriver
@Deriver.DeriverClass()
class BuilderClass(MakerClass):
	pass

#Print
#print('MakerClass.DerivedClassesList is '+str(MakerClass.DerivedClassesList))

#Definition the AttestedStr
SYS._attest(
	[
		'MakerClass.DerivedClassesList is '+str(MakerClass.DerivedClassesList)
	]
) 

#Print
