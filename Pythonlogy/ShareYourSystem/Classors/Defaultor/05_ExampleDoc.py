#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Defaultor,Attester
from ShareYourSystem.Objects import Initiator

#Definition a FooClass decorated by the DefaultorClass
@Defaultor.DefaultorClass()
class FooClass(Initiator.InitiatorClass):

	def default_init(self,
						_MyShareInitiator=Initiator.InitiatorClass()
				):
		pass

#Definition 
FooClass.MyShareInitiator.MyInt=2
MyFirstFoo=FooClass()
MySecondFoo=FooClass()

#Definition the AttestedStr
AttestingStrsList=[
		'MyFirstFoo.MyShareInitiator.__dict__ is ',str(MyFirstFoo.MyShareInitiator.__dict__)
	]

#Print
#print(AttestingStrsList)

#Definition
SYS._attest(AttestingStrsList)

#Print

