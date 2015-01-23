#ImportModules
import ShareYourSystem as SYS

#Represent a simple object
@SYS.RepresenterClass()
class MakerClass(SYS.InitiatorClass):

	RepresentingKeyStrsList=['MadeMyInt']

	def default_init(self,
						_MakingMyFloat=0.,  
						_MadeMyInt=0
					):
		pass
	
#Definition a simple instance
SimpleMaker=MakerClass(_MakingMyFloat=2.)

#Represent a structured instance
ParentMaker=MakerClass()
ParentMaker.FirstChildMaker=MakerClass()
ParentMaker.CircularChildMaker=MakerClass()
ParentMaker.CircularChildMaker.ParentMaker=ParentMaker
ParentMaker.CircularChildMaker.SelfMaker=ParentMaker.CircularChildMaker

#Definition a derived class from the MakerClass
@SYS.RepresenterClass()
class BuilderClass(MakerClass):

	RepresentingKeyStrsList=['BuiltMyStr']

	def default_init(self,
						_BuildingMyStr='hello',  
						_BuiltMyStr='None'
					):
		pass

#Definition a simple instance
SimpleBuilder=BuilderClass(_MakingMyFloat=2.)

#Definition the AttestedStr
SYS._attest(
	[
		'SimpleMaker is '+SYS._str(SimpleMaker),
		'ParentMaker is '+SYS._str(ParentMaker),
		'SimpleBuilder is '+SYS._str(SimpleBuilder)
	]
) 

#Print

