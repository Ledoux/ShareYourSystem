#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Standards.Classors import Doer,Attester 
from ShareYourSystem.Standards.Objects import Initiator

#Definition a MakerClass decorated by the DefaultorClass
@Doer.DoerClass()
class MakerClass(Initiator.InitiatorClass):

	def default_init(self,
				_MakingMyFloat=0.,
				_MadeShareInitiator=Initiator.InitiatorClass(),
				_MadeSpecificInitiator=None
				):
		pass

	def do_make(self):

		#print
		print('Maker : I am going to make')
		print('')

		#set
		self.MadeSpecificInitiator.MyInt=int(self.MakingMyFloat)

		#Return self
		#return self
	
#Definition of an instance and make
MakerClass.MadeShareInitiator.MyInt=5
MyMaker=MakerClass().make(3.)

#Add
AttestingStrsList=[
		'After the make ',
		'MakerClass.MadeSpecificInitiator is '+str(MakerClass.MadeSpecificInitiator),
		'MyMaker.MadeShareInitiator.__dict__ is '+str(MyMaker.MadeShareInitiator.__dict__),
		'MyMaker.MadeSpecificInitiator.__dict__ is '+str(MyMaker.MadeSpecificInitiator.__dict__)
	]

#Print
#print(AttestingStrsList)

#Definition
SYS._attest(AttestingStrsList)

#Print
