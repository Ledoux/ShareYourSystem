#ImportModules
import ShareYourSystem as SYS

#Update several things
MyUpdater=SYS.UpdaterClass(
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

