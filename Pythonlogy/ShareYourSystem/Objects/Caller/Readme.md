

<!--
FrozenIsBool False
-->

#Caller

##Doc
----


>
> The Caller is an Object that helps to get an make call a function/method.
>
>

----

<small>
View the Caller notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyour
system.ouvaton.org/Caller.ipynb)
</small>




<!--
FrozenIsBool False
-->

##Code

----

<ClassDocStr>

----

```python
# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Caller is an Object that helps to get an make call a function/method.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Objects.Packager"
DecorationModuleStr="ShareYourSystem.Classors.Tester"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import sys
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class CallerClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'CallingVariable',
'CallingFunctionStr',
                                                                'CallingMethod',
'CallingMethodStr',
'CallingInstanceVariable',
                                                                'CallingClass',
'CallingClassStr',
                                                        ]

        def default_init(self,
                                                _CallingVariable=None,
                                                _CallingFunctionStr="",
                                                _CallingMethod=None,
                                                _CallingMethodStr="",
                                                _CallingInstanceVariable=None,
                                                _CallingClass=None,
                                                _CallingClassStr="",
                                                **_KwargVariablesDict
                                        ):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        #<DefineDoMethod>
        def do_call(self):

                #Module first to know where we are
                self.package()

                #debug
                '''
                print("self.CallingVariable is ",self.CallingVariable)
                print('')
                '''

                #If it was not yet setted or changed
                if self.CallingVariable==None or
self.CallingVariable.__name__!=self.CallingFunctionStr:

                        #debug
                        '''
                        print('Get in the module')
                        print('self.PackagingModuleVariable is
'+str(self.PackagingModuleVariable))
                        print('')
                        '''

                        #Get maybe the one in the module
                        if self.CallingFunctionStr!="":

                                #debug
                                '''
                                print('Get in the module with the function Str')
                                print('self.CallingFunctionStr is
',self.CallingFunctionStr)
                                print('')
                                '''

                                #Get and return
                                self.CallingVariable=getattr(self.PackagedModule
Variable,self.CallingFunctionStr)
                                return self

                #Get the function
                if self.CallingVariable==None or
self.CallingVariable.__name__!=self.CallingMethodStr:

                        #debug
                        '''
                        print('Get in a class')
                        print('self.PackagingModuleVariable is
'+str(self.PackagingModuleVariable))
                        print('self.CallingVariable is ',self.CallingVariable)
                        print('self.CallingMethodStr is ',self.CallingMethodStr)
                        print('self.CallingClass is ',self.CallingClass)
                        print('self.CallingClassStr is ',self.CallingClassStr)
                        print('self.CallingInstanceVariable is
',self.CallingInstanceVariable)
                        print('')
                        '''

                        #Get with the CallingInstanceVariable class maybe
                        if self.CallingClass==None and
self.CallingInstanceVariable!=None:
self.CallingClass=self.CallingInstanceVariable.__class__

                        #Import the module if not already
                        if self.CallingClass==None:
                                if self.CallingClassStr!="":
self.CallingClass=getattr(self.PackagedModuleVariable,self.CallingClassStr)
                                else:
                                        self.CallingClass=getattr(
self.PackagedModuleVariable,
SYS.getClassStrWithNameStr(
SYS.getNameStrWithModuleStr(self.PackagedModuleVariable.__name__)
)
                                                                        )


                        #debug
                        '''
                        print('Now get the unbounded method function')
                        print('self.CallingClass is '+str(self.CallingClass))
                        print('')
                        '''

                        #Check
                        if self.CallingMethodStr!="":

                                #debug
                                '''
                                print('self.CallingMethodStr is
',self.CallingMethodStr)
                                print('')
                                '''

                                #Return
self.CallingVariable=getattr(self.CallingClass,self.CallingMethodStr)

                #Return
                #return self

#</DefineClass>


```

<small>
View the Caller sources on [Github](https://github.com/Ledoux/ShareYourSystem/tr
ee/master/ShareYourSystem/Objects/Caller)
</small>




<!---
FrozenIsBool True
-->

##Example

Let's create an empty class, which will automatically receive
special attributes from the decorating ClassorClass,
specially the NameStr, that should be the ClassStr
without the TypeStr in the end.

```python
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Objects import Caller

#Definition of a Caller instance
MyCaller=Caller.CallerClass()

#Call the _print from the Rep
MyCaller.call(
    _FunctionStr='represent',
    **{
        'PackagingModuleVariable':'ShareYourSystem.Classors.Representer',
    }
)

#Definition the AttestedStr
SYS._attest(
    [
        'MyCaller is '+SYS._str(
        MyCaller,
        **{
            'RepresentingBaseKeyStrsListBool':False
        }
        )
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

MyCaller is < (CallerClass), 4457587792>
   /{
   /  '<New><Instance>IdInt' : 4457587792
   /  '<Spe><Class>CallingClass' : None
   /  '<Spe><Class>CallingClassStr' :
   /  '<Spe><Class>CallingInstanceVariable' : None
   /  '<Spe><Class>CallingMethod' : None
   /  '<Spe><Class>CallingMethodStr' :
   /  '<Spe><Instance>CallingFunctionStr' : represent
   /  '<Spe><Instance>CallingVariable' : <function Watcher@represent at
0x10990a2a8>
   /}

*****End of the Attest *****



```

