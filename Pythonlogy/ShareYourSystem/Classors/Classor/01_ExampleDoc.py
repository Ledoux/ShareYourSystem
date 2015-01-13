#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Classor,Attester

#Definition a FooClass decorated by the ClassorClass
@Classor.ClassorClass()
class FooClass():
	pass

#Definition the AttestedStr
SYS._attest(
	[
		'FooClass.KeyStrsList is '+str(FooClass.KeyStrsList),
		'FooClass.NameStr is '+FooClass.NameStr,
		'FooClass.DeriveClassor is '+str(FooClass.DeriveClassor)	
	]
) 

#Print
