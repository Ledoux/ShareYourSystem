
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Walkers import Cumulater,Visiter

#Definition a Visiter instance that is grouped
MyVisiter=Visiter.VisiterClass().update(
	[
		(
			'<Visitome>FirstChildVisiter',
			Visiter.VisiterClass().update(
				[
					(
						'<Collectome>GrandChildCumulater',
						Cumulater.CumulaterClass()
					)
				]
			)
		),
		(
			'<Visitome>SecondChildVisiter',
			Visiter.VisiterClass()
		)
	]	
)

#Walk inside the group in order to parent
MyVisiter.visit(['Visitome','Collectome'],[('TagStr','Je suis passe par la')])
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyVisiter is '+SYS._str(
		MyVisiter,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
) 

#Print

 