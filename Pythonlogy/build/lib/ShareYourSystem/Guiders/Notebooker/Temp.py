#ImportModules
from ShareYourSystem.Classors import Attester
from ShareYourSystem.Objects import Hdformater

#Definition a Hdformater that writes an empty hdf file
MyHdformater=Hdformater.HdformaterClass().hdformat().hdfview().hdfclose()
#.hdfview().hdfclose()

#Definition the AttestedStr
SYS._attest(
					[
						'MyHdformater.HdformatedStr is '+str(
							MyHdformater.HdformatedStr)
					]
				) 

#Print




#import os
#os.popen('import os;os.popen('')')