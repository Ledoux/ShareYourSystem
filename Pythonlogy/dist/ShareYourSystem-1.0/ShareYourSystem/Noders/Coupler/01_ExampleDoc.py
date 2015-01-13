
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Coupler

#store
MyCoupler=Coupler.CouplerClass().collect(
		'Couplome',
		'FirstChild',
		Coupler.CouplerClass()
).collect(
		'Couplome',
		'SecondChild',
		Coupler.CouplerClass()
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

