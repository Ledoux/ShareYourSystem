
#ImportModules
import ShareYourSystem as SYS

from ShareYourSystem.Walkers import Router

#Definition a Router instance that has Tree nodes
MyRouter=Router.RouterClass().update(
	[
		(
			'<Tree>FirstChildRouter',
			Router.RouterClass().update(
				[
					(
						'<Tree>GrandChildRouter',
						Router.RouterClass()
					)
				]
			)
		),
		(
			'<Tree>SecondChildRouter',
			Router.RouterClass()
		)
	]	
)

#Walk inside the Tree in order to parent
MyRouter.walk(
	{
		'BeforeUpdateList':
		[
			('route',{'LiargVariablesList':[
												['NodedTreeInt','NodedTreeKeyStr']
												#['/']
											]
					})
		],
		'GatherVariablesList':['<Tree>']
	}
)

#Definition the AttestedStr
SYS._attest(
	[
		'MyRouter is '+SYS._str(
		MyRouter,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
) 

#Print

 