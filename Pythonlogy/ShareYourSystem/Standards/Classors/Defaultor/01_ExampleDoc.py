#ImportModules
import ShareYourSystem as SYS

#Definition a FooClass decorated by the DefaultorClass
@SYS.DefaultorClass()
class FooClass(SYS.InitiatorClass):

	def default_init(self,
						Int,
						_MyFloat=1.,
						_MyInt={
									'DefaultingSetType':int
								}
				):
		
		#Definition an attribute
		self.MyStr='I am a Foo with MyFloat equal to '+str(self.MyFloat)+' and Int equal to '+str(Int)

#Definition a default instance that will take its values from the default classed attributes
DefaultFoo=FooClass(3)

#Definition a special instance that sets in its __dict__
SpecialFoo=FooClass(
			3,
			**{'MyInt':3}
			)

#Definition the AttestedStr
AttestingStrsList=[
		'FooClass.__init__ is '+str(FooClass.__init__),
		'FooClass has some special attributes',
		#'FooClass.InitArgumentDict is '+SYS._str(FooClass.InitArgumentDict),
		'FooClass.DefaultAttributeVariablesOrderedDict is '+str(
			FooClass.DefaultAttributeVariablesOrderedDict),
		'FooClass.MyFloat is '+str(FooClass.MyFloat),
		'FooClass.MyInt is '+str(FooClass.MyInt),
		'What are you saying DefaultFoo ?',
		'DefaultFoo.__dict__ is '+str(DefaultFoo.__dict__),
		'DefaultFoo.MyFloat is '+str(DefaultFoo.MyFloat),
		'DefaultFoo.MyInt is '+str(DefaultFoo.MyInt),
		'What are you saying SpecialFoo ?',
		'SpecialFoo.__dict__ is '+str(SpecialFoo.__dict__),
		'SpecialFoo.MyFloat is '+str(SpecialFoo.MyFloat),
		'DefaultFoo.MyInt is '+str(SpecialFoo.MyInt)
	]

#Change a classed attribute
FooClass.MyFloat=5

#Add
AttestingStrsList+=[
		'After reset at the level of the class',
		'DefaultFoo.MyFloat is '+str(DefaultFoo.MyFloat),
		'SpecialFoo.MyFloat is '+str(SpecialFoo.MyFloat),
	]

#Print
#print(AttestingStrsList)

#Definition
SYS._attest(AttestingStrsList)

#Print

