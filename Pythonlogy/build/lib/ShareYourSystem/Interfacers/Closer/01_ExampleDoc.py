#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Interfacers import Closer

#Definition of an instance Closer and make it find the current dir
MyCloser=Closer.CloserClass().file('MyFile.txt','w').close()
	
#Definition the AttestedStr
SYS._attest(
	[
		'MyCloser is '+SYS._str(
			MyCloser,
			**{
				'RepresentingAlineaIsBool':False
			}
		)
	]
) 

#Print

