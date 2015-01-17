import brian


help(brian.Synapses)


"""
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Connecter,Networker
import operator

#Definition of a brian structure
MyNetworker=Networker.NetworkerClass(
	).push(
[
	(
		'First',
		Connecter.ConnecterClass().update(
			[
				('ConnectingGraspClueVariablesList',
					[
						'/NodePointDeriveNoder/<Connectome>SecondConnecter'
					]
				),
				('TagStr','Networked')
			]
		)
	),
	(
		'Second',
		Connecter.ConnecterClass().__setitem__(
			'TagStr',
			'Networked'
		)
	)
],
	**{
		'CollectingCollectionStr':'Connectome'
	}
).network(
	**{
				'RecruitingConcludeConditionTuplesList':[
					('__class__.NameStr',operator.eq,'Connecter')
				]
		}
	)	

#Definition the AttestedStr
SYS._attest(
	[
		'MyNetworker is '+SYS._str(
		MyNetworker,
		**{
			'RepresentingBaseKeyStrsList':False,
			'RepresentingAlineaIsBool':False
		}
		),
	]
) 

#Print
"""
