

<!--
FrozenIsBool False
-->

#Restricter

##Doc
----


>
> A Restricter object sets only in the __dict__ only if
hasattr(self,self.SettingKeyVariable)
> returns True before.
>
>

----

<small>
View the Restricter notebook on [NbViewer](http://nbviewer.ipython.org/url/share
yoursystem.ouvaton.org/Restricter.ipynb)
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


A Restricter object sets only in the __dict__ only if
hasattr(self,self.SettingKeyVariable)
returns True before.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Itemizers.Attributer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class RestricterClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'RestrictingIsBool',
'RestrictingKeyStr',
'RestrictedSetIsBool'
                                                        ]

        def default_init(self,
                                _RestrictingIsBool=False,
                                _RestrictingKeyStr=None,
                                _RestrictedSetIsBool=True,
                                **_KwargVariablesDict
                                ):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_restrict(self):

                #Init
                self.RestrictedSetIsBool=True

                #debug
                '''
self.debug(('self.',self,['RestrictingIsBool','RestrictingKeyStr']))
                '''

                #Check
                if self.RestrictingIsBool:

                        #Check
                        if hasattr(self,self.RestrictingKeyStr):
                                self.RestrictedSetIsBool=False

                else:

                        #set to False
                        self.RestrictedSetIsBool=False

#<Hook>@Hooker.HookerClass(**{'HookingAfterVariablesList':[BaseClass.set]})
        #@Imitater.ImitaterClass()
        def mimic_set(self):
                """ """

                #debug
                '''
self.debug(('self.',self,['SettingKeyVariable','SettingValueVariable']))
                '''

                #Definition
                OutputDict={'HookingIsBool':True}

                #debug
                '''
                self.debug('We are going to restrict')
                '''

                #restrict
                self.restrict(_KeyStr=self.SettingKeyVariable)

                #<Hook>
                #Stop the setting
                if self.RestrictedSetIsBool:
                        OutputDict["HookingIsBool"]=False
                        return OutputDict
                #</Hook>

                #Debug
                '''
                self.debug(
                                        [
                                                'BaseClass is '+str(BaseClass),
                                                'BaseClass.set is
'+str(BaseClass.set),
                                        ]
                                )
                '''

                #Call the parent set method
                return BaseClass.set(self)

#</DefineClass>


```

<small>
View the Restricter sources on <a href="https://github.com/Ledoux/ShareYourSyste
m/tree/master/Pythonlogy/ShareYourSystem/Itemizers/Restricter"
target="_blank">Github</a>
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
from ShareYourSystem.Itemizers import Restricter

#Explicit expression
MyRestricter=Restricter.RestricterClass(**{'RestrictingIsBool':True})
MyRestricter.ResettedStr="Hello"
MyRestricter.__setitem__('ResettedStr',"Bonjour")
MyRestricter.__setitem__('NotsettedFloat',1.)

#Return
SYS._attest(
    [
    'MyRestricter is '+SYS._str(
            MyRestricter,
            **{
            'RepresentingBaseKeyStrsListBool':False,
            'RepresentingAlineaIsBool':False
            }
        )
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

MyRestricter is < (RestricterClass), 4554378320>
   /{
   /  '<New><Instance>IdInt' : 4554378320
   /  '<New><Instance>ResettedStr' : Bonjour
   /  '<Spe><Instance>RestrictedSetIsBool' : True
   /  '<Spe><Instance>RestrictingIsBool' : True
   /  '<Spe><Instance>RestrictingKeyStr' : NotsettedFloat
   /}

*****End of the Attest *****



```

