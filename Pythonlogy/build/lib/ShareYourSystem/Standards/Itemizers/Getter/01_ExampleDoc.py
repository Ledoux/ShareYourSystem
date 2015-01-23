
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Standards.Itemizers import Getter

#Definition a Getter
MyGetter=Getter.GetterClass()
MyGetter.MyInt=1
		
#Definition the AttestedStr
SYS._attest(
	[
		'Get the MyInt returns '+str(MyGetter['MyInt']),
		'Get the MyStr returns '+str(MyGetter['MyStr'])
	]
) 

#Print

