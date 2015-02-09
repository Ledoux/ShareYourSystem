#ImportModules
import ShareYourSystem as SYS

#Definition a Statuser
MyStatuser=SYS.StatuserClass().status('mongod')

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


