#Hooker
	
Hooker helps for hooking a call of a method with the one from another function. 

```python
import ShareYourSystem as SYS

#Definition a first Class
class FirstClass(object):

	def printSomething(self,**_VariablesDict):
		print('First')

#Definition a derived second Class
class SecondClass(FirstClass):

	@SYS.HookerClass(**{'AfterTuplesList':[(FirstClass,'printSomething')]})
	def printSomething(self,**_VariablesDict):
		print('Second')
```

In this code, an instance of FirstClass will just print "First" when printSomething is called :

```console
>>>FirstClass().printSomething()
First
>>>
```

Now, the equivalent but hooked method in the Second Class will 
first call FirstClass.printSomething(self,) then SecondClass.printSomething(self,): 

```console
>>>SecondClass().printSomething()
First
Second
>>>
```

