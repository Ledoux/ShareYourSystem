
#ImportModules
import ShareYourSystem as SYS

#Definition a Walker instance with a noded tree
MyWalker=SYS.WalkerClass().update(
	[
		(
			'<Walkers>FirstChildWalker',
			SYS.WalkerClass().update(
				[
					(
						'<Walkers>GrandChildWalker',
						SYS.WalkerClass()
					)
				]
			)
		),
		(
			'<Walkers>SecondChildWalker',
			SYS.WalkerClass()
		)
	]	
)

#Walk inside the Tree in order to parent again because the tree was not yet completely setted when it was done
MyWalker.walk(
		{
			'BeforeUpdateList':
			[
				('SwitchingParentBool',False),
				('parent',{'LiargVariablesList':[]})
			],
			'GatherVariablesList':['<Walkers>']
		}
	)


#Definition the AttestedStr
SYS._attest(
	[
		'MyWalker is '+SYS._str(
		MyWalker,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False,
			'RepresentingKeyStrsList':['ParentedDeriveParentersList']
		}
		)
	]
) 

#Print

