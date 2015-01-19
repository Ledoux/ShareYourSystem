#ImportModules
from ShareYourSystem.Classors import Representer,Attester,Classer
from ShareYourSystem.Functers import Argumenter
from ShareYourSystem.Objects import Initiator

#Definition a derived second Class
@Classer.ClasserClass()
class MakerClass(Initiator.InitiatorClass):

	def __init__(self,
			_MakingMyFloat=0.,
			_MakingMyList=None,
			_MakingMyInt=0,
			_MadeMyInt=0	
		):
		
		#Call the parent method
		Initiator.InitiatorClass.__init__(self)

	@Argumenter.ArgumenterClass()
	def special_make(self,**_KwargsVariablesDict):

		#Cast
		self.MadeMyInt=int(self.MakingMyFloat)

#Define an instance
MyMaker=MakerClass()

#make
MyMaker.special_make(**{'MakingMyFloat':3.})

#Definition the AttestedStr
SYS._attest(
	[
		'MyMaker.__dict__ is '+SYS._str(
		MyMaker.__dict__,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
	]
) 

#Print

