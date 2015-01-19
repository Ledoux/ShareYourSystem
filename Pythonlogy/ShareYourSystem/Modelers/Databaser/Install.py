#ImportModules
import os
from ShareYourSystem.Objects import Installer

#Install
Installer.InstallerClass().install(**{
			'InstallingPathStr':os.getcwd()+"/"
			}
		)

