
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Simulaters import Rater,Brianer
from ShareYourSystem.Noders import Connecter

#Definition of a brian structure
MyBrianer=Brianer.BrianerClass(
	).push(
		'Populome',
		map(
				lambda __KeyStr:
				[
					__KeyStr,
					Rater.RaterClass()
				],
				['First','Second']
			)
	).push(
		'Connectome',
		map(
				lambda __KeyStr:
				[
					__KeyStr,
					Connecter.ConnecterClass(**{
						'ConnectingGetStrsTuple':[
								'/NodePointDeriveNoder/<Populome>FirstRater',
								'/NodePointDeriveNoder/<Populome>SecondRater'
							]
						}
					)
				],
				['FirstToSecond']
			)
	).push(
		'Clockome',
		[
			['Simulation',{'ClockingStepTimeFloat':0.1}],
			['Record',{'ClockingStepTimeFloat':1.}]
		]
	)
).brian('Populome','Connectome','Clockome')
		
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


