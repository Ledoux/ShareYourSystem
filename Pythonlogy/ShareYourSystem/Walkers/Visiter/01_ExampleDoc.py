
#ImportModules
import ShareYourSystem as SYS

#Definition a Visiter instance that is grouped
MyVisiter=SYS.VisiterClass().update(
	[
		(
			'<Visiters>FirstChildVisiter',
			SYS.VisiterClass().update(
				[
					(
						'<Collecters>GrandChildCumulater',
						SYS.CumulaterClass()
					)
				]
			)
		),
		(
			'<Visiters>SecondChildVisiter',
			SYS.VisiterClass()
		)
	]	
)

#Walk inside the group in order to parent
MyVisiter.visit(
	['Visiters','Collecters'],
	[('TagStr','Je suis passe par la')]
)
		
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

 