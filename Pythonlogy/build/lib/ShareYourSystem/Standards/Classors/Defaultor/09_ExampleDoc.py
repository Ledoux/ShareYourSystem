#ImportModules
import ShareYourSystem as SYS

#Definition a FooClass decorated by the DefaultorClass
@SYS.DefaultorClass()
class FooClass(object):

	def default_init(self,
						_MyFloat=1.,
						_MyShareList=[],
						_MyFirstSpecificList=None,
						_MySecondSpecificList=None,
						_MyInt={
									'DefaultValueType':int
								}
				):
		object.__init__(self)

#Definition a FeeClass decorated by the DefaultorClass
@SYS.DefaultorClass()
class FeeClass(FooClass):

	def default_init(self,
						_MyBool=True,
				):
		FooClass.__init__(self)

#Definition 
MyFee=FeeClass(**{'MyFloat':5.,'MyInt':9,'MyBool':False})

#Before default
print('Before setDefault MyFee.__dict__ is')
print(SYS.indent(MyFee.__dict__))

#default
MyFee.setDefault(
	#ClassVariable,
	[FooClass,'FeeClass'],
	#AttributeKeyStrsList,
	'MyFloat'
)

#After default
print('\nAfter setDefault MyFee.__dict__ is')
print(SYS.indent(MyFee.__dict__))

#default
MyFee.setDefault(
	#ClassVariable
	#it can be a Class, ClassKeyStr or [Class]
	FooClass,
	#AttributeKeyStrsList 
	#it can be just a KeyStr a [<KeyStr>] and if None it is all the KeyStr from all the Classes
	['MyFloat','MyFirstSpecificList']
)

#append to the share list
MyFee.MyShareList.append(8)

#After default
print('\nAfter setDefault MyFee.__dict__ is')
print(SYS.indent(MyFee.__dict__))

#define
print('\nFooClass.DefaultAttributeVariablesOrderedDict is '+SYS.indent(
			FooClass.DefaultAttributeVariablesOrderedDict)
)

#print
print('\nMyFee.__dict__ is ')
print(SYS.indent(MyFee.__dict__))



