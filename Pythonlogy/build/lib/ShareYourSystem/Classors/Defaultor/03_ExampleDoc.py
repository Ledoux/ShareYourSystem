#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Defaultor,Attester
from ShareYourSystem.Objects import Initiator
import numpy as np

#Definition a FooClass decorated by the DefaultorClass
@Defaultor.DefaultorClass()
class FooClass(Initiator.InitiatorClass):

	def default_init(self,
						_MyFirstList=[],
						_MyArray=None,
						_MySecondList=None,
				):
		pass

#Definition a default instance that will take its values from the default classed attributes
DefaultFoo=FooClass()

#But it can touch at the mutable values defined in the class
DefaultFoo.MyFirstList.append('hello')

#Note: if you write DefaultFoo.MyFirstList=['hello'], 
#then it will set it as a new list in the __dict__ of the DefaultFoo.

#Definition a special instance that sets in its __dict__
SpecialFoo=FooClass(
			_MyArray=np.array([4]),
			_MySecondList=['bonjour'],
			**{'MyInt':3}
			)

#Definition the AttestedStr
AttestingStrsList=[
		'FooClass has some special attributes',
		#'FooClass.InitArgumentDict is '+SYS._str(FooClass.InitArgumentDict),
		'FooClass.DefaultAttributeVariablesOrderedDict is '+str(
			FooClass.DefaultAttributeVariablesOrderedDict),
		'FooClass.MyFirstList is '+str(FooClass.MyFirstList),
		'FooClass.MySecondList is '+str(FooClass.MySecondList),
		'What are you saying DefaultFoo ?',
		'DefaultFoo.__dict__ is '+str(DefaultFoo.__dict__),
		'DefaultFoo.MyFirstList is '+str(DefaultFoo.MyFirstList),
		'DefaultFoo.MySecondList is '+str(DefaultFoo.MySecondList),
		'What are you saying SpecialFoo ?',
		'SpecialFoo.__dict__ is '+str(SpecialFoo.__dict__),
		'SpecialFoo.MyFirstList is '+str(SpecialFoo.MyFirstList),
		'SpecialFoo.MySecondList is '+str(SpecialFoo.MySecondList),
	]

#Print
#print(AttestingStrsList)

#Definition
SYS._attest(AttestingStrsList)

#Print

