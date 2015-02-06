

<!--
FrozenIsBool False
-->

#Recuperater

##Doc
----


>
> Recuperater instances
>
>

----

<small>
View the Recuperater notebook on [NbViewer](http://nbviewer.ipython.org/url/shar
eyoursystem.ouvaton.org/Recuperater.ipynb)
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


Recuperater instances

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Databasers.Joiner"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>


#<DefineClass>
@DecorationClass()
class RecuperaterClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'RecuperatingRetrieveList'
                                                                ]

        #@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':
BaseClass.__init__}]})
        def default_init(self,
                                                _RecuperatingRetrieveList=None,
                                                **_KwargVariablesDict
                                        ):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_recuperate(self):

                #retrieve
                self.retrieve(self.RecuperatingRetrieveList)

                #debug
                self.debug(('self',self,['RetrievedPickOrderedDict']))


#</DefineClass>


```

<small>
View the Recuperater sources on <a href="https://github.com/Ledoux/ShareYourSyst
em/tree/master/Pythonlogy/ShareYourSystem/Databasers/Recuperater"
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
from ShareYourSystem.Classors import Classer
from ShareYourSystem.Functers import Triggerer
from ShareYourSystem.Noders import Structurer
from ShareYourSystem.Databasers import Featurer,Recuperater
import tables
import operator

MyRecuperater=Recuperater.RecuperaterClass()

#Definition the AttestedStr
SYS._attest(
    [
        'MyRecuperater is '+SYS._str(
        MyRecuperater,
        **{
            'RepresentingBaseKeyStrsListBool':False,
            'RepresentingAlineaIsBool':False
        }
        ),
        'hdf5 file is : '+MyRecuperater.hdfview().hdfclose().HdformatedConsoleStr
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

MyRecuperater is < (RecuperaterClass), 4565656784>
   /{
   /  '<New><Instance>IdInt' : 4565656784
   /  '<New><Instance>NewtorkAttentionStr' :
   /  '<New><Instance>NewtorkCatchStr' :
   /  '<New><Instance>NewtorkCollectionStr' :
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopRecuperater
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<Spe><Class>RecuperatingRetrieveList' : None
   /}

------

hdf5 file is :

*****End of the Attest *****



```

