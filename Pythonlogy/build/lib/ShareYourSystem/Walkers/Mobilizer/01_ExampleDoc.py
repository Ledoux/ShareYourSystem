
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Walkers import Visiter,Recruiter,Mobilizer
import operator

#Definition a Mobilizer instance that is grouped
MyMobilizer=Mobilizer.MobilizerClass().update(
	[
		(
			'<Mobilizome>FirstChildMobilizer',
			Mobilizer.MobilizerClass().update(
				[
					(
						'<Recruitome>GrandChildRecruiter',
						Recruiter.RecruiterClass()
					),
					(
						'<Recruitome>FakeGrandChildVisiter',
						Visiter.VisiterClass()
					)
				]
			)
		),
		(
			'<Mobilizome>SecondChildMobilizer',
			Mobilizer.MobilizerClass()
		),
		(
			'<Mobilizome>ThirdChildMobilizer',
			Mobilizer.MobilizerClass()
		)
	]	
)

#Walk inside the group in order to parent
MyMobilizer.mobilize(
	[
		'Mobilizer','Recruiter'
	],
	**{
			'VisitingCollectionStrsList':['Mobilizome','Recruitome'],
			'RecruitingConcludeConditionTuplesList':[('NodeIndexInt',lambda _TestInt,_AttestInt:
				_TestInt!=None and operator.lt(_TestInt,_AttestInt),2)]
	}
)
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyMobilizer is '+SYS._str(
		MyMobilizer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
) 

#Print

