
#ImportModules
import ShareYourSystem as SYS
import operator

#Definition a Mobilizer instance that is grouped
MyMobilizer=SYS.MobilizerClass().update(
	[
		(
			'<Mobilizers>FirstChildMobilizer',
			SYS.MobilizerClass().update(
				[
					(
						'<Recruiters>GrandChildRecruiter',
						SYS.RecruiterClass()
					),
					(
						'<Recruiters>FakeGrandChildVisiter',
						SYS.VisiterClass()
					)
				]
			)
		),
		(
			'<Mobilizers>SecondChildMobilizer',
			SYS.MobilizerClass()
		),
		(
			'<Mobilizers>ThirdChildMobilizer',
			SYS.MobilizerClass()
		)
	]	
)

#Walk inside the group in order to parent
MyMobilizer.mobilize(
	[
		'Mobilizer','Recruiter'
	],
	**{
			'VisitingCollectionStrsList':['Mobilizers','Recruiters'],
			'RecruitingConcludeConditionVariable':[
			('NodeIndexInt',lambda _TestInt,_AttestInt:
				_TestInt!=None and operator.lt(_TestInt,_AttestInt),2)
			]
	}
)
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyMobilizer is '+SYS._str(
		MyMobilizer.CumulatedVariablesList,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
) 

#Print

