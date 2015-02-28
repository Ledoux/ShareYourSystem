#ImportModules
import ShareYourSystem as SYS

#Definition a MakerClass decorated by the DefaultorClass
@SYS.DoerClass()
class MakerClass(object):

	def default_init(self,
				_MakingMyFloat=1.,
				_MakingShareList=['bonjour'],
				_MakingSpecificList=None,
				_MakingMyInt={'DefaultValueType':int}
				):
		object.__init__(self)

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
print("\n".join(
	[
	'MakerClass has some special attributes',
	'MakerClass.DoingAttributeVariablesOrderedDict is '+str(
		MakerClass.DoingAttributeVariablesOrderedDict),
	'MakerClass.DoneAttributeVariablesOrderedDict is '+str(
		MakerClass.DoneAttributeVariablesOrderedDict),
	'What are you saying DefaultMaker ?',
	'DefaultMaker.__dict__ is '+str(DefaultMaker.__dict__),
	'DefaultMaker.getDo() is '+str(DefaultMaker.getDo()),
	'What are you saying SpecialMaker ?',
	'SpecialMaker.__dict__ is '+str(SpecialMaker.__dict__),
	'SpecialMaker.getDo() is '+str(SpecialMaker.getDo())
	]
))

#Change classed attributes
MakerClass.MakingMyFloat=5.
MakerClass.MakingMyInt=5

#Add
print("\n"+"\n".join(
	[
		'After reset at the level of the class',
		'What are you saying DefaultMaker ?',
		'DefaultMaker.__dict__ is '+str(DefaultMaker.__dict__),
		'DefaultMaker.getDo() is '+str(DefaultMaker.getDo()),
		'What are you saying SpecialMaker ?',
		'SpecialMaker.__dict__ is '+str(SpecialMaker.__dict__),
		'SpecialMaker.getDo() is '+str(SpecialMaker.getDo())
	]
))


