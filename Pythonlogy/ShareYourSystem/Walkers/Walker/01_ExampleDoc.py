
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Walkers import Walker

#Definition a Walker instance with a noded tree
MyWalker=Walker.WalkerClass().update(
	[
		(
			'<Tree>FirstChildWalker',
			Walker.WalkerClass().update(
				[
					(
						'<Tree>GrandChildWalker',
						Walker.WalkerClass()
					)
				]
			)
		),
		(
			'<Tree>SecondChildWalker',
			Walker.WalkerClass()
		)
	]	
)

#Walk inside the Tree in order to parent again because the tree was not yet completely setted when it was done
MyWalker.walk(
			{
				'BeforeUpdateList':
				[
					('SwitchingParentBool',False),
					('parent',{'LiargVariablesList':['Tree']})
				],
				'GatherVariablesList':['<Tree>']
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

