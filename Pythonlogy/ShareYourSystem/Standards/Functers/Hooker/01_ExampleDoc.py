#ImportModules
from ShareYourSystem.Standards.Classors import Attester
from ShareYourSystem.Functers import Hooker

#Definition a derived second Class
class FooClass():

	def printSomething(self,**_KwargVariablesDict):
		print('Something !')

	@Hooker.HookerClass(**{'HookingAfterVariablesList':[
		{'CallingMethodStr':'printSomething'}]}
	)
	def printOtherthing(self,**_KwargVariablesDict):
		print('An Other Thing ?')

#Definition an instance
MyFoo=FooClass()

#Do a printOtherThing hooked with printSomething
MyFoo.printOtherthing()
