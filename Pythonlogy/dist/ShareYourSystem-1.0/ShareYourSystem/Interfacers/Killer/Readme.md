

<!--
FrozenIsBool False
-->

#Killer

##Doc
----


>
> The Killer
>
>

----

<small>
View the Killer notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyour
system.ouvaton.org/Killer.ipynb)
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


The Killer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Interfacers.Statuser"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import os
#</ImportSpecificModules>

#<DefineDoStrsList>
DoStrsList=["Killer","Kill","Killing","Killed"]
#<DefineDoStrsList>

#<DefineClass>
@DecorationClass()
class KillerClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
                                                        ]

        def default_init(self,
                                                **_KwargVariablesDict
                                        ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_kill(self):

                #first status
                self.status()

                #debug
                '''
                self.debug(('self.',self,['StatusedIdStrsList']))
                '''

                #map kill the other previous process
                if self.StatusingProcessStr=='Python' and
len(self.StatusedIdStrsList)>1:
                        map(
                                lambda __IdStr:
                                os.popen("kill "+__IdStr),
                                sorted(self.StatusedIdStrsList)[:-1]
                        )

                #Return self
                #return self

#</DefineClass>

```

<small>
View the Killer sources on <a href="https://github.com/Ledoux/ShareYourSystem/tr
ee/master/Pythonlogy/ShareYourSystem/Interfacers/Killer"
target="_blank">Github</a>
</small>



```python
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Interfacers import Killer

#Definition a Killer
MyKiller=Killer.KillerClass().kill(**{'StatusingProcessStr':"Python"})

#Definition the AttestedStr
SYS._attest(
    [
        'MyKiller is '+SYS._str(
        MyKiller,
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

MyKiller is < (KillerClass), 4554095568>
   /{
   /  '<New><Instance>IdInt' : 4554095568
   /}

*****End of the Attest *****



```

