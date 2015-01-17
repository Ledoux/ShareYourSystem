

<!--
FrozenIsBool False
-->

#Grabber

##Doc
----


>
> A Grabber
>
>

----

<small>
View the Grabber notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyou
rsystem.ouvaton.org/Grabber.ipynb)
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


A Grabber

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Walkers.Router"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
import collections
from ShareYourSystem.Functers import Argumenter
from ShareYourSystem.Noders import Noder
#</ImportSpecificModules>

#<DefineLocals>
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class GrabberClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'GrabbingNodeStr',
'GrabbingPickVariablesList',
'GrabbedVariablesOrderedDict'
                                                                ]

        def default_init(self,
                                _GrabbingNodeStr=None,
                                _GrabbingPickVariablesList=None,
                                _GrabbedVariablesOrderedDict=None,
                                **_KwargVariablesDict):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        #@Argumenter.ArgumenterClass()
        def do_grab(self):

                #Init
                if self.GrabbedVariablesOrderedDict==None:
self.GrabbedVariablesOrderedDict=collections.OrderedDict()

                #debug
                '''
self.debug(('self.',self,['GrabbingNodeStr','GrabbingPickVariablesList']))
                '''

                #Walk inside the Tree in order to parent
                self.walk(
                                        {
                                                'BeforeUpdateList':
                                                [
('route',{'LiargVariablesList':[
                                                self.GrabbingPickVariablesList
                                        ]
})
                                                ],
                                                'GatherVariablesList':[
Noder.NodingPrefixGetStr+self.GrabbingNodeStr+Noder.NodingSuffixGetStr]
                                        }
                                )

                #Link
                self.GrabbedVariablesOrderedDict=self.RoutedVariablesOrderedDict


#</DefineClass>

```

<small>
View the Grabber sources on <a href="https://github.com/Ledoux/ShareYourSystem/t
ree/master/Pythonlogy/ShareYourSystem/Walkers/Grabber"
target="_blank">Github</a>
</small>



```python

#ImportModules
import ShareYourSystem as SYS

from ShareYourSystem.Walkers import Grabber

#Definition a Grabber instance that has Tree nodes
MyGrabber=Grabber.GrabberClass().update(
        [
            (
                '<Tree>FirstChildGrabber',
                Grabber.GrabberClass().update(
                    [
                        (
                            '<Tree>GrandChildGrabber',
                            Grabber.GrabberClass()
                        )
                    ]
                )
            ),
            (
                '<Tree>SecondChildGrabber',
                Grabber.GrabberClass()
            )
        ]
    )

#Grab
MyGrabber.grab("Tree",['NodedTreeInt','NodedTreeKeyStr'])

#Definition the AttestedStr
SYS._attest(
    [
        'MyGrabber is '+SYS._str(
        MyGrabber,
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

MyGrabber is < (GrabberClass), 4559654352>
   /{
   /  '<New><Instance>IdInt' : 4559654352
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopGrabber
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /{
   /   /  'FirstChildGrabber' : < (GrabberClass), 4559653264>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4559653264
   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstChildGrabber
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (GrabberClass),
4559654352>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4559710904>
   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  'GrandChildGrabber' : < (GrabberClass), 4559706256>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>IdInt' : 4559706256
   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /   /   /  '<New><Instance>NodeKeyStr' : GrandChildGrabber
   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(GrabberClass), 4559653264>
   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4559710312>
   /   /   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<Spe><Class>GrabbedVariablesOrderedDict' : None
   /   /   /   /   /  '<Spe><Class>GrabbingNodeStr' : None
   /   /   /   /   /  '<Spe><Class>GrabbingPickVariablesList' : None
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<Spe><Class>GrabbedVariablesOrderedDict' : None
   /   /   /  '<Spe><Class>GrabbingNodeStr' : None
   /   /   /  '<Spe><Class>GrabbingPickVariablesList' : None
   /   /   /}
   /   /  'SecondChildGrabber' : < (GrabberClass), 4559706576>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4559706576
   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondChildGrabber
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (GrabberClass),
4559654352>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4559710904>
   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<Spe><Class>GrabbedVariablesOrderedDict' : None
   /   /   /  '<Spe><Class>GrabbingNodeStr' : None
   /   /   /  '<Spe><Class>GrabbingPickVariablesList' : None
   /   /   /}
   /   /}
   /  '<Spe><Instance>GrabbedVariablesOrderedDict' :
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
   /  '<Spe><Instance>GrabbingNodeStr' : Tree
   /  '<Spe><Instance>GrabbingPickVariablesList' : ['NodedTreeInt',
'NodedTreeKeyStr']
   /}

*****End of the Attest *****



```

