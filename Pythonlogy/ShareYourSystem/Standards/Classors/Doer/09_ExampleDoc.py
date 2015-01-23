#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Standards.Classors import Doer,Attester 
from ShareYourSystem.Standards.Objects import Initiator

#Definition a MakerClass decorated by the DefaultorClass
@Doer.DoerClass()
class MakerClass(Initiator.InitiatorClass):

	def default_init(self,
				_MakingMyFloat=1.,
				_MakingMyList=None,
				_MakingFirstInt={'DefaultingSetType':int},
				_MakingSecondInt=0,
				_MadeMyInt=0,
				_MadeMyList=None,
				):
		pass

	def do_make(self):

		#print
		print('Maker : I am going to make')
		print('self.MakingMyFloat is ',self.MakingMyFloat)
		print('')

		#set
		self.MadeMyInt=int(self.MakingMyFloat)

		#Return self
		#return self
	
#Definition of an instance and make
MyMaker=MakerClass(
	_MakingMyList=['hello'],
	**{'MakingFirstInt':3}
	).superDo_make(
		3.,['bonjour'],
		_SecondInt=5
	)

print('MyMaker is ')
SYS._print(MyMaker)

print('we reset doing')
MyMaker.setDoing(MakerClass)

print('MyMaker after set doing is ')
SYS._print(MyMaker)

#Add
AttestingStrsList=[
		'MyMaker.__dict__ is '+SYS._str(MyMaker.__dict__,
			**{'RepresentingAlineaIsBool':False})
	]

#Definition
SYS._attest(AttestingStrsList)

#Print
