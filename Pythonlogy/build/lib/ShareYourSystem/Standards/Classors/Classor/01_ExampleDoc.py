#ImportModules
import ShareYourSystem as SYS

#Definition a FooClass decorated by the ClassorClass
@SYS.ClassorClass()
class FooClass(object):
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