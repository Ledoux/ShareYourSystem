#ImportModules
import ShareYourSystem as SYS
import operator

#Definition of a brian structure
MyNetworker=SYS.NetworkerClass(
	).array(
		["Networkers","Connecters"],
		[
			['A','B'],['1','2']
		],
		[SYS.NetworkerClass,SYS.ConnecterClass],
	).update(
		[
			(
				'<Networkers>ANetworker/Dis_<Connecters>',
				[
						[
							('ConnectingGraspClueVariablesList',
								[
									'/NodePointDeriveNoder/<Connecters>2Connecter'
								]
							),
							('TagStr','Networked')
						],
						[
							('TagStr','Networked')
						]
				]
			),
		]
	).network(
		**{
			'VisitingCollectionStrsList':["Networkers","Connecters"],
			'RecruitingConcludeConditionTuplesList':[
				('NameStr',operator.eq,'Connecter')
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
