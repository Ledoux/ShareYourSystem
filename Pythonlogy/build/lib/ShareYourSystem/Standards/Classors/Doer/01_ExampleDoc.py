#ImportModules
import ShareYourSystem as SYS

#Definition a MakerClass decorated by the DefaultorClass
@SYS.DoerClass()
class MakerClass(SYS.InitiatorClass):

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
SpecialMaker=MakerClass(
	_MakingSpecificList=['hello'],
	**{
		'MakingMyFloat':3.
	}
)

#Definition the AttestedStr
AttestingStrsList=[
	'MakerClass has some special attributes',
	'MakerClass.DoingAttributeVariablesOrderedDict is '+SYS._str(
		MakerClass.DoingAttributeVariablesOrderedDict),
	'MakerClass.DoneAttributeVariablesOrderedDict is '+SYS._str(
		MakerClass.DoneAttributeVariablesOrderedDict),
	'What are you saying DefaultMaker ?',
	'DefaultMaker.__dict__ is '+SYS._str(DefaultMaker.__dict__),
	'DefaultMaker.getDo() is '+SYS._str(DefaultMaker.getDo()),
	'What are you saying SpecialMaker ?',
	'SpecialMaker.__dict__ is '+SYS._str(SpecialMaker.__dict__),
	'SpecialMaker.getDo() is '+SYS._str(SpecialMaker.getDo())
]

#Change classed attributes
MakerClass.MakingMyFloat=5.
MakerClass.MakingMyInt=5

#Add
AttestingStrsList+=[
		'After reset at the level of the class',
		'What are you saying DefaultMaker ?',
		'DefaultMaker.__dict__ is '+SYS._str(DefaultMaker.__dict__),
		'DefaultMaker.getDo() is '+SYS._str(DefaultMaker.getDo()),
		'What are you saying SpecialMaker ?',
		'SpecialMaker.__dict__ is '+SYS._str(SpecialMaker.__dict__),
		'SpecialMaker.getDo() is '+SYS._str(SpecialMaker.getDo())
	]

#Print
#print(AttestingStrsList)

#Definition
SYS._attest(AttestingStrsList)

#Print

