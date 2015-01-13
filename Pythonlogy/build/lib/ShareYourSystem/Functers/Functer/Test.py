#Import Modules
from ShareYourSystem.Functers import Functer,Hooker
from ShareYourSystem.Classors import Representer
from ShareYourSystem.Classors.Representer import _print
from ShareYourSystem.Functers import Functer

#Print a version of the class
_print(dict(Functer.FuncterClass.__dict__.items()))

#Print a version of this object
_print(Functer.FuncterClass())

#Print a version of his __dict__
_print(Functer.FuncterClass().__dict__)

#Definition a first Class
class FirstClass(object):

	def printSomething(self,**_KwargVariablesDict):
		_print('First')

#Definition a derived second Class
class SecondClass(FirstClass):

	@Functer.FuncterClass()
	def printSomething(self,**_KwargVariablesDict):
		_print('Second')

	@Functer.FuncterClass()
	@Functer.FuncterClass()
	def printOtherthing(self,**_KwargVariablesDict):
		_print('Third')

#Reset
Representer.RepresentedAlineaStr=""

#Do just a test of the basic FirstClass method printSomething
FirstClass().printSomething()

#Do a test of the hooked SecondClass method printSomething
SecondClass().printSomething()

#Do a test of the hooked SecondClass method printOtherthing to see that functors can be accumulated
SecondClass().printOtherthing()

#Print the 
_print(dict(SecondClass.__dict__.items()))