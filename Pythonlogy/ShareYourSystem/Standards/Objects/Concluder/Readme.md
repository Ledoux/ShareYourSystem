

<!--
FrozenIsBool False
-->

#Concluder

##Doc
----


>
> A Concluder
>
>

----

<small>
View the Concluder notebook on [NbViewer](http://nbviewer.ipython.org/url/sharey
oursystem.ouvaton.org/Concluder.ipynb)
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


A Concluder

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Objects.Conditioner"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Tester"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class ConcluderClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'ConcludingTestVariable',
'ConcludingConditionTuplesList',
'ConcludedConditionIsBoolsList',
'ConcludedIsBool'
                                                                ]

        def default_init(self,
                                _ConcludingTestVariable=None,
                                _ConcludingConditionTuplesList=None,
                                _ConcludedConditionIsBoolsList=None,
                                _ConcludedIsBool=True,
                                **_KwargVariablesDict
                                ):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_conclude(self):
                """ """

                #debug
                '''
                self.debug(('self.',self,['ConcludingConditionTuplesList']))
                '''

                #Apply __getitem__
                self.ConcludedConditionIsBoolsList=map(
                                lambda __ConcludingConditionTuple:
                                self.condition(
                                                self.ConcludingTestVariable[
__ConcludingConditionTuple[0]
                                                ] if type(
__ConcludingConditionTuple[0])
                                                in SYS.StrTypesList else
__ConcludingConditionTuple[0],
                                                __ConcludingConditionTuple[1],
                                                __ConcludingConditionTuple[2]
                                        ).ConditionedIsBool,
                                self.ConcludingConditionTuplesList
                        )

                #all
                self.ConcludedIsBool=all(self.ConcludedConditionIsBoolsList)

                #Return self
                #return self
#</DefineClass>

```

<small>
View the Concluder sources on <a href="https://github.com/Ledoux/ShareYourSystem
/tree/master/Pythonlogy/ShareYourSystem/Objects/Concluder"
target="_blank">Github</a>
</small>




<!---
FrozenIsBool True
-->

##Example

Let's do a simple conclude call

```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Standards.Objects import Concluder
import operator

#Definition of an instance Concluder and make it print hello
MyConcluder=Concluder.ConcluderClass().conclude(
    {'MyColorStr':'Black','MySuperInt':6},
    [
        ('MyColorStr',operator.eq,"Black"),
        ('MySuperInt',operator.gt,3),
        (1,operator.eq,1)
    ]
)

#Definition the AttestedStr
SYS._attest(
    [
        'MyConcluder is '+SYS._str(
        MyConcluder,
        **{
            'RepresentingBaseKeyStrsListBool':False,
            'RepresentingAlineaIsBool':False
            }
        ),
    ]
)

#Print






```


```console
>>>


*****Start of the Attest *****

MyConcluder is < (ConcluderClass), 4537034448>
   /{
   /  '<New><Instance>IdInt' : 4537034448
   /  '<Spe><Instance>ConcludedConditionIsBoolsList' :
   /   /[
   /   /  0 : True
   /   /  1 : True
   /   /  2 : True
   /   /]
   /  '<Spe><Instance>ConcludedIsBool' : True
   /  '<Spe><Instance>ConcludingConditionTuplesList' :
   /   /[
   /   /  0 :
   /   /   /(
   /   /   /  0 : MyColorStr
   /   /   /  1 : <built-in function eq>
   /   /   /  2 : Black
   /   /   /)
   /   /  1 :
   /   /   /(
   /   /   /  0 : MySuperInt
   /   /   /  1 : <built-in function gt>
   /   /   /  2 : 3
   /   /   /)
   /   /  2 :
   /   /   /(
   /   /   /  0 : 1
   /   /   /  1 : {...}< (builtin_function_or_method), 4522748384>
   /   /   /  2 : 1
   /   /   /)
   /   /]
   /  '<Spe><Instance>ConcludingTestVariable' :
   /   /{
   /   /  'MyColorStr' : Black
   /   /  'MySuperInt' : 6
   /   /}
   /}

*****End of the Attest *****



```

