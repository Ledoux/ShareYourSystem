
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Simulaters import Rater,Brianer

#Definition of a brian structure
MyBrianer=Brianer.BrianerClass(
	).push(
	[
		(
			'First',
			Rater.RaterClass().update(
				[
					('PopulatingUnitsInt',3),
					('MoniteringTrackTuplesList',
						[
							('State','v',[0,1],1.)
						]
					),
					('ConnectingCatchGetStrsList',
						[
							'/NodePointDeriveNoder/<Connectome>SecondRater'
						]
					),
					('ConnectingAttentionGetStrsList',
						[
							'/NodePointDeriveNoder/<Connectome>SecondRater'
						]
					)
				]
			)
		),
		(
			'Second',
			Rater.RaterClass().update(
				[
					('PopulatingUnitsInt',1)
				]
			)
		)
	],
	**{
		'CollectingCollectionStr':'Connectome'
	}
).run(2.)	
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyBrianer is '+SYS._str(
		MyBrianer,
		**{
			'RepresentingBaseKeyStrsList':False,
			'RepresentingAlineaIsBool':False
		}
		),
	]
) 

#Print


