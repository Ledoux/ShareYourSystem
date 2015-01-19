

<!--
FrozenIsBool False
-->

#Databaser

##Doc
----


>
> A Databaser rises to the DatabaserClass. This latter is the deepest class for
instancing
> Variables able to store values in hierarchic tables. Here, as a first step,
> the database method helps to set the <DatabasingKeyStr> in the __dict__
>
>

----

<small>
View the Databaser notebook on [NbViewer](http://nbviewer.ipython.org/url/sharey
oursystem.ouvaton.org/Databaser.ipynb)
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


A Databaser rises to the DatabaserClass. This latter is the deepest class for
instancing
Variables able to store values in hierarchic tables. Here, as a first step,
the database method helps to set the <DatabasingKeyStr> in the __dict__

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Noders.Structurer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass(**{'ClassingSwitchMethodStrsList':['database']})
class DatabaserClass(
                                                BaseClass
                                ):

        #Definition
        RepresentingKeyStrsList=[
'ModeledSuffixStr',
'DatabasedCollectionStr',
'ModeledSuffixStr',
'ModeledPointDeriveStorerVariable'
                                                        ]

        def default_init(self,
                                        _DatabasingKeyStr="",
                                        _DatabasedCollectionStr="",
                                        _ModeledSuffixStr="",
_ModeledPointDeriveStorerVariable=None,
                                        **_KwargVariablesDict
                                ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_database(self):

                #set
                if hasattr(self,'NodeKeyStr'):
                        self.DatabasingKeyStr=self.NodeKeyStr
                        self.DatabasedCollectionStr=self.NodeCollectionStr

                #set
                self.ModeledSuffixStr=self.DatabasingKeyStr+'Model'

                #
                if hasattr(self,'NodePointDeriveNoder'):
                        self.point(
                                self.NodePointDeriveNoder,
                                'ModeledPointDeriveStorerVariable'
                        )

#</DefineClass>

```

<small>
View the Databaser sources on <a href="https://github.com/Ledoux/ShareYourSystem
/tree/master/Pythonlogy/ShareYourSystem/Databasers/Databaser"
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
from ShareYourSystem.Controllers import Storer
from ShareYourSystem.Modelers import Databaser

#Definition of a Storer instance with a noded databaser
MyStorer=Storer.StorerClass().collect(
    "Datome",
    "Things",
    Databaser.DatabaserClass()
)

#database
MyStorer['<Datome>ThingsDatabaser'].database()

#Definition the AttestedStr
SYS._attest(
    [
        'MyStorer is '+SYS._str(
        MyStorer,
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

MyStorer is < (StorerClass), 4559345232>
   /{
   /  '<New><Instance>DatomeCollectionOrderedDict' :
   /   /{
   /   /  'ThingsDatabaser' : < (DatabaserClass), 4561982864>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4561982864
   /   /   /  '<New><Instance>NewtorkAttentionStr' :
   /   /   /  '<New><Instance>NewtorkCatchStr' :
   /   /   /  '<New><Instance>NewtorkCollectionStr' :
   /   /   /  '<New><Instance>NodeCollectionStr' : Datome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : ThingsDatabaser
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (StorerClass),
4559345232>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4563600328>
   /   /   /  '<Spe><Instance>DatabasedCollectionStr' : Datome
   /   /   /  '<Spe><Instance>ModeledPointDeriveStorerVariable' : {...}<
(StorerClass), 4559345232>
   /   /   /  '<Spe><Instance>ModeledSuffixStr' : ThingsDatabaserModel
   /   /   /}
   /   /}
   /  '<New><Instance>IdInt' : 4559345232
   /  '<New><Instance>NewtorkAttentionStr' :
   /  '<New><Instance>NewtorkCatchStr' :
   /  '<New><Instance>NewtorkCollectionStr' :
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopStorer
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<Spe><Class>StoringOrganizeIsBool' : False
   /}

*****End of the Attest *****



```

