#ImportModules
import ShareYourSystem as SYS

from ShareYourSystem.Interfacers import Folderer,Deployer

#Definition a Deployer
try:
	MyDeployer=Deployer.DeployerClass().deploy()
except:
	MyDeployer=Deployer.DeployerClass()
	
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



