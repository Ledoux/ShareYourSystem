

<!--
FrozenIsBool False
-->

#Collecter

##Doc
----


>
> Collecter instances
>
>

----

<small>
View the Collecter notebook on [NbViewer](http://nbviewer.ipython.org/url/sharey
oursystem.ouvaton.org/Collecter.ipynb)
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


Collecter instances

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Noders.Parenter"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Classors import Doer
from ShareYourSystem.Standards.Noders import Noder
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class CollecterClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'CollectingCollectionStr',
'CollectingNodeKeyStr',
'CollectingNodeVariable',
'CollectedGetStr',
'CollectedSuffixStr',
'CollectedSetKeyStr'
                                                                ]

        #@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':
BaseClass.__init__}]})
        def default_init(self,
                                                _CollectingCollectionStr="",
                                                _CollectingNodeKeyStr="",
                                                _CollectingNodeVariable=None,
                                                _CollectedGetStr="",
                                                _CollectedSuffixStr="",
                                                _CollectedSetKeyStr="",
                                                **_KwargVariablesDict
                                        ):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_collect(self):

                #debug
                '''
                self.debug(('self.',self,[
                                                'CollectingCollectionStr',
                                                'CollectingNodeKeyStr',
                                                'CollectingNodeVariable'
                                        ]))
                '''

                #Set
                self.CollectedGetStr=Noder.NodingPrefixGetStr+self.CollectingCol
lectionStr+Noder.NodingSuffixGetStr

                #Add a typing suffix Str
                if hasattr(self.CollectingNodeVariable.__class__,'NameStr'):
self.CollectedSuffixStr=self.CollectingNodeVariable.__class__.NameStr
                else:
CollectedTypeStr=type(self.CollectingNodeVariable).__name__
self.CollectedSuffixStr=CollectedTypeStr[0].upper()+CollectedTypeStr[1:]

                #set
                self.CollectedSetKeyStr=self.CollectedGetStr+self.CollectingNode
KeyStr+self.CollectedSuffixStr

                #debug
                '''
                self.debug(('self.',self,['CollectedSetKeyStr']))
                '''

                #node
                self[self.CollectedSetKeyStr]=self.CollectingNodeVariable

#</DefineClass>


```

<small>
View the Collecter sources on <a href="https://github.com/Ledoux/ShareYourSystem
/tree/master/Pythonlogy/ShareYourSystem/Noders/Collecter"
target="_blank">Github</a>
</small>



```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Standards.Noders import Noder,Collecter

#Definition of an instance
MyCollecter=Collecter.CollecterClass().collect(
    'Nodome',
    'First',
    Noder.NoderClass()
).collect(
    'Nodome',
    'Second',
    Noder.NoderClass()
)

#Definition the AttestedStr
SYS._attest(
    [
        'MyCollecter is '+SYS._str(
        MyCollecter,
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

MyCollecter is < (CollecterClass), 4555207312>
   /{
   /  '<New><Instance>IdInt' : 4555207312
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopCollecter
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>NodomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstNoder' : < (NoderClass), 4540175184>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4540175184
   /   /   /  '<New><Instance>NodeCollectionStr' : Nodome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstNoder
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (CollecterClass),
4555207312>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4556378488>
   /   /   /  '<Spe><Class>NodedCollectionIndexInt' : -1
   /   /   /  '<Spe><Class>NodedCollectionOrderedDict' : None
   /   /   /  '<Spe><Class>NodedCollectionStr' :
   /   /   /  '<Spe><Class>NodedKeyStr' :
   /   /   /  '<Spe><Class>NodingCollectionStr' :
   /   /   /}
   /   /  'SecondNoder' : < (NoderClass), 4555576272>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4555576272
   /   /   /  '<New><Instance>NodeCollectionStr' : Nodome
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondNoder
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (CollecterClass),
4555207312>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4556378488>
   /   /   /  '<Spe><Class>NodedCollectionIndexInt' : -1
   /   /   /  '<Spe><Class>NodedCollectionOrderedDict' : None
   /   /   /  '<Spe><Class>NodedCollectionStr' :
   /   /   /  '<Spe><Class>NodedKeyStr' :
   /   /   /  '<Spe><Class>NodingCollectionStr' :
   /   /   /}
   /   /}
   /  '<Spe><Instance>CollectedGetStr' : <Nodome>
   /  '<Spe><Instance>CollectedSetKeyStr' : <Nodome>SecondNoder
   /  '<Spe><Instance>CollectedSuffixStr' : Noder
   /  '<Spe><Instance>CollectingCollectionStr' : Nodome
   /  '<Spe><Instance>CollectingNodeKeyStr' : Second
   /  '<Spe><Instance>CollectingNodeVariable' : {...}< (NoderClass), 4555576272>
   /}

*****End of the Attest *****



```

