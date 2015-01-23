#ImportModules
import ShareYourSystem as SYS

#Definition a FooClass decorated by the DefaultorClass
@SYS.DefaultorClass()
class FooClass(SYS.InitiatorClass):

	def default_init(self,
						_MyShareInitiator=SYS.InitiatorClass()
				):
		pass

#Definition 
FooClass.MyShareInitiator.MyInt=2
MyFirstFoo=FooClass()
MySecondFoo=FooClass()

#Definition the AttestedStr
AttestingStrsList=[
		'MyFirstFoo.MyShareInitiator.__dict__ is ',str(
			MyFirstFoo.MyShareInitiator.__dict__)
	]

#Print
#print(AttestingStrsList)

#Definition
SYS._attest(AttestingStrsList)

#Print

