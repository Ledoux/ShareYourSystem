

<!--
FrozenIsBool False
-->

#Walker

##Doc
----


>
> A Parenter completes the list of grand-parent nodes that
> a child node could have. It is a recursive top-down set
> of the pointers and the pathStrs.
>
>

----

<small>
View the Walker notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyour
system.ouvaton.org/Walker.ipynb)
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


A Parenter completes the list of grand-parent nodes that
a child node could have. It is a recursive top-down set
of the pointers and the pathStrs.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Applyiers.Commander"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
from ShareYourSystem.Functers import Argumenter
#</ImportSpecificModules>

#<DefineLocals>
WalkingStr="zz"
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class WalkerClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'WalkingSocketDict',
#'WalkedOrderedDict',
#'WalkedTopOrderedDict'
                                                                ]

        def default_init(self,
                                _WalkingSocketDict=None,
                                _WalkedOrderedDict=None,
                                _WalkedTopOrderedDict=None,
                                **_KwargVariablesDict
                        ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_walk(self):

                #Init the WalkedTopOrderedDict
                WalkedTopOrderedDict=None
                if 'IdStr' not in self.WalkingSocketDict:

                        #Definition the IdStr of this walk
                        IdStr=str(id(self.WalkingSocketDict))

                        #set the _WalkingSocketDict
                        self.WalkingSocketDict.update(
                                                                        {
'IdStr':IdStr,
'TopVariable':self,
                                                                        }
                                                                )

                        #Definition WalkedTopOrderedSetTagStr
WalkedTopOrderedSetTagStr='Walked'+WalkingStr+IdStr+WalkingStr+'OrderedDict'

                        #set the corresponding WalkedOrderedDict
                        self.__setattr__(
WalkedTopOrderedSetTagStr,
collections.OrderedDict(**
                                                                        {
'IndexInt':-1,
'TopIntsList':['/'],
'TopVariablesList':[self]
                                                                        }
                                                                )
                                                        )

                        #Alias this Dict
                        self.WalkedTopOrderedDict=getattr(
                                self,
                                WalkedTopOrderedSetTagStr
                        )

                else:

                        #Get the information at the top
                        WalkedTopOrderedSetTagStr='Walked'+WalkingStr+self.Walk
ingSocketDict['IdStr']+WalkingStr+'OrderedDict'
                        self.WalkedTopOrderedDict=getattr(
                                self.WalkingSocketDict['TopVariable'],
                                WalkedTopOrderedSetTagStr
                        )
                        self.WalkedTopOrderedDict['IndexInt']+=1
                        self.WalkedTopOrderedDict['TopIntsList']+=[str(
                                self.WalkedTopOrderedDict['IndexInt'])]
                        self.WalkedTopOrderedDict['TopVariablesList']+=[self]

                #An Update just before is possible
                if 'BeforeUpdateList' in self.WalkingSocketDict:

                        #debug
                        '''
self.debug(('_SocketDict',_SocketDict,['BeforeUpdateList']))
                        '''

                        #Update
                        self.update(self.WalkingSocketDict['BeforeUpdateList'])

                #Debug
                '''
                self.debug(('self.',self,['WalkingSocketDict']))
                '''

                #Command an recursive order in other gathered variables
                self.command(
                                                _UpdateList=[
                                                        ('walk',{
'LiargVariablesList':[self.WalkingSocketDict],
                                                                        }
                                                        )
                                                ],
                                                **{
'GatheringVariablesList':self.WalkingSocketDict[
'GatherVariablesList'
                                                        ]
                                                }
                                        )

                #An Update just after is possible
                if 'AfterUpdateList' in self.WalkingSocketDict:
                        self.update(self.WalkingSocketDict[
                                'AfterUpdateList'])

                #Retrieve the previous Path
                if len(self.WalkedTopOrderedDict['TopIntsList'])>0:
self.WalkedTopOrderedDict['TopIntsList']=self.WalkedTopOrderedDict[
                        'TopIntsList'][:-1]
self.WalkedTopOrderedDict['TopVariablesList']=self.WalkedTopOrderedDict[
                        'TopVariablesList'][:-1]

                #Return self
                if self.WalkingSocketDict['TopVariable']==self:
                        self.WalkedOrderedDict=WalkedTopOrderedDict
                        del self[WalkedTopOrderedSetTagStr]
                        return self
#</DefineClass>

```

<small>
View the Walker sources on <a href="https://github.com/Ledoux/ShareYourSystem/tr
ee/master/Pythonlogy/ShareYourSystem/Walkers/Walker" target="_blank">Github</a>
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
from ShareYourSystem.Standards.Walkers import Walker

#Definition a Walker instance with a noded tree
MyWalker=Walker.WalkerClass().update(
    [
        (
            '<Tree>FirstChildWalker',
            Walker.WalkerClass().update(
                [
                    (
                        '<Tree>GrandChildWalker',
                        Walker.WalkerClass()
                    )
                ]
            )
        ),
        (
            '<Tree>SecondChildWalker',
            Walker.WalkerClass()
        )
    ]
)

#Walk inside the Tree in order to parent again because the tree was not yet
completely setted when it was done
MyWalker.walk(
            {
                'BeforeUpdateList':
                [
                    ('SwitchingParentBool',False),
                    ('parent',{'LiargVariablesList':['Tree']})
                ],
                'GatherVariablesList':['<Tree>']
            }
        )


#Definition the AttestedStr
SYS._attest(
    [
        'MyWalker is '+SYS._str(
        MyWalker,
        **{
            'RepresentingBaseKeyStrsListBool':False,
            'RepresentingAlineaIsBool':False,
            'RepresentingKeyStrsList':['ParentedDeriveParentersList']
        }
        )
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

MyWalker is < (WalkerClass), 4556651408>
   /{
   /  '<New><Instance>IdInt' : 4556651408
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopWalker
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>SwitchingParentBool' : False
   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /{
   /   /  'FirstChildWalker' : < (WalkerClass), 4556652432>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4556652432
   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstChildWalker
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (WalkerClass),
4556651408>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4557623672>
   /   /   /  '<New><Instance>SwitchingParentBool' : False
   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  'GrandChildWalker' : < (WalkerClass), 4556221648>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>IdInt' : 4556221648
   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /   /   /  '<New><Instance>NodeKeyStr' : GrandChildWalker
   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(WalkerClass), 4556652432>
   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4555945200>
   /   /   /   /   /  '<New><Instance>SwitchingParentBool' : False
   /   /   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<Spe><Instance>ParentedDeriveParentersList' :
   /   /   /   /   /   /[
   /   /   /   /   /   /  0 : {...}< (WalkerClass), 4556652432>
   /   /   /   /   /   /  1 : {...}< (WalkerClass), 4556651408>
   /   /   /   /   /   /]
   /   /   /   /   /  '<Spe><Instance>WalkingSocketDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /  'BeforeUpdateList' :
   /   /   /   /   /   /   /[
   /   /   /   /   /   /   /  0 :
   /   /   /   /   /   /   /   /(
   /   /   /   /   /   /   /   /  0 : SwitchingParentBool
   /   /   /   /   /   /   /   /  1 : False
   /   /   /   /   /   /   /   /)
   /   /   /   /   /   /   /  1 :
   /   /   /   /   /   /   /   /(
   /   /   /   /   /   /   /   /  0 : parent
   /   /   /   /   /   /   /   /  1 :
   /   /   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /   /   /  'LiargVariablesList' : ['Tree']
   /   /   /   /   /   /   /   /   /}
   /   /   /   /   /   /   /   /)
   /   /   /   /   /   /   /]
   /   /   /   /   /   /  'GatherVariablesList' : ['<Tree>']
   /   /   /   /   /   /  'IdStr' : 4555544288
   /   /   /   /   /   /  'TopVariable' : {...}< (WalkerClass), 4556651408>
   /   /   /   /   /   /}
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<Spe><Instance>ParentedDeriveParentersList' :
   /   /   /   /[
   /   /   /   /  0 : {...}< (WalkerClass), 4556651408>
   /   /   /   /]
   /   /   /  '<Spe><Instance>WalkingSocketDict' : {...}< (dict), 4555544288>
   /   /   /}
   /   /  'SecondChildWalker' : < (WalkerClass), 4555021968>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4555021968
   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondChildWalker
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (WalkerClass),
4556651408>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4557623672>
   /   /   /  '<New><Instance>SwitchingParentBool' : False
   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<Spe><Instance>ParentedDeriveParentersList' :
   /   /   /   /[
   /   /   /   /  0 : {...}< (WalkerClass), 4556651408>
   /   /   /   /]
   /   /   /  '<Spe><Instance>WalkingSocketDict' : {...}< (dict), 4555544288>
   /   /   /}
   /   /}
   /  '<Spe><Instance>ParentedDeriveParentersList' : []
   /  '<Spe><Instance>WalkingSocketDict' : {...}< (dict), 4555544288>
   /}

*****End of the Attest *****



```

