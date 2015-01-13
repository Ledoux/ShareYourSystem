#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Interfacers import Statuser
import os

#Definition a Statuser
MyStatuser=Statuser.StatuserClass().status('Python')

#Definition the AttestedStr
SYS._attest(
	[
		'MyStatuser is '+SYS._str(
		MyStatuser,
		**{
			'RepresentingBaseKeyStrsListBool':False
		}
		)
	]
)  

#Print


