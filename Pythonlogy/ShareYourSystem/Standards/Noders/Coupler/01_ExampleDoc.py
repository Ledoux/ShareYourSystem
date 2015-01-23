
#ImportModules
import ShareYourSystem as SYS

#store
MyCoupler=SYS.CouplerClass().collect(
		'Couplome',
		'FirstChild',
		SYS.CouplerClass()
).collect(
		'Couplome',
		'SecondChild',
		SYS.CouplerClass()
)

#couple
MyCoupler['<Couplome>SecondChildCoupler'].couple(
			'Relatome',
			'/NodePointDeriveNoder/<Couplome>FirstChildCoupler'
	)

#Return
SYS._attest(
	[
	'MyCoupler is '+SYS._str(
			MyCoupler,
			**{
				'RepresentingBaseKeyStrsListBool':False,
				'RepresentingAlineaIsBool':False
			}
		)
	]
)

#Print

