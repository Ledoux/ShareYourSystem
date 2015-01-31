#ImportModules
import ShareYourSystem as SYS

#Definition
MyRater=SYS.RaterClass().update(
	{
		'RatingTimeConstantVariable':10.,

		'PopulatingUnitsInt':2,

		'collect':
		{
			'LiargVariablesList':
			[
				"Matricers",
				"Local",
				SYS.MatrixerClass().update(
					{
						'MatricingStdFloat':1.,
						'MatricingStatStr':'norm',
						'MatricingNormalisationFunction':lambda _UnitsInt:1./_UnitsInt
					}
				)
			]
		},

		'produce':
		{
			'LiargVariablesList':
			[
				"StateMoniters",
				['Rate'],
				SYS.MoniterClass,
				{
					'MoniteringVariableStr':'RatedPostFloatsList',
					'MoniteringIndexIntsList':[0,1]
				}
			]
		}
	}
).rate()
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyRater is '+SYS._str(
		MyRater,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False,
			'RepresentingKeyStrsList':[
			]
		}
		),
	]
) 

#Print

