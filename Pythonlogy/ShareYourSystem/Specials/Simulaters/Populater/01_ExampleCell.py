
#ImportModules
import ShareYourSystem as SYS
import operator

#Definition of a brian structure
MyNetworker=SYS.NetworkerClass(
	).produce(
		'Networkers',
		['First','Second'],
		SYS.NetworkerClass,
		{
			'produce':{
				'LiargVariablesList':
				[
					['E','I'],
					SYS.PopulaterClass,
					{
						'PopulatingUnitsInt':500
					}
				],
			}
		}
	).network(
		**{
				'RecruitingConcludeConditionTuplesList':[
					('__class__.NameStr',operator.eq,'Populater')
				],
				'VisitingCollectionStrsList':['Networkers','Populaters']
		}
	)

#populate in each
map(
	lambda __NetworkedDeriveConnecter:
	__NetworkedDeriveConnecter.populate(),
	MyNetworker.NetworkedDeriveConnectersList
)
	
#Definition the AttestedStr
SYS._attest(
	[
		'MyNetworker is '+SYS._str(
		MyNetworker,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
	]
) 

#Print

