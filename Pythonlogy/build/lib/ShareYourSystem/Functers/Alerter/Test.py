#Import Modules
from ShareYourSystem.Classors import Representer,Doer
from ShareYourSystem.Classors.Representer import _print
from ShareYourSystem.Functers import Alerter
from ShareYourSystem.Objects import Debugger

#Print a version of the class
_print(dict(Alerter.AlerterClass.__dict__.items()))

#Print a version of this object
_print(Alerter.AlerterClass())

#Print a version of his __dict__
_print(Alerter.AlerterClass().__dict__)

#Definition a first Class
class FooerClass(Debugger.DebuggerClass):

	@Alerter.AlerterClass(**{'AlertingDebugBool':True})
	def foo(self,**_VariablesDict):
		self._print('First')

	@Alerter.AlerterClass(**{'AlertingDebugBool':True})
	def _foo(self,**_VariablesDict):
		self.foo()
		self._print('Second')

#Do just a test of the basic FirstClass method printSomething
FooerClass()._foo()

'''
#Definition a first Class
class FooerClass(SYS.DebuggerClass):

	@SYS.AlerterClass(**{'AlertingDebugBool':True})
	def foo(self,**_VariablesDict):
		self.FooDict={'ChildDict':{'MyStr':"hello"},"MyInt":0}
		self._print(self)

	@SYS.AlerterClass(**{'AlertingDebugBool':True})
	def _foo(self,**_VariablesDict):
		self.foo()
		print(self)

#Do just a test of the basic FirstClass method printSomething
FooerClass()._foo()
'''
