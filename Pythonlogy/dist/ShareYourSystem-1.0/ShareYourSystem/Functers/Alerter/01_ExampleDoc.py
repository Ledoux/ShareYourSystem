#ImportModules
from ShareYourSystem.Classors import Attester
from ShareYourSystem.Functers import Alerter
from ShareYourSystem.Objects import Debugger

#Definition a derived second Class
class FooClass(Debugger.DebuggerClass):

	@Alerter.AlerterClass()
	def printSomething(self,**_KwargVariablesDict):
		self._print('Something !')

#Definition an instance
MyFoo=FooClass()

#Do just a test of the basic FirstClass method printSomething
MyFoo.printSomething()

