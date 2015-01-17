

<!--
FrozenIsBool False
-->

#Router

##Doc
----


>
> A Router
>
>

----

<small>
View the Router notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyour
system.ouvaton.org/Router.ipynb)
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


A Router

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Walkers.Mobilizer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
import collections
from ShareYourSystem.Itemizers import Pather
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class RouterClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'RoutingPickKeyVariablesList',
'RoutedVariablesOrderedDict'
                                                                ]

        def default_init(self,
                                _RoutingPickKeyVariablesList=None,
                                _RoutedVariablesOrderedDict=None,
                                **_KwargVariablesDict):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_route(self):

                #debug
                '''
self.debug(('self.',self,['WalkingSocketDict','WalkedTopOrderedDict']))
                '''

                #Init
                if 'RouteTopOrderedDict' not in self.WalkedTopOrderedDict:
                        self.WalkedTopOrderedDict['RouteTopOrderedDict']=self.Wa
lkingSocketDict['TopVariable'].RoutedVariablesOrderedDict

                #Init
                if 'PickKeyVariablesList' not in self.WalkedTopOrderedDict:
                        self.WalkedTopOrderedDict['PickKeyVariablesList']=self.W
alkingSocketDict['TopVariable'].RoutingPickKeyVariablesList

                #Pick and set in the dict
                RouteVariablesOrderedDict=collections.OrderedDict()
                map(
                                lambda __PickKeyVariable,__PickValueVariable:
                                RouteVariablesOrderedDict.update(
                                        {__PickKeyVariable:__PickValueVariable}
                                ),
self.WalkedTopOrderedDict['PickKeyVariablesList'],
self.pick(self.WalkedTopOrderedDict['PickKeyVariablesList'])
                        )

                #debug
                '''
                self.debug(
                        (
                                'self.WalkedTopOrderedDict ',
                                self.WalkedTopOrderedDict,
                                [
                                        'RouteTopOrderedDict',
                                        'TopIntsList'
                                ]
                        )
                )
                '''

                #set
                Pather.setWithPathVariableAndKeyVariable(
                        self.WalkedTopOrderedDict['RouteTopOrderedDict'],
                        self.WalkedTopOrderedDict['TopIntsList'],
                        RouteVariablesOrderedDict
                )

                #debug
                '''
                self.debug(
                                        [
                                                'After set...',
                                                (
'self.WalkedTopOrderedDict ',
self.WalkedTopOrderedDict,
                                                        ['RouteTopOrderedDict']
                                                )
                                        ]
                                )
                '''


#</DefineClass>

```

<small>
View the Router sources on <a href="https://github.com/Ledoux/ShareYourSystem/tr
ee/master/Pythonlogy/ShareYourSystem/Walkers/Router" target="_blank">Github</a>
</small>



```python

#ImportModules
import ShareYourSystem as SYS

from ShareYourSystem.Walkers import Router

#Definition a Router instance that has Tree nodes
MyRouter=Router.RouterClass().update(
    [
        (
            '<Tree>FirstChildRouter',
            Router.RouterClass().update(
                [
                    (
                        '<Tree>GrandChildRouter',
                        Router.RouterClass()
                    )
                ]
            )
        ),
        (
            '<Tree>SecondChildRouter',
            Router.RouterClass()
        )
    ]
)

#Walk inside the Tree in order to parent
MyRouter.walk(
    {
        'BeforeUpdateList':
        [
            ('route',{'LiargVariablesList':[
['NodedTreeInt','NodedTreeKeyStr']
                                                #['/']
                                            ]
                    })
        ],
        'GatherVariablesList':['<Tree>']
    }
)

#Definition the AttestedStr
SYS._attest(
    [
        'MyRouter is '+SYS._str(
        MyRouter,
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

MyRouter is < (RouterClass), 4559653072>
   /{
   /  '<New><Instance>IdInt' : 4559653072
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopRouter
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /{
   /   /  'FirstChildRouter' : < (RouterClass), 4555684688>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4555684688
   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstChildRouter
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (RouterClass),
4559653072>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4559693928>
   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  'GrandChildRouter' : < (RouterClass), 4559654224>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>IdInt' : 4559654224
   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /   /   /  '<New><Instance>NodeKeyStr' : GrandChildRouter
   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(RouterClass), 4555684688>
   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4559693632>
   /   /   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<Spe><Instance>RoutedVariablesOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<Spe><Instance>RoutingPickKeyVariablesList' :
['NodedTreeInt', 'NodedTreeKeyStr']
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<Spe><Instance>RoutedVariablesOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<Spe><Instance>RoutingPickKeyVariablesList' : {...}< (list),
4556261352>
   /   /   /}
   /   /  'SecondChildRouter' : < (RouterClass), 4559654288>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4559654288
   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondChildRouter
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (RouterClass),
4559653072>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4559693928>
   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<Spe><Instance>RoutedVariablesOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<Spe><Instance>RoutingPickKeyVariablesList' : {...}< (list),
4556261352>
   /   /   /}
   /   /}
   /  '<Spe><Instance>RoutedVariablesOrderedDict' :
   /   /{
   /   /  'NodedTreeInt' : None
   /   /  'NodedTreeKeyStr' : None
   /   /  '0' :
   /   /   /{
   /   /   /  'NodedTreeInt' : None
   /   /   /  'NodedTreeKeyStr' : None
   /   /   /  '1' :
   /   /   /   /{
   /   /   /   /  'NodedTreeInt' : None
   /   /   /   /  'NodedTreeKeyStr' : None
   /   /   /   /}
   /   /   /}
   /   /  '2' :
   /   /   /{
   /   /   /  'NodedTreeInt' : None
   /   /   /  'NodedTreeKeyStr' : None
   /   /   /}
   /   /}
   /  '<Spe><Instance>RoutingPickKeyVariablesList' : {...}< (list), 4556261352>
   /}

*****End of the Attest *****



```

