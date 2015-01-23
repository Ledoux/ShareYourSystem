#ImportModules
import ShareYourSystem as SYS

#Definition
MyGatherer=SYS.GathererClass()

#Definition a Gatherer
map(
		lambda __ItemTuple:
		MyGatherer.__setitem__(*__ItemTuple),
		[
			('MyInt',0),
			(
				'FirstChildGatherer',
				SYS.GathererClass().__setitem__(
					'MyStr',
					"bonjour"
				)
			),
			(
				'SecondChildGatherer',
				SYS.GathererClass().__setitem__(
					'MyStr',
					"hello"
				)
			)
		]
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

