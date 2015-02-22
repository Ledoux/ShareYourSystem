#ImportModules
from ShareYourSystem.Standards.Classors import Attester
from ShareYourSystem.Functers import Functer

#Definition a derived second Class
class FooClass():

	@Functer.FuncterClass()
	def printSomething(self,**_KwargVariablesDict):
		print('Something !')

	#Functers can be cumulated
	@Functer.FuncterClass()
	@Functer.FuncterClass()
	def printOtherthing(self,**_KwargVariablesDict):
		print('An Other Thing ?')

#Definition an instance
MyFoo=FooClass()

#Do just a test of the basic FirstClass method printSomething
MyFoo.printSomething()

#Do just a test of the basic FirstClass method printSomething
MyFoo.printOtherthing()
