#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Applyiers import Gatherer

#Definition a Gatherer
MyGatherer=Gatherer.GathererClass().map('__setitem__',map(
		lambda __ItemTuple:
		{'LiargVariablesList':__ItemTuple},
		[
			('MyInt',0),
			('FirstChildGatherer',Gatherer.GathererClass().__setitem__(
					'MyStr',
					"bonjour"
					)
			),
			('SecondChildGatherer',Gatherer.GathererClass().__setitem__(
					'MyStr',
					"hello"
					)
			)
		]
	)
)

#Map some gets
GatheredVariablesList=MyGatherer.gather(
							[
								['MyInt'],
								['/FirstChildGatherer/MyStr','/SecondChildGatherer/MyStr']
							]
						)
		
#Definition the AttestedStr
SYS._attest(
	[
		'GatheredVariablesList is '+SYS._str(
			GatheredVariablesList
			,**{
					'RepresentingBaseKeyStrsListBool':False,
					'RepresentingAlineaIsBool':False
			}
		)
	]
) 

#Print

