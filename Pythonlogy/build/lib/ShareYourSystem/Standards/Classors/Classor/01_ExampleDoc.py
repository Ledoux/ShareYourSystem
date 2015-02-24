#ImportModules
import ShareYourSystem as SYS

#Definition a FooClass decorated by the ClassorClass
@SYS.ClassorClass()
class FooClass(object):
	pass

#print
print('FooClass.KeyStrsList is '+str(FooClass.KeyStrsList))
print('FooClass.NameStr is '+FooClass.NameStr)
print('FooClass.DeriveClassor is '+str(FooClass.DeriveClassor))