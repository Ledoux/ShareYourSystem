
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Guiders import Installer

#Definition a Installer instance
MyInstaller=Installer.InstallerClass().install(_AllBool=True)	

#Definition the AttestedStr
SYS._attest(
	[
		'MyInstaller is '+SYS._str(
		MyInstaller,
		**{
			'RepresentingBaseKeyStrsListBool':False
		}
		)
	]
)  

#Print






