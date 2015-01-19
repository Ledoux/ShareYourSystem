

<!--
FrozenIsBool False
-->

#Featurer

##Doc
----


>
> Featurer instances helps for defining Databaser where all
> the rowed variables are identifying items.
>
>

----

<small>
View the Featurer notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyo
ursystem.ouvaton.org/Featurer.ipynb)
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


Featurer instances helps for defining Databaser where all
the rowed variables are identifying items.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Modelers.Hierarchizer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Modelers import Rower
#</ImportSpecificModules>


#<DefineClass>
@DecorationClass()
class FeaturerClass(
                                        BaseClass
                                ):

        #Definition
        RepresentingKeyStrsList=[
'FeaturingAllBool',
'FeaturedJoinDatabasersList'
                                                                ]

        def default_init(self,
                                                _FeaturingAllBool=False,
                                                _FeaturingJoinFlushBool=True,
_FeaturedJoinDatabasersList=None,
                                                **_KwargVariablesDict
                                        ):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def mimic_model(self):

                #<NotHook>
                #feature first
                self.feature()
                #</NotHook>

                #<NotHook>
                #model then
                BaseClass.model(self)
                #</NotHook>

                #<NotHook>
                #Return self
                #return self
                #</NotHook>


        def mimic_row(self):

                #debug
                '''
                self.debug(('self.',self,self.__class__.DoingAttributeVariablesO
rderedDict.keys()))
                '''

                #Put all the GettingStrsList in the identifying container
                if self.FeaturingAllBool:

                        #debug
                        '''
                        self.debug('Set the RowingGetStrsList with all the
DatabasingGetStrs')
                        '''

                        #set
                        self['Attr_RowingGetStrsList']=SYS.unzip(
                        self.DatabasingSealTuplesList,
                        [0]
                )

                        #debug
                        '''
self.debug(('self.',self,['RowingGetStrsList','DatabasingSealTuplesList']))
                        '''

                #<NotHook>
                #row then
                BaseClass.row(self)
                #</NotHook>

                #<NotHook>
                #Return self
                #return self
                #</NotHook>

        def mimic_flush(self):

                #<NotHook>
                #feature first
                self.feature()
                #</NotHook>

                #debug
                '''
                self.debug(('self.',self,['FeaturingJoinFlushBool']))
                '''

                #Check
                if len(self.FeaturedJoinDatabasersList)>0 and
self.FeaturingJoinFlushBool:

                        #debug
                        '''
                        self.debug('flush in the joined featured databasers')
                        '''

                        #set
                        self.FeaturingJoinFlushBool=False

                        #map
                        map(
                                        lambda __FeaturedDatabaser:
                                        __FeaturedDatabaser.flush(),
                                        self.FeaturedJoinDatabasersList
                                )

                        #set
                        self.FeaturingJoinFlushBool=True

                        #Return
                        return

                else:

                        #debug
                        self.debug('flush now here')

                        #flush directly
                        BaseClass.flush(self)

        def do_feature(self):

                #Check
                if self.NodePointDeriveNoder!=None:

                        #map
                        self.FeaturedJoinDatabasersList=SYS.filterNone(
                                map(
                                        lambda __NodedDatabaser:
                                        __NodedDatabaser if hasattr(
__NodedDatabaser,'JoiningDownGetKeyStrsList')
                                        and
__NodedDatabaser.JoiningDownGetKeyStrsList !=None and
                                        self.NodedDatabaseKeyStr in
__NodedDatabaser.JoiningDownGetKeyStrsList
                                        else None,
self.DatabasedDeriveDatabasersOrderedDict.values()
                                )
                        )

                #debug
                '''
                self.debug(('self.',self,['FeaturedJoinDatabasersList']))
                '''

#</DefineClass>

```

<small>
View the Featurer sources on <a href="https://github.com/Ledoux/ShareYourSystem/
tree/master/Pythonlogy/ShareYourSystem/Databasers/Featurer"
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
from ShareYourSystem.Classors import Classer
from ShareYourSystem.Functers import Triggerer
from ShareYourSystem.Noders import Structurer
from ShareYourSystem.Modelers import Featurer,Joiner
import tables
import operator

MyFeaturer=Featurer.FeaturerClass()

#Definition the AttestedStr
SYS._attest(
    [
        'MyFeaturer is '+SYS._str(
        MyFeaturer,
        **{
            'RepresentingBaseKeyStrsListBool':False,
            'RepresentingAlineaIsBool':False
        }
        ),
        'hdf5 file is : '+MyFeaturer.hdfview().hdfclose().HdformatedStr
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

MyFeaturer is < (FeaturerClass), 4564994576>
   /{
   /  '<New><Instance>IdInt' : 4564994576
   /  '<New><Instance>NewtorkAttentionStr' :
   /  '<New><Instance>NewtorkCatchStr' :
   /  '<New><Instance>NewtorkCollectionStr' :
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopFeaturer
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<Spe><Class>FeaturedJoinDatabasersList' : None
   /  '<Spe><Class>FeaturingAllBool' : False
   /}

------

hdf5 file is :

*****End of the Attest *****



```

