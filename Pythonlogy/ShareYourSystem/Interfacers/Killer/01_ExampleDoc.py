#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Interfacers import Killer

#Definition a Killer
MyKiller=Killer.KillerClass().kill(**{'StatusingProcessStr':"Python"})

#Definition the AttestedStr
SYS._attest(
	[
		'MyKiller is '+SYS._str(
		MyKiller,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
)  

#Print



