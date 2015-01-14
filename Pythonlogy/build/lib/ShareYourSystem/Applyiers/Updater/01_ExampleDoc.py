#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Applyiers import Updater

#Update several things
MyUpdater=Updater.UpdaterClass(
	).update(
		[
			('MyInt',0),
			('MyFloat',0.2)
		]
	).update(
		{
			'MyStr':"hello"
		}
	)
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyUpdater is '+SYS._str(
		MyUpdater,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
)  

#Print

