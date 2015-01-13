
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Applyiers import Pusher

#push
MyPusher=Pusher.PusherClass().push(
	[
		[
			'FirstChild',
			Pusher.PusherClass().__setitem__('MyInt',0)
		],
		[
			'SecondChild',
			Pusher.PusherClass()
		]
	],
	**{'CollectingCollectionStr':'Pushome'}
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

