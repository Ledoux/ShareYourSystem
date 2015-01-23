

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
BaseModuleStr="ShareYourSystem.Standards.Modelers.Databaser"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import copy
import tables
from ShareYourSystem.Standards.Classors import Doer
#</ImportSpecificModules>

#<DefineLocals>
AnalyzingColStrsList=[
                                                        'Int',
                                                        'Float',
                                                        'Str'
                                        ]
DatabasingJoinStr='__'
DatabasingLinkStr='_'
#</DefineLocals>

#<DefineFunctions>
def getDatabasedColWithGetKeyStr(_GetKeyStr):

        #Definition
        global AnalyzingColStrsList

        #Definition
        DatabasedColStr=SYS._filter(
                lambda __AnalyzingColStr:
                _GetKeyStr.endswith(__AnalyzingColStr),
                AnalyzingColStrsList
                )[0]

        #Get the Col Class
        DatabasedColClass=getattr(tables,DatabasedColStr+'Col')

        #Return
        if _GetKeyStr=='Str':
                return DatabasedColClass(length=100)
        else:
                return DatabasedColClass()

def getDatabasingColumnTupleWithGetKeyStr(_GetKeyStr):
        return (_GetKeyStr,_GetKeyStr,getDatabasedColWithGetKeyStr(_GetKeyStr))

#</DefineFunctions>

#<DefineClass>
@DecorationClass(**{
        'ClassingSwitchMethodStrsList':["model"]
})
class ModelerClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'DatabasingSealTuplesList',
'DatabasedModelClassesOrderedDict',
'DatabasedModelClass',
'DatabasedKeyStr'
                                                                ]

        def default_init(
                                        self,
                                        _DatabasingSealTuplesList={
'DefaultingSetType':property,
'PropertizingInitVariable':[],
'PropertizingDocStr':''
                                                },
                                        _DatabasedModelClassesOrderedDict=None,
                                        _DatabasedModelClass=None,
                                        _DatabasedKeyStr="",
                                        **_KwargVariablesDict
                                ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_model(self):
                """ """

                #debug
                '''
                self.debug(('self.',self,['DatabasingSealTuplesList']))
                '''

                #<NotHook>
                #database first
                self.database()
                #</NotHook>

                #set a name if it was not already
                if self.DatabasedKeyStr=="":

                        #debug
                        '''
self.debug(('self.',self,['DatabasingKeyStr','ModeledSuffixStr']))
                        '''

                        #Link set
                        self.DatabasedKeyStr=self.ModeledSuffixStr

                #Definition the ModelClass
                class DatabasedModelClass(tables.IsDescription):

                        #Add a tabulared Int (just like a unique KEY in
mysql...)
                        RowInt=tables.Int64Col()

                #debug
                '''
self.debug(('self.',self,['DatabasedGetStrToColumnStrOrderedDict']))
                '''

                #set the cols in the ModelClass
                map(
                                lambda __DatabasingColumnTuple:
                                DatabasedModelClass.columns.__setitem__(
                                        __DatabasingColumnTuple[1],
                                        __DatabasingColumnTuple[2]
                                        ),
                                self.DatabasingSealTuplesList
                        )

                #Give a name
DatabasedModelClass.__name__=SYS.getClassStrWithNameStr(self.DatabasedKeyStr)

                #set the ModelClass
                if self.DatabasedModelClassesOrderedDict==None:
                        self.DatabasedModelClassesOrderedDict=collections.OrderedDict()
                self.DatabasedModelClassesOrderedDict[self.DatabasedKeyStr]=DatabasedModelClass

                #set the DatabasedModelClass
                self.DatabasedModelClass=DatabasedModelClass

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
from ShareYourSystem.Standards.Noders import Collecter
from ShareYourSystem.Standards.Modelers import Modeler

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
        'MyCollecter["<Datome>ThingsModeler"].DatabasedModelClass.__dict__ is
'+SYS._str(
        dict(MyCollecter['<Datome>ThingsModeler'].DatabasedModelClass.__dict__.items()
            ) if MyCollecter['<Datome>ThingsModeler'
        ].DatabasedModelClass!=None else {},**{'RepresentingAlineaIsBool':False}
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
   /   /   /  '<New><Instance>_DatabasingSealTuplesList' :
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
   /   /   /  '<Spe><Class>DatabasingSealTuplesList' : {...}< (list), 4559830048>
   /   /   /  '<Spe><Instance>DatabasedModelClass' : <class
'tables.description.ThingsModelerModelClass'>
   /   /   /  '<Spe><Instance>DatabasedModelClassesOrderedDict' :
   /   /   /   /{
   /   /   /   /  'ThingsModelerModel' : {...}< (MetaIsDescription),
140476448323056>
   /   /   /   /}
   /   /   /  '<Spe><Instance>DatabasedKeyStr' : ThingsModelerModel
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

MyCollecter["<Datome>ThingsModeler"].DatabasedModelClass.__dict__ is
   /{
   /  '__doc__' : None
   /  '__module__' : tables.description
   /  'columns' :
   /   /{
   /   /  'RowInt' : Int64Col(shape=(), dflt=0, pos=None)
   /   /  'MyInt' : Int64Col(shape=(), dflt=0, pos=None)
   /   /  'MyIntsList' : Int64Col(shape=(3,), dflt=0, pos=None)
   /   /  'MyStr' : StringCol(itemsize=10, shape=(), dflt='', pos=None)
   /   /}
   /}

*****End of the Attest *****



```

