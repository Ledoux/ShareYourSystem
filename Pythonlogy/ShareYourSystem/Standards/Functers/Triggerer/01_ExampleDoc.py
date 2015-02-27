#ImportModules
import operator
from ShareYourSystem.Standards.Classors import Attester,Doer
from ShareYourSystem.Functers import Triggerer
from ShareYourSystem.Standards.Objects import Initiator

#Definition a MakerClass decorated by the TriggererClass
@Doer.DoerClass()
class MakerClass(Initiator.InitiatorClass):

	def __init__(self,
				_MakingMyFloat=1.,
				_MakingMyList=None,
				_MakingMyInt={'DefaultValueType':int},
				_MadeMyInt=0):
		Initiator.InitiatorClass.__init__(self)

	#Definition a triggering function
	def printShould(self):

		#Print
		print('Should I make ?')

	@Triggerer.TriggererClass(**{
			'TriggeringHookFunctionStr':'printShould',
			'TriggeringConditionVariable':[('MakingMyFloat',(operator.gt,5.))]
	})
	def do_make(self):

		#Print
		print("Yes, I am Making !")
		self.MadeMyInt=int(self.MakingMyFloat)


#Definition an instance and HERE particular case where the class is not yet a Watcher....We have to call once the triggering method to set it
MakerClass().make()
NotTriggeringMaker=MakerClass()
TriggeringMaker=MakerClass(_MakingMyFloat=6.)

#Do just a test of the basic FirstClass method printSomething
NotTriggeringMaker.printShould()
TriggeringMaker.printShould()

#Definition the AttestedStr
SYS._attest(
	[
		'NotTriggeringMaker.MadeMyInt is '+str(NotTriggeringMaker.MadeMyInt),
		'TriggeringMaker.MadeMyInt is '+str(TriggeringMaker.MadeMyInt)
	]
) 

#Print



