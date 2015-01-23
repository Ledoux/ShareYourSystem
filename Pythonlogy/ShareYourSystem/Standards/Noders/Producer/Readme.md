

<!--
FrozenIsBool False
-->

#Producer

##Doc
----


>
> Producer instances
>
>

----

<small>
View the Producer notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyo
ursystem.ouvaton.org/Producer.ipynb)
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


Producer instances

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Applyiers.Pusher"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Noders import Noder
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class ProducerClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'ProducingCollectionKeyStrsList',
'ProducingPushClass',
'ProducingUpdateVariable',
'ProducedPushList'
                                                                ]

        def default_init(self,
_ProducingCollectionKeyStrsList=None,
_ProducingPushClass=Noder.NoderClass,
                                                _ProducingUpdateVariable=None,
                                                _ProducedPushList=None,
                                                **_KwargVariablesDict
                                        ):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_produce(self):

                #set
                self.ProducedPushList=map(
                                                                        lambda
__ProducingCollectionKeyStr:
                                                                        [
__ProducingCollectionKeyStr,
self.ProducingPushClass().update(
        self.ProducingUpdateVariable
)
                                                                        ],
self.ProducingCollectionKeyStrsList
                                                                )

                #debug
                '''
                self.debug(('self.',self,['ProducedPushList']))
                '''

                #push
                self.push(
                                        _StoreListsList=self.ProducedPushList
                                )

                #Return self
                #return self

#</DefineClass>


```

<small>
View the Producer sources on <a href="https://github.com/Ledoux/ShareYourSystem/
tree/master/Pythonlogy/ShareYourSystem/Applyiers/Producer"
target="_blank">Github</a>
</small>



```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Standards.Noders import Noder
from ShareYourSystem.Applyiers import Producer

#produce
MyProducer=Producer.ProducerClass().produce(
        ['First','Second'],
        Noder.NoderClass,
        {'MyInt':0},
        **{'CollectingCollectionStr':'Nodome'}
    )

#Definition the AttestedStr
SYS._attest(
    [
        'MyProducer is '+SYS._str(
        MyProducer,
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

MyProducer is < (ProducerClass), 4555020560>
   /{
   /  '<New><Instance>IdInt' : 4555020560
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopProducer
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>NodomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstNoder' : < (NoderClass), 4555021392>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4555021392
   /   /   /  '<New><Instance>MyInt' : 0
   /   /   /  '<New><Instance>NodeCollectionStr' : Nodome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstNoder
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (ProducerClass),
4555020560>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4555324088>
   /   /   /  '<Spe><Class>NodedCollectionIndexInt' : -1
   /   /   /  '<Spe><Class>NodedCollectionOrderedDict' : None
   /   /   /  '<Spe><Class>NodedCollectionStr' :
   /   /   /  '<Spe><Class>NodedKeyStr' :
   /   /   /  '<Spe><Class>NodingCollectionStr' :
   /   /   /}
   /   /  'SecondNoder' : < (NoderClass), 4555021584>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4555021584
   /   /   /  '<New><Instance>MyInt' : 0
   /   /   /  '<New><Instance>NodeCollectionStr' : Nodome
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondNoder
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (ProducerClass),
4555020560>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4555324088>
   /   /   /  '<Spe><Class>NodedCollectionIndexInt' : -1
   /   /   /  '<Spe><Class>NodedCollectionOrderedDict' : None
   /   /   /  '<Spe><Class>NodedCollectionStr' :
   /   /   /  '<Spe><Class>NodedKeyStr' :
   /   /   /  '<Spe><Class>NodingCollectionStr' :
   /   /   /}
   /   /}
   /  '<Spe><Instance>ProducedPushList' :
   /   /[
   /   /  0 :
   /   /   /[
   /   /   /  0 : First
   /   /   /  1 : {...}< (NoderClass), 4555021392>
   /   /   /]
   /   /  1 :
   /   /   /[
   /   /   /  0 : Second
   /   /   /  1 : {...}< (NoderClass), 4555021584>
   /   /   /]
   /   /]
   /  '<Spe><Instance>ProducingCollectionKeyStrsList' : ['First', 'Second']
   /  '<Spe><Instance>ProducingPushClass' : <class
'ShareYourSystem.Standards.Noders.Noder.NoderClass'>
   /  '<Spe><Instance>ProducingUpdateVariable' :
   /   /{
   /   /  'MyInt' : 0
   /   /}
   /}

*****End of the Attest *****



```

