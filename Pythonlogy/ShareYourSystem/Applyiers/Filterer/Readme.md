

<!--
FrozenIsBool False
-->

#Filterer

##Doc
----


>
> A Filterer pick and
>
>

----

<small>
View the Filterer notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyo
ursystem.ouvaton.org/Filterer.ipynb)
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


A Filterer pick and

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Itemizers.Pointer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
import collections
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class FiltererClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'FilteringGetVariable',
'FilteredGetVariable',
'FilteredVariablesList'
                                                                ]

        def default_init(self,
                                _FilteringGetVariable=None,
                                _FilteredGetVariable=None,
                                _FilteredVariablesList=None,
                                **_KwargVariablesDict):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_filter(self):

                #debug
                '''
                self.debug(('self.',self,[
'PickingGetKeyVariablesList',
'ConcludingConditionTuplesList',
'FilteringGetVariable'
                                                                ])
                                )
                '''

                #Get
                if type(self.FilteringGetVariable) in SYS.StrTypesList:
                        self.FilteredGetVariable=self[self.FilteringGetVariable]
                else:
                        self.FilteredGetVariable=self.FilteringGetVariable

                #Check
                if self.conclude(self.FilteredGetVariable).ConcludedIsBool:

                        #debug
                        '''
                        self.debug(
                                        (
                                                'self.',self,[
'PickingGetKeyVariablesList',
'ConcludedConditionIsBoolsList',
]+SYS.unzip(
self.ConcludingConditionTuplesList,[0]
                                                                        )
                                        )
                                )
                        '''

                        #Pick
                        self.FilteredVariablesList=self.pick()


#</DefineClass>

```

<small>
View the Filterer sources on <a href="https://github.com/Ledoux/ShareYourSystem/
tree/master/Pythonlogy/ShareYourSystem/Applyiers/Filterer"
target="_blank">Github</a>
</small>



```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Applyiers import Filterer
import operator

#Definition a Filter instance that is grouped
MyFilterer=Filterer.FiltererClass().update(
    [
        ('NodeIndexInt',1),
        ('NodeKeyStr','MyFilterer'),
        (
            'ConcludingConditionTuplesList',[
                        (
                            'NodeIndexInt',
                            lambda _TestInt,_AttestInt:
                                operator.lt(_TestInt,_AttestInt)
                                if _TestInt!=None else False,
                            2
                        )
                    ]
                ),
        (
            'PickingGetKeyVariablesList',['NodeKeyStr']
        )
    ]
).filter('/')


#Definition the AttestedStr
SYS._attest(
    [
        'MyFilterer is '+SYS._str(
        MyFilterer,
        **{
            'RepresentingBaseKeyStrsListBool':False,
            'RepresentingAlineaIsBool':False
        }
        )
    ]
)



```


```console
>>>


*****Start of the Attest *****

MyFilterer is < (FiltererClass), 4555338640>
   /{
   /  '<New><Instance>IdInt' : 4555338640
   /  '<New><Instance>NodeIndexInt' : 1
   /  '<New><Instance>NodeKeyStr' : MyFilterer
   /  '<Spe><Instance>FilteredGetVariable' : {...}< (FiltererClass), 4555338640>
   /  '<Spe><Instance>FilteredVariablesList' : ['MyFilterer']
   /  '<Spe><Instance>FilteringGetVariable' : /
   /}

*****End of the Attest *****



```

