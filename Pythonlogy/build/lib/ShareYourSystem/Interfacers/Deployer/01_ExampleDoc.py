#ImportModules
import ShareYourSystem as SYS

from ShareYourSystem.Interfacers import Folderer,Deployer

#Definition a Deployer
MyDeployer=Deployer.DeployerClass().deploy()

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



