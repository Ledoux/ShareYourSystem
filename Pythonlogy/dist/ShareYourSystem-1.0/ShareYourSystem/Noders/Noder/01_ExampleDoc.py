
#ImportModules
import ShareYourSystem as SYS
		
#Definition of a Noder instance
MyNoder=SYS.NoderClass()

#Short expression for setting in the appended manner a structured object
MyNoder['<Noders>FirstChildNoder']=SYS.NoderClass()

#Short expression for setting in the appended manner a structured object
MyNoder['<Noders>SecondChildNoder']=SYS.NoderClass()

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

