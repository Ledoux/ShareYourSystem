#ImportModules
import ShareYourSystem as SYS

#Definition a FooClass decorated by the DefaultorClass
@SYS.DefaultorClass()
class FooClass(SYS.ObjectClass):

	def default_init(self,
						_MyFloat=1.,
						_MyShareList=[],
						_MyFirstSpecificList=None,
						_MySecondSpecificList=None,
						_MyInt={
									'DefaultingSetType':int
								}
				):
		SYS.ObjectClass.__init__(self)

#Definition 
MyFoo=FooClass(**{'MyFloat':5.,'MyInt':9})
MyFoo.MyShareList.append(7)
MyFoo.MyFirstSpecificList=['hello']

#Before default
print('Before setDefault MyFoo.__dict__ is')
print(MyFoo.__dict__)

#default
MyFoo.setDefault(
	FooClass,
	#['MyFloat']
)

#After default
print('After setDefault MyFoo.__dict__ is')
print(MyFoo.__dict__)

#Reset some mutable things
MyFoo.MyInt=5
MyFoo.MyFirstSpecificList=['hello']

#After default
print('After a re set MyFoo.__dict__ is')
print(MyFoo.__dict__)

#default
MyFoo.setDefaultMutable(
	FooClass,
	#['MyFloat']
	**{'ForceSetIsBool':True}
)

#After default
print('After a forced setDefaultMutable MyFoo.__dict__ is')
print(MyFoo.__dict__)

#Reset some mutable things
MyFoo.MyInt=5
MyFoo.MyFirstSpecificList=['hello']
MyFoo.MySecondSpecificList=None

#After default
print('After a re set MyFoo.__dict__ is')
print(MyFoo.__dict__)

#default
MyFoo.setDefaultMutable(
	FooClass,
	#['MyFloat']
)

#After default
print('After a non forced setDefaultMutable MyFoo.__dict__ is')
print(MyFoo.__dict__)

#Definition the AttestedStr
print("\n".join(
	[
		'FooClass.DefaultAttributeVariablesOrderedDict is '+str(
			FooClass.DefaultAttributeVariablesOrderedDict),
		'MyFoo.__dict__ is ',str(MyFoo.__dict__)
	]
	)
)


