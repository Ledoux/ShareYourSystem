#ImportModules
import ShareYourSystem as SYS

#Definition a Deployer
try:
	MyDeployer=SYS.DeployerClass().deploy()
except:
	MyDeployer=SYS.DeployerClass()
	
#Definition the AttestedStr
SYS._attest(
	[
		'MyDeployer is '+SYS._str(
		MyDeployer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
)  

#Print



