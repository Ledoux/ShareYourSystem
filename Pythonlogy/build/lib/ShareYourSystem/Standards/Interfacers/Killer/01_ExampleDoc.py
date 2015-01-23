#ImportModules
import ShareYourSystem as SYS

#Definition a Killer
MyKiller=SYS.KillerClass().kill(**{'StatusingProcessStr':"Python"})

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



