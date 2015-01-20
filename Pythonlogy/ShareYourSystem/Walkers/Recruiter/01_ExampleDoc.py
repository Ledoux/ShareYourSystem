
#ImportModules
import ShareYourSystem as SYS
import operator

#Definition a Recruiter instance that is grouped
MyRecruiter=SYS.RecruiterClass().update(
		[
			(
				'<Recruiters>FirstChildRecruiter',
				SYS.RecruiterClass().update(
					[
						(
							'<Cumulaters>GrandChildCumulater',
							SYS.CumulaterClass()
						)
					]
				)
			),
			(
				'<Recruiters>SecondChildRecruiter',
				SYS.RecruiterClass()
			),
			(
				'<Recruiters>ThirdChildRecruiter',
				SYS.RecruiterClass()
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
	**{'VisitingCollectionStrsList':['Recruiters','Cumulaters']}
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

 