#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Inspecter,Attester 
from ShareYourSystem.Objects import Initiator

#Definition a FooClass decorated by the ClassorClass
@Inspecter.InspecterClass()
class MakerClass(Initiator.InitiatorClass):
	def make(self,
			_MakingStr,
			_MakingInt=0,
			**_KwargVariablesDict
		):
		self.__class__.__bases__[0].__init__(self,**_KwargVariablesDict)

#Definition the AttestedStr
SYS._attest(
	[
		'MakerClass.InspectedArgumentDict is '+SYS._str(MakerClass.InspectedArgumentDict)
	]
) 

#Print

