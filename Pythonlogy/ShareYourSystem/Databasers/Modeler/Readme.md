

<!--
FrozenIsBool False
-->

#Modeler

##Doc
----


>
> The Modeler defines the model to be stored in a database like Django or
PyTable.
> Here are defined the relations between attributes of an instance and their
corresponding
> types in the databased structures.
>
>

----

<small>
View the Modeler notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyou
rsystem.ouvaton.org/Modeler.ipynb)
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


The Modeler defines the model to be stored in a database like Django or PyTable.
Here are defined the relations between attributes of an instance and their
corresponding
types in the databased structures.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Databasers.Databaser"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import copy
import tables
from ShareYourSystem.Classors import Doer
#</ImportSpecificModules>

#<DefineLocals>
AnalyzingColStrsList=[
                                                        'Int',
                                                        'Float',
                                                        'Str'
                                        ]
ModelingJoinStr='__'
ModelingLinkStr='_'
#</DefineLocals>

#<DefineFunctions>
def getModeledColWithGetKeyStr(_GetKeyStr):

        #Definition
        global AnalyzingColStrsList

        #Definition
        ModeledColStr=SYS._filter(
                lambda __AnalyzingColStr:
                _GetKeyStr.endswith(__AnalyzingColStr),
                AnalyzingColStrsList
                )[0]

        #Get the Col Class
        ModeledColClass=getattr(tables,ModeledColStr+'Col')

        #Return
        if _GetKeyStr=='Str':
                return ModeledColClass(length=100)
        else:
                return ModeledColClass()

def getModelingColumnTupleWithGetKeyStr(_GetKeyStr):
        return (_GetKeyStr,_GetKeyStr,getModeledColWithGetKeyStr(_GetKeyStr))

#</DefineFunctions>

#<DefineClass>
@DecorationClass(**{
        'ClassingSwitchMethodStrsList':["model"]
})
class ModelerClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'ModelingSealTuplesList',
'ModeledClassesOrderedDict',
'ModeledClass',
'ModeledKeyStr'
                                                                ]

        def default_init(
                                        self,
                                        _ModelingSealTuplesList={
'DefaultingSetType':property,
'PropertizingInitVariable':[],
'PropertizingDocStr':''
                                                },
                                        _ModeledClassesOrderedDict=None,
                                        _ModeledClass=None,
                                        _ModeledKeyStr="",
                                        **_KwargVariablesDict
                                ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_model(self):
                """ """

                #debug
                '''
                self.debug(('self.',self,['ModelingSealTuplesList']))
                '''

                #<NotHook>
                #database first
                self.database()
                #</NotHook>

                #set a name if it was not already
                if self.ModeledKeyStr=="":

                        #debug
                        '''
self.debug(('self.',self,['DatabasingKeyStr','DatabasedSuffixStr']))
                        '''

                        #Link set
                        self.ModeledKeyStr=self.DatabasedSuffixStr

                #Definition the ModelClass
                class ModeledClass(tables.IsDescription):

                        #Add a tabulared Int (just like a unique KEY in
mysql...)
                        ModeledInt=tables.Int64Col()

                #debug
                '''
self.debug(('self.',self,['ModeledGetStrToColumnStrOrderedDict']))
                '''

                #set the cols in the ModelClass
                map(
                                lambda __ModelingColumnTuple:
                                ModeledClass.columns.__setitem__(
                                        __ModelingColumnTuple[1],
                                        __ModelingColumnTuple[2]
                                        ),
                                self.ModelingSealTuplesList
                        )

                #Give a name
ModeledClass.__name__=SYS.getClassStrWithNameStr(self.ModeledKeyStr)

                #set the ModelClass
                if self.ModeledClassesOrderedDict==None:
                        self.ModeledClassesOrderedDict=collections.OrderedDict()
                self.ModeledClassesOrderedDict[self.ModeledKeyStr]=ModeledClass

                #set the ModeledClass
                self.ModeledClass=ModeledClass

#</DefineClass>

