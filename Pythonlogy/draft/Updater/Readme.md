

<!--
FrozenIsBool False
-->

#Updater

##Doc
----


>
> An Updater maps a __setitem__
>
>

----

<small>
View the Updater notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyou
rsystem.ouvaton.org/Updater.ipynb)
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


An Updater maps a __setitem__

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Applyiers.Gatherer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class UpdaterClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'UpdatingItemVariable'
                                                        ]

        def default_init(self,
                                _UpdatingItemVariable=None,
                                **_KwargVariablesDict):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_update(self):
                """ """

                #debug
                '''
                self.debug("self.UpdatingItemVariable is
"+Representer.represent(
self.UpdatingItemVariable,**{'RepresentingAlineaIsBool':False}))
                '''

                #Apply
                self.map('__setitem__',map(
                                                                        lambda
__UpdatingItemTuple:
{'LiargVariablesList':__UpdatingItemTuple},
self.UpdatingItemVariable.items()
                                                                        if
hasattr(self.UpdatingItemVariable,'items')
                                                                        else
(self.UpdatingItemVariable
if self.UpdatingItemVariable !=None
else []
                                                                        )
                                                                )
                )

                #Return
                #return self
#</DefineClass>

```

<small>
View the Updater sources on <a href="https://github.com/Ledoux/ShareYourSystem/t
ree/master/Pythonlogy/ShareYourSystem/Applyiers/Updater"
target="_blank">Github</a>
</small>




<!---
FrozenIsBool True
-->

##Example

Update is possible with a TuplesList or a Dict (and OrderedDict)

```python
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Applyiers import Updater

#Update several things
MyUpdater=Updater.UpdaterClass(
    ).update(
        [
            ('MyInt',0),
            ('MyFloat',0.2)
        ]
    ).update(
        {
            'MyStr':"hello"
        }
    )

#Definition the AttestedStr
SYS._attest(
    [
        'MyUpdater is '+SYS._str(
        MyUpdater,
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

MyUpdater is < (UpdaterClass), 4555210640>
   /{
   /  '<New><Instance>IdInt' : 4555210640
   /  '<New><Instance>MyFloat' : 0.2
   /  '<New><Instance>MyInt' : 0
   /  '<New><Instance>MyStr' : hello
   /  '<Spe><Instance>UpdatingItemVariable' :
   /   /{
   /   /  'MyStr' : hello
   /   /}
   /}

*****End of the Attest *****



```

