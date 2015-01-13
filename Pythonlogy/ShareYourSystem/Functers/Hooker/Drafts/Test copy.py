'''
```python
'''

#import Modules
import tables
from ShareYourSystem.Classors import Attester
from ShareYourSystem.Objects import Structurer

#Definition a first Class
class FirstClass(object):

	def printSomething(self,**_KwargVariablesDict):
		_print('First')

#Definition a derived second Class
class SecondClass(FirstClass):

	@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':FirstClass.printSomething}]})
	def printSomething(self,**_KwargVariablesDict):
		_print('Second')

'''
```

In this code, an instance of FirstClass will just print "First" when printSomething is called :
```console

'''

FirstClass().printSomething()

'''
First
```

Now, the equivalent but hooked method in the Second Class will 
first call FirstClass.printSomething(self,) then SecondClass.printSomething(self,): 
```console
'''

SecondClass().printSomething()


'''
```
'''







'''
```python
'''

#import Modules
import tables
from ShareYourSystem.Classors import Attester
from ShareYourSystem.Objects import Structurer

#Definition a first Class
class FirstClass(object):

	def printSomething(self,**_KwargVariablesDict):
		_print('First')

#Definition a derived second Class
class SecondClass(FirstClass):

	@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':FirstClass.printSomething}]})
	def printSomething(self,**_KwargVariablesDict):
		_print('Second')

	@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingMethodStr':'printSomething'}]})
	def printOtherThing(self,**_KwargVariablesDict):
		_print('Third')

	@Hooker.HookerClass(**{'HookingAfterVariablesList':[{
													'CallingMethodStr':'printSomething',
													'CallingClass':FirstClass
													}]}
	)
	def printAnyThing(self,**_KwargVariablesDict):
		_print('BlaBleuBliBlouBleu')

'''
```
'''


	#Do just a test of the basic FirstClass method printSomething
	FirstClass().printSomething()
	print('')

	#Do a test of the hooked SecondClass method printSomething
	SecondClass().printSomething()
	print('')

	#Do a test of the hooked SecondClass method printOtherThing
	SecondClass().printOtherThing()
	print('')

	#Do a test of the hooked SecondClass method printOtherThing
	SecondClass().printAnyThing()
	print('')

	#Print the hooked method
	_print(SecondClass.printSomething)

#</DefineAttestingFunctions>