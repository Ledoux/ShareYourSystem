
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Applyiers import Poker

#push
MyPoker=Poker.PokerClass().push(
	[
		[
			'FirstChild',
			Poker.PokerClass()
		],
		[
			'SecondChild',
			Poker.PokerClass()
		],
		[
			'ThirdChild',
			Poker.PokerClass()
		]
	],
	**{'CollectingCollectionStr':"Pokome"}
)


MyPoker['<Pokome>ThirdChildPoker'].poke(
		'Relatome',
		[
			'/NodePointDeriveNoder/<Pokome>FirstChildPoker',
			'/NodePointDeriveNoder/<Pokome>SecondChildPoker'
		]
	)

#Definition the AttestedStr
SYS._attest(
	[
		'MyPoker is '+SYS._str(
		MyPoker,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
) 

#Print

