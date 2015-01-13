#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Doer,Attester 
from ShareYourSystem.Objects import Initiator

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
	
#Look at the decorated make method
AttestingStrsList=['MakerClass.make is '+str(MakerClass.make)]

#Definition of an instance and make
MyMaker=MakerClass(
	_MakingMyList=['hello'],
	**{'MakingFirstInt':3}
	).superDo_make(
		3.,
		_SecondInt=5
	)

#Add
AttestingStrsList+=[
		'After the make ',
		'MyMaker.MakingMyFloat is '+str(MyMaker.MakingMyFloat),
		'MyMaker.MakingMyList is '+str(MyMaker.MakingMyList),
		'MyMaker.MakingFirstInt is '+str(MyMaker.MakingFirstInt),
		'MyMaker.MakingSecondInt is '+str(MyMaker.MakingSecondInt),
		'MyMaker.MadeMyInt is '+str(MyMaker.MadeMyInt),
		'MyMaker.MadeMyList is '+str(MyMaker.MadeMyList)
	]

#Print
#print(AttestingStrsList)

#Definition
SYS._attest(AttestingStrsList)

#Print
