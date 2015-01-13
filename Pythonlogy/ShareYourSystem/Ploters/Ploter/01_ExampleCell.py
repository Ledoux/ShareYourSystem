
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Ploters import Ploter
from numpy import random

#Define

MyPloter=Ploter.PloterClass().plot(
		random.rand(100),
		random.rand(100)
	)

#Definition the AttestedStr
SYS._attest(
	[
		'MyPloter is '+SYS._str(
		MyPloter,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
	]
) 

#Print

