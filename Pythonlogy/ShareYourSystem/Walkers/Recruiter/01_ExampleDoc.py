
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Walkers import Cumulater,Recruiter
import operator

#Definition a Recruiter instance that is grouped
MyRecruiter=Recruiter.RecruiterClass().update(
		[
			(
				'<Visitome>FirstChildRecruiter',
				Recruiter.RecruiterClass().update(
					[
						(
							'<Collectome>GrandChildCumulater',
							Cumulater.CumulaterClass()
						)
					]
				)
			),
			(
				'<Visitome>SecondChildRecruiter',
				Recruiter.RecruiterClass()
			),
			(
				'<Visitome>ThirdChildRecruiter',
				Recruiter.RecruiterClass()
			)
		]	
	)

#Walk inside the group in order to parent
MyRecruiter.recruit(
	[
		(
			'NodeIndexInt',
			lambda _TestIndexInt,_AttestIndexInt:operator.lt(_TestIndexInt,_AttestIndexInt)
			if _TestIndexInt!=None else False,
			2
		)
	],
	**{'VisitingCollectionStrsList':['Visitome','Collectome']}
)
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyRecruiter is '+SYS._str(
		MyRecruiter,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
) 

#Print

 