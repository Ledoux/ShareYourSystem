#ImportModules
import ShareYourSystem as SYS,Classer
from ShareYourSystem.Functers import Imitater
from ShareYourSystem.Objects import Initiator

@Classer.ClasserClass()
class MakerClass(Initiator.InitiatorClass):

	def __init__(self,
			_MakingMyFloat=0.,
			_MakingMyList=None,
			_MakingMyInt=0,
			_MadeMyInt=0	
		):
		pass

	def do_make(self):
		self.MadeMyInt=int(self.MakingMyFloat)

@Classer.ClasserClass()
class BuilderClass(MakerClass):

	def __init__(self):

		#Call the parent method
		MakerClass.__init__(self)

	@Imitater.ImitaterClass()
	def make(self):

		#Call the parent method
		MakerClass.make(self)

		#Do something more
		self.MadeMyInt+=2

#Definition of a Builder instance that is going to make
MyBuilder=BuilderClass().make(3.)

#Definition the AttestedStr
SYS._attest(
	[
		'BuilderClass.make is '+str(BuilderClass.make),
		'MyBuilder.__dict__ is '+SYS._str(
		MyBuilder.__dict__,
		**{
			'RepresentingBaseKeyStrsListBool':False
		}
		)
	]
) 

#Print




