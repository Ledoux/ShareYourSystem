#ImportModules
from ShareYourSystem.Standards.Objects import Initiator

#Definition a derived class of the InitiatorClass
class FooClass(Initiator.InitiatorClass):

	def default_init(self,**_KwargVariablesDict):

		#Definition the attributes
		self.InitiatingInt=0
		self.InitiatingStr=""

		Initiator.InitiatorClass.__init__(self,**_KwargVariablesDict)

#Print a version of the class
print(dict(FooClass.__dict__.items()))

#Print a version of this object
print(FooClass(**{'InitiatingInt':2,'InitiatingStr':"hello"}))

#Print a version of his __dict__, InitiatingStr should not appear
print(FooClass(**{'InitiatingInt':2,'InitiatingStr':"hello"}).__dict__)