```

<small>
View the Modeler sources on <a href="https://github.com/Ledoux/ShareYourSystem/t
ree/master/Pythonlogy/ShareYourSystem/Databasers/Modeler"
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
import tables
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Collecter
from ShareYourSystem.Databasers import Modeler

#Definition of a Collecter instance with a noded datar
MyCollecter=Collecter.CollecterClass().collect(
    "Datome",
    "Things",
    Modeler.ModelerClass()
)

#Definition a Modeler instance
MyCollecter['<Datome>ThingsModeler'].model([
                                        #GetStr #ColumnStr #Col
                                        ('MyInt','MyInt',tables.Int64Col()),
                                        ('MyStr','MyStr',tables.StringCol(10)),
('MyIntsList','MyIntsList',tables.Int64Col(shape=3))
                                ])


#Definition the AttestedStr
SYS._attest(
    [
        'MyCollecter is '+SYS._str(
        MyCollecter,
        **{
            'RepresentingBaseKeyStrsListBool':False,
            'RepresentingAlineaIsBool':False
        }
        ),
        'MyCollecter["<Datome>ThingsModeler"].ModeledClass.__dict__ is
'+SYS._str(
        dict(MyCollecter['<Datome>ThingsModeler'].ModeledClass.__dict__.items()
            ) if MyCollecter['<Datome>ThingsModeler'
        ].ModeledClass!=None else {},**{'RepresentingAlineaIsBool':False}
        )
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

MyCollecter is < (CollecterClass), 4563976464>
   /{
   /  '<New><Instance>DatomeCollectionOrderedDict' :
   /   /{
   /   /  'ThingsModeler' : < (ModelerClass), 4563976528>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4563976528
   /   /   /  '<New><Instance>NewtorkAttentionStr' :
   /   /   /  '<New><Instance>NewtorkCatchStr' :
   /   /   /  '<New><Instance>NewtorkCollectionStr' :
   /   /   /  '<New><Instance>NodeCollectionStr' : Datome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : ThingsModeler
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (CollecterClass),
4563976464>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4563600032>
   /   /   /  '<New><Instance>_ModelingSealTuplesList' :
   /   /   /   /[
   /   /   /   /  0 :
   /   /   /   /   /(
   /   /   /   /   /  0 : MyInt
   /   /   /   /   /  1 : MyInt
   /   /   /   /   /  2 : Int64Col(shape=(), dflt=0, pos=None)
   /   /   /   /   /)
   /   /   /   /  1 :
   /   /   /   /   /(
   /   /   /   /   /  0 : MyStr
   /   /   /   /   /  1 : MyStr
   /   /   /   /   /  2 : StringCol(itemsize=10, shape=(), dflt='', pos=None)
   /   /   /   /   /)
   /   /   /   /  2 :
   /   /   /   /   /(
   /   /   /   /   /  0 : MyIntsList
   /   /   /   /   /  1 : MyIntsList
   /   /   /   /   /  2 : Int64Col(shape=(3,), dflt=0, pos=None)
   /   /   /   /   /)
   /   /   /   /]
   /   /   /  '<Spe><Class>ModelingSealTuplesList' : {...}< (list), 4559830048>
   /   /   /  '<Spe><Instance>ModeledClass' : <class
'tables.description.ThingsModelerModelClass'>
   /   /   /  '<Spe><Instance>ModeledClassesOrderedDict' :
   /   /   /   /{
   /   /   /   /  'ThingsModelerModel' : {...}< (MetaIsDescription),
140476448323056>
   /   /   /   /}
   /   /   /  '<Spe><Instance>ModeledKeyStr' : ThingsModelerModel
   /   /   /}
   /   /}
   /  '<New><Instance>IdInt' : 4563976464
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopCollecter
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<Spe><Instance>CollectedGetStr' : <Datome>
   /  '<Spe><Instance>CollectedSetKeyStr' : <Datome>ThingsModeler
   /  '<Spe><Instance>CollectedSuffixStr' : Modeler
   /  '<Spe><Instance>CollectingCollectionStr' : Datome
   /  '<Spe><Instance>CollectingNodeKeyStr' : Things
   /  '<Spe><Instance>CollectingNodeVariable' : {...}< (ModelerClass),
4563976528>
   /}

------

MyCollecter["<Datome>ThingsModeler"].ModeledClass.__dict__ is
   /{
   /  '__doc__' : None
   /  '__module__' : tables.description
   /  'columns' :
   /   /{
   /   /  'ModeledInt' : Int64Col(shape=(), dflt=0, pos=None)
   /   /  'MyInt' : Int64Col(shape=(), dflt=0, pos=None)
   /   /  'MyIntsList' : Int64Col(shape=(3,), dflt=0, pos=None)
   /   /  'MyStr' : StringCol(itemsize=10, shape=(), dflt='', pos=None)
   /   /}
   /}

*****End of the Attest *****



```

