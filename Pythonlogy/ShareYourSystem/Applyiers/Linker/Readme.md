

<!--
FrozenIsBool False
-->

#Linker

##Doc
----


>
> An Linker maps a point
>
>

----

<small>
View the Linker notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyour
system.ouvaton.org/Linker.ipynb)
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


An Linker maps a point

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Applyiers.Updater"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class LinkerClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'LinkingPointListsList'
                                                        ]

        def default_init(self,
                                _LinkingPointListsList=None,
                                **_KwargVariablesDict):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_link(self):
                """ """

                #debug
                '''
                self.debug(('self.',self,['LinkingPointListsList']))
                '''

                #Apply
                self.map('point',map(
                                                                lambda
__LinkingPointList:
{'LiargVariablesList':__LinkingPointList},
self.LinkingPointListsList
                                                        )
                )

                #Return
                #return self

#</DefineClass>



```

<small>
View the Linker sources on <a href="https://github.com/Ledoux/ShareYourSystem/tr
ee/master/Pythonlogy/ShareYourSystem/Applyiers/Linker"
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
from ShareYourSystem.Itemizers import Pather
from ShareYourSystem.Applyiers import Linker

#Update several things
MyLinker=Linker.LinkerClass().update(
    map(
            lambda __Int:
            (str(__Int)+'Pather',Pather.PatherClass()),
            xrange(3)
        )
)

#link
MyLinker.link(
        map(
                lambda __Int:
(str(__Int)+'Pather','/'+str(__Int-1)+'Pather/'+str(__Int)+'Pather')
                if __Int>0
                else
                (str(0)+'Pather','/2Pather/0Pather'),
                xrange(3)
            )
        )

#Definition the AttestedStr
SYS._attest(
    [
        'MyLinker is '+SYS._str(
        MyLinker,
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

MyLinker is < (LinkerClass), 4554250000>
   /{
   /  '<New><Instance>0Pather' : < (PatherClass), 4554324240>
   /   /{
   /   /  '<New><Instance>IdInt' : 4554324240
   /   /  '<Spe><Class>PathedChildKeyStr' :
   /   /  '<Spe><Class>PathedGetKeyStr' :
   /   /  '<Spe><Class>PathedKeyStrsList' : None
   /   /  '<Spe><Class>PathingKeyStr' :
   /   /}
   /  '<New><Instance>1Pather' : < (PatherClass), 4554323856>
   /   /{
   /   /  '<New><Instance>IdInt' : 4554323856
   /   /  '<Spe><Class>PathedChildKeyStr' :
   /   /  '<Spe><Class>PathedGetKeyStr' :
   /   /  '<Spe><Class>PathedKeyStrsList' : None
   /   /  '<Spe><Class>PathingKeyStr' :
   /   /}
   /  '<New><Instance>2Pather' : < (PatherClass), 4554323216>
   /   /{
   /   /  '<New><Instance>IdInt' : 4554323216
   /   /  '<Spe><Class>PathedChildKeyStr' :
   /   /  '<Spe><Class>PathedGetKeyStr' :
   /   /  '<Spe><Class>PathedKeyStrsList' : None
   /   /  '<Spe><Class>PathingKeyStr' :
   /   /}
   /  '<New><Instance>IdInt' : 4554250000
   /  '<Spe><Instance>LinkingPointListsList' :
   /   /[
   /   /  0 : ('0Pather', '/2Pather/0Pather')
   /   /  1 : ('1Pather', '/0Pather/1Pather')
   /   /  2 : ('2Pather', '/1Pather/2Pather')
   /   /]
   /}

*****End of the Attest *****



```

