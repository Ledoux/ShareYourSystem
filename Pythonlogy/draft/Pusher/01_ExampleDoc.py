
#ImportModules
import ShareYourSystem as SYS

#push
MyPusher=SYS.PusherClass().push(
	'Pushome',
	[
		[
			'FirstChild',
			SYS.PusherClass().__setitem__('MyInt',0)
		],
		[
			'SecondChild',
			SYS.PusherClass()
		]
	]
)

#Definition the AttestedStr
SYS._attest(
	[
		'MyPusher is '+SYS._str(
		MyPusher,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
) 

