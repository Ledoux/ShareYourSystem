#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Doer,Attester 
from ShareYourSystem.Objects import Initiator

#Definition a MakerClass decorated by the DefaultorClass
@Doer.DoerClass()
class MakerClass(Initiator.InitiatorClass):

	def default_init(self,
				_MakingMyFloat=1.,
				_MakingShareList=['bonjour'],
				_MakingRestrictList=None,
				_MakingMyInt={'DefaultingSetType':int}
				):
		pass

	def do_make(self):

		#print
		print('Maker : I am going to make')
		print('')

		#set
		self.MadeMyInt=int(self.MakingMyFloat)

		#Return self
		#return self
		
#Definition the AttestedStr
AttestingStrsList=[
	'MakerClass.do_make is '+str(MakerClass.do_make),
	'MakerClass.doWithmake is '+str(MakerClass.superDo_make),
	'MakerClass.make is '+str(MakerClass.make),
	'MakerClass.callDo is '+str(MakerClass.callDo),
]

#Print
#print(AttestingStrsList)

#Definition
SYS._attest(AttestingStrsList)

#Print

