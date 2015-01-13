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
				_MakingSpecificList=None,
				_MakingMyInt={'DefaultingSetType':int}
				):
		pass

#Definition a default instance
DefaultMaker=MakerClass()

#Definition a special instance
SpecialMaker=MakerClass(_MakingMyList=['hello'],**{'MakingMyInt':3})

#Definition the AttestedStr
AttestingStrsList=[
	'MakerClass has some special attributes',
	'MakerClass.DoingAttributeVariablesOrderedDict is '+SYS._str(
		MakerClass.DoingAttributeVariablesOrderedDict),
	'MakerClass.DoneAttributeVariablesOrderedDict is '+SYS._str(
		MakerClass.DoneAttributeVariablesOrderedDict),
	'MakerClass.MakingMyFloat is '+str(MakerClass.MakingMyFloat),
	'MakerClass.MakingSpecificList is '+str(MakerClass.MakingSpecificList),
	'MakerClass.MakingShareList is '+str(MakerClass.MakingShareList),
	'What are you saying DefaultMaker ?',
	'DefaultMaker.__dict__ is '+SYS._str(DefaultMaker.__dict__),
	'DefaultMaker.MakingMyFloat is '+str(DefaultMaker.MakingMyFloat),
	'DefaultMaker.MakingShareList is '+str(DefaultMaker.MakingShareList),
	'DefaultMaker.MakingSpecificList is '+str(DefaultMaker.MakingSpecificList),
	'DefaultMaker.MakingMyInt is '+str(DefaultMaker.MakingMyInt),
	'What are you saying SpecialMaker ?',
	'SpecialMaker.__dict__ is '+SYS._str(SpecialMaker.__dict__),
	'SpecialMaker.MakingMyFloat is '+str(SpecialMaker.MakingMyFloat),
	'SpecialMaker.MakingShareList is '+str(SpecialMaker.MakingShareList),
	'SpecialMaker.MakingSpecificList is '+str(SpecialMaker.MakingSpecificList),
	'SpecialMaker.MakingMyInt is '+str(SpecialMaker.MakingMyInt),
]

#Change a classed attribute
MakerClass.MakingMyFloat=5.

#Add
AttestingStrsList+=[
		'After reset at the level of the class',
		'DefaultMaker.MakingMyFloat is '+str(DefaultMaker.MakingMyFloat),
		'SpecialMaker.MakingMyFloat is '+str(SpecialMaker.MakingMyFloat),
	]

#Print
#print(AttestingStrsList)

#Definition
SYS._attest(AttestingStrsList)

#Print

