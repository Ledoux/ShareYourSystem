#<ImportSpecificModules>
from ShareYourSystem.Classors import Representer
from ShareYourSystem.Objects import Initiator
#</ImportSpecificModules>


#Print a version of the class
Representer._print(dict(Representer.RepresenterClass.__dict__.items()))

#Print a version of this object
Representer._print(Representer.RepresenterClass())

#Print a version of his __dict__
Representer._print(Representer.RepresenterClass().__dict__)

#Represent a dict
Dict={
	'ParentDict':
		{
		'ChildDict':
			{
				'MyInt':0
			},
		'MyStr':"hello"
		}
	}
print(Representer.getRepresentedStrWithDictatedVariable(Dict))

#Represent a TuplesList
TuplesList=[
				(
					'ParentTuplesList',
					[
						(
							'ChildDict',
							{
								'MyInt':0
							}
						)
					]
				),
				("MyStr","hello")
			]
print(Representer.getRepresentedStrWithListedVariable(TuplesList))


#Represent a list
List=[
		[
			0,
			[
				"hello"
			]
		]
	]
print(Representer.getRepresentedStrWithListedVariable(List))

#Represent a simple object
@Representer.RepresenterClass()
class MakerClass(Initiator.InitiatorClass):

	RepresentingKeyStrsList=['MakingInt']

	def default_init(self,
						_MakingInt=0,  
						_MadeFloat=1.
					):
		pass

#Print special attributes the class
print('')
print('MakerClass.KeyStrsList is ')
print(MakerClass.KeyStrsList)
print('MakerClass.RepresentedBaseKeyStrsList is ')
print(MakerClass.RepresentedBaseKeyStrsList)

#Print a simple version
print('')
print('Print some Instance with class or instance level defined attributes')
print(MakerClass())
print(MakerClass(_MakingInt=2))
MakerClass.TopStr="I am a new class defined variable"
print(MakerClass(_MadeFloat=2))

#Represent a hierarchic object
ParentMaker=MakerClass()
#ParentMaker.ChildDict={'MyStr':"I make something else"}
ParentMaker.ChildMaker=MakerClass()
#ParentMaker.ChildMaker.MakingStr="I make something else"
print('')
#print(ParentMaker.__repr__())
print(ParentMaker)


#Shift a representation
'''
Representer.RepresentedAlineaStr+="<Shift>"
print(SYS.Representer.getRepresentedStrWithDictatedVariable(Dict))
print(SYS.Representer.getRepresentedStrWithListedVariable(List))
print(ParentMaker.__repr__())
'''

'''
@Representer.RepresenterClass()
class BuilderClass(MakerClass):

	RepresentingKeyStrsList=['BuiltFloat']

	def default_init(self,
						_BuildingInt=0,  
						_BuiltFloat=1.
					):
		MakerClass.__init__(self)

#Print the class
Representer._print(BuilderClass.__dict__)

#Print a simple version
print(BuilderClass())
'''





