
#Hooker


    #import Modules
    from ShareYourSystem.Standards.Classors.Representer import _print
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
            
    #Call the hooked printSomething method of the SecondClass
    SecondClass().printSomething();

    First
    Second



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
