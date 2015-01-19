#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Settler

#Short expression and set in the appended manner
MySettler=Settler.SettlerClass().__setitem__(
	'<Settlome>ChildSettler',
	Settler.SettlerClass()
).update(
	[
		(
			'<Settlome>GrandFirstChildSettler',
			Settler.SettlerClass()
		),
		(
			'<Settlome>GrandSecondChildSettler',
			Settler.SettlerClass(**{
				'SettlingParentBool':True,
				'SettlingLinkBool':True
				}
				).__setitem__(
				'LinkingPointListsList',
				[
		('/NodePointDeriveNoder/<Settlome>GrandFirstChildSettler','GrandFirstChildSettler')
				]
			)
		)
	]
)



#Definition the AttestedStr
SYS._attest(
	[
		'MySettler is '+SYS._str(
		MySettler,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
) 
#Print

