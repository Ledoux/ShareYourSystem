#ImportModules
import ShareYourSystem as SYS

#Definition a FooClass decorated by the DefaultorClass
@SYS.DefaultorClass()
class FooClass(SYS.ObjectClass):

	def default_init(self,
						_ShareObject=SYS.ObjectClass()
				):
		SYS.ObjectClass.__init__(self)

#Definition 
FooClass.ShareObject.MyInt=2
MyFirstFoo=FooClass()
MySecondFoo=FooClass()

#Definition the AttestedStr
print("\n".join(
	[
		'MyFirstFoo.ShareObject.__dict__ is ',str(
			MyFirstFoo.ShareObject.__dict__)
	]
	)
)


