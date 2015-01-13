'''
```python
'''

#ImportModules



#import Modules
from ShareYourSystem.Classors.Representer import _print
from ShareYourSystem.Functers import Hooker

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
