#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Standards.Interfacers import Loader

#Definition of an instance Loader and make it find the current dir
MyLoader=Loader.LoaderClass().file('MyFile.txt','w')
MyLoader.FiledHardVariable.write('hello')
MyLoader.FiledHardVariable.close()
MyLoader.load()
	
#Definition the AttestedStr
SYS._attest(
	[
		'MyLoader is '+SYS._str(MyLoader,
			**{'RepresentingAlineaIsBool':False}
		)
	]
) 

#Print

