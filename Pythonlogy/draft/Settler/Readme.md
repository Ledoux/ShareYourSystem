

<!--
FrozenIsBool False
-->

#Settler

##Doc
----


>
> A Settler
>
>

----

<small>
View the Settler notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyou
rsystem.ouvaton.org/Settler.ipynb)
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


A Settler

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Noders.Coupler"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
from ShareYourSystem.Itemizers import Pather
from ShareYourSystem.Applyiers import Linker
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass(**{'ClassingSwitchMethodStrsList':['settle']})
class SettlerClass(
                                        BaseClass,
                                        Linker.LinkerClass
                                        ):

        #Definition
        RepresentingKeyStrsList=[
'SettlingParentBool',
'SettlingLinkBool'
                                                        ]

        def default_init(self,
                                _SettlingParentBool=False,
                                _SettlingLinkBool=False,
                                **_KwargVariablesDict):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        #@Switcher.SwitcherClass()
        def do_settle(self):

                #debug
                '''
                self.debug('We settle here')
                '''

                #Parent first
                if self.SettlingParentBool:

                        #debug
                        '''
                        self.debug('We parent here')
                        '''

                        #parent
                        self.parent()

                #link
                if self.SettlingLinkBool:

                        #debug
                        '''
                        self.debug('We link here')
                        '''

                        #link
                        self.link()

                #Return self
                #return self

        #@Imitater.ImitaterClass()
        def mimic_set(self):

                #debug


                #Call the parent method
                OutputDict=BaseClass.set(self)

                #debug
                '''
                self.debug(('self.',self,[
'SettingKeyVariable',
'SettingValueVariable'
                                                                ]))
                '''

                #Check
                if self.SettingKeyVariable=='NodePointDeriveNoder' and
self.SettingValueVariable!=None:

                        #debug
                        '''
                        self.debug(('self.',self,['NodePointDeriveNoder']))
                        '''

                        #settle
                        self.settle()

                #return
                #return OutputDict

#</DefineClass>


```

<small>
View the Settler sources on <a href="https://github.com/Ledoux/ShareYourSystem/t
ree/master/Pythonlogy/ShareYourSystem/Noders/Settler" target="_blank">Github</a>
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
from ShareYourSystem.Noders import Settler

#Short expression and set in the appended manner
MySettler=Settler.SettlerClass().__setitem__(
    '<Settlome>ChildSettler',
    Settler.SettlerClass()
).update(
    [
        (
            '<Settlome>GrandFirstChildSettler',
            Settler.SettlerClass()
        ),
        (
            '<Settlome>GrandSecondChildSettler',
            Settler.SettlerClass(**{
                'SettlingParentBool':True,
                'SettlingLinkBool':True
                }
                ).__setitem__(
                'LinkingPointListsList',
                [
        ('/NodePointDeriveNoder/<Settlome>GrandFirstChildSettler','GrandFirstChi
ldSettler')
                ]
            )
        )
    ]
)



#Definition the AttestedStr
SYS._attest(
    [
        'MySettler is '+SYS._str(
        MySettler,
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

MySettler is < (SettlerClass), 4555534992>
   /{
   /  '<New><Instance>IdInt' : 4555534992
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopSettler
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>SettlomeCollectionOrderedDict' :
   /   /{
   /   /  'ChildSettler' : < (SettlerClass), 4555578640>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4555578640
   /   /   /  '<New><Instance>NodeCollectionStr' : Settlome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : ChildSettler
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (SettlerClass),
4555534992>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4555699440>
   /   /   /  '<Spe><Class>SettlingLinkBool' : False
   /   /   /  '<Spe><Class>SettlingParentBool' : False
   /   /   /}
   /   /  'GrandFirstChildSettler' : < (SettlerClass), 4555497808>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4555497808
   /   /   /  '<New><Instance>NodeCollectionStr' : Settlome
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : GrandFirstChildSettler
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (SettlerClass),
4555534992>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4555699440>
   /   /   /  '<Spe><Class>SettlingLinkBool' : False
   /   /   /  '<Spe><Class>SettlingParentBool' : False
   /   /   /}
   /   /  'GrandSecondChildSettler' : < (SettlerClass), 4555497936>
   /   /   /{
   /   /   /  '<New><Instance>GrandFirstChildSettler' : {...}< (SettlerClass),
4555497808>
   /   /   /  '<New><Instance>IdInt' : 4555497936
   /   /   /  '<New><Instance>NodeCollectionStr' : Settlome
   /   /   /  '<New><Instance>NodeIndexInt' : 2
   /   /   /  '<New><Instance>NodeKeyStr' : GrandSecondChildSettler
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (SettlerClass),
4555534992>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4555699440>
   /   /   /  '<Spe><Instance>SettlingLinkBool' : True
   /   /   /  '<Spe><Instance>SettlingParentBool' : True
   /   /   /}
   /   /}
   /  '<Spe><Class>SettlingLinkBool' : False
   /  '<Spe><Class>SettlingParentBool' : False
   /}

*****End of the Attest *****



```

