

<!--
FrozenIsBool False
-->

#Pusher

##Doc
----


>
> Pusher instances
>
>

----

<small>
View the Pusher notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyour
system.ouvaton.org/Pusher.ipynb)
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


Pusher instances

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Noders.Collecter"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class PusherClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'PushingStoreListsList'
                                                                ]

        #@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':
BaseClass.__init__}]})
        def default_init(self,
                                                _PushingStoreListsList=None,
                                                **_KwargVariablesDict
                                        ):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_push(self):

                #debug
                '''
                self.debug(('self.',self,['PushingStoreListsList']))
                '''

                #Apply __getitem__
                self.map('collect',map(
                                                                        lambda
__PushingStoreList:
                                                                        {
'LiargVariablesList':[],
'KwargVariablesDict':
{
        'CollectingNodeKeyStr':__PushingStoreList[0],
        'CollectingNodeVariable':__PushingStoreList[1],
}
                                                                        },
self.PushingStoreListsList
                                                                )
                                        )
#</DefineClass>


```

<small>
View the Pusher sources on <a href="https://github.com/Ledoux/ShareYourSystem/tr
ee/master/Pythonlogy/ShareYourSystem/Applyiers/Pusher"
target="_blank">Github</a>
</small>



```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Applyiers import Pusher

#push
MyPusher=Pusher.PusherClass().push(
    [
        [
            'FirstChild',
            Pusher.PusherClass().__setitem__('MyInt',0)
        ],
        [
            'SecondChild',
            Pusher.PusherClass()
        ]
    ],
    **{'CollectingCollectionStr':'Pushome'}
)

#Definition the AttestedStr
SYS._attest(
    [
        'MyPusher is '+SYS._str(
        MyPusher,
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

MyPusher is < (PusherClass), 4555340112>
   /{
   /  '<New><Instance>IdInt' : 4555340112
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopPusher
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>PushomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstChildPusher' : < (PusherClass), 4555018576>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4555018576
   /   /   /  '<New><Instance>MyInt' : 0
   /   /   /  '<New><Instance>NodeCollectionStr' : Pushome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstChildPusher
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (PusherClass),
4555340112>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4554959840>
   /   /   /  '<Spe><Class>PushingStoreListsList' : None
   /   /   /}
   /   /  'SecondChildPusher' : < (PusherClass), 4555018704>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4555018704
   /   /   /  '<New><Instance>NodeCollectionStr' : Pushome
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondChildPusher
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (PusherClass),
4555340112>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4554959840>
   /   /   /  '<Spe><Class>PushingStoreListsList' : None
   /   /   /}
   /   /}
   /  '<Spe><Instance>PushingStoreListsList' :
   /   /[
   /   /  0 :
   /   /   /[
   /   /   /  0 : FirstChild
   /   /   /  1 : {...}< (PusherClass), 4555018576>
   /   /   /]
   /   /  1 :
   /   /   /[
   /   /   /  0 : SecondChild
   /   /   /  1 : {...}< (PusherClass), 4555018704>
   /   /   /]
   /   /]
   /}

*****End of the Attest *****



```

