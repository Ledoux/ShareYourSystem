
#ImportModules
import ShareYourSystem as SYS

from ShareYourSystem.Walkers import Grabber

#Definition a Grabber instance that has Tree nodes
MyGrabber=Grabber.GrabberClass().update(
		[
			(
				'<Tree>FirstChildGrabber',
				Grabber.GrabberClass().update(
					[
						(
							'<Tree>GrandChildGrabber',
							Grabber.GrabberClass()
						)
					]
				)
			),
			(
				'<Tree>SecondChildGrabber',
				Grabber.GrabberClass()
			)
		]	
	)

#Grab
MyGrabber.grab("Tree",['NodedTreeInt','NodedTreeKeyStr'])

#Definition the AttestedStr
SYS._attest(
	[
		'MyGrabber is '+SYS._str(
		MyGrabber,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
) 

#Print

 