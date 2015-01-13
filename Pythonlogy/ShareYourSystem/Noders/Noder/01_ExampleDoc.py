
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Noder
		
#Definition of a Noder instance
MyNoder=Noder.NoderClass()

#Short expression for setting in the appended manner a structured object
MyNoder['<Nodome>FirstChildNoder']=Noder.NoderClass()

#Short expression for setting in the appended manner a structured object
MyNoder['<Nodome>SecondChildNoder']=Noder.NoderClass()

#Definition the AttestedStr
SYS._attest(
	[
		'MyNoder is '+SYS._str(
				MyNoder,
				**{
				'RepresentingBaseKeyStrsListBool':False,
				'RepresentingAlineaIsBool':False
				}
			)
	]
) 

#Print

