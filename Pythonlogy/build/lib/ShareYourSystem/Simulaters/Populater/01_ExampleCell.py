
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Networker
from ShareYourSystem.Simulaters import Populater
import operator

#Definition of a brian structure
MyNetworker=Networker.NetworkerClass(
	).produce(
		['First','Second'],
		Networker.NetworkerClass,
		{
			'produce':{
				'LiargVariablesList':
				[
					['E','I'],
					Populater.PopulaterClass,
					{
						'PopulatingUnitsInt':500
					}
				],
				'KwargVariablesDict':
				{
					'CollectingCollectionStr':'Populatome'
				}
			}
		},
		**{
			'CollectingCollectionStr':'Nodome'
		}
	).network(
		**{
				'RecruitingConcludeConditionTuplesList':[
					('__class__.NameStr',operator.eq,'Populater')
				],
				'VisitingCollectionStrsList':['Nodome','Populatome']
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

