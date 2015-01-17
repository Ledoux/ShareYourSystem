

<!--
FrozenIsBool False
-->

#Statuser

##Doc
----


>
> The Statuser
>
>

----

<small>
View the Statuser notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyo
ursystem.ouvaton.org/Statuser.ipynb)
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


The Statuser

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Interfacers.Processer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import os
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class StatuserClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'StatusingProcessStr',
'StatusedSnapshotStr',
'StatusedLineStrsList',
'StatusedIdStrsList'
                                                                ]

        def default_init(self,
                                                _StatusingProcessStr="",
                                                _StatusedSnapshotStr="",
                                                _StatusedLineStrsList=None,
                                                _StatusedIdStrsList=None,
                                                **_KwargVariablesDict
                                        ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_status(self):

                #Check
                if self.StatusingProcessStr!="":

                        #call
                        self.StatusedSnapshotStr=self.process(
                                "ps -ef | grep "+self.StatusingProcessStr
                        ).ProcessedBashStr

                        #debug
                        '''
                        self.debug(('self.',self,['StatusedSnapshotStr']))
                        '''

                        #map
                        self.StatusedLineStrsList=SYS._filter(
                                        lambda __LineStr:
                                        SYS.PythonPathStr in __LineStr,
                                        self.StatusedSnapshotStr.split('\n')
                                )

                        #debug
                        '''
                        self.debug(('self.',self,['StatusedLineStrsList']))
                        '''

                        #call
                        self.StatusedIdStrsList=map(
                                lambda __LineStr:
                                __LineStr.split()[1],
                                self.StatusedLineStrsList
                        )

                        #debug
                        '''
                        self.debug(('self.',self,['StatusedIdStrsList']))
                        '''

                #Return self
                #return self

#</DefineClass>

```

<small>
View the Statuser sources on <a href="https://github.com/Ledoux/ShareYourSystem/
tree/master/Pythonlogy/ShareYourSystem/Interfacers/Statuser"
target="_blank">Github</a>
</small>



```python
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Interfacers import Statuser
import os

#Definition a Statuser
MyStatuser=Statuser.StatuserClass().status('Python')

#Definition the AttestedStr
SYS._attest(
    [
        'MyStatuser is '+SYS._str(
        MyStatuser,
        **{
            'RepresentingBaseKeyStrsListBool':False
        }
        )
    ]
)

#Print




```


```console
>>>


*****Start of the Attest *****

MyStatuser is < (StatuserClass), 4554094352>
   /{
   /  '<New><Instance>IdInt' : 4554094352
   /  '<Spe><Instance>StatusedIdStrsList' : ['15410']
   /  '<Spe><Instance>StatusedLineStrsList' : ['  501 15410 12535   0  5:55PM
ttys000    0:01.07 /usr/local/Cellar/python/2.7.9/Frameworks/Python.framework/Ve
rsions/2.7/Resources/Python.app/Contents/MacOS/Python inform.py']
   /  '<Spe><Instance>StatusedSnapshotStr' :   501 15410 12535   0  5:55PM
ttys000    0:01.07 /usr/local/Cellar/python/2.7.9/Frameworks/Python.framework/Ve
rsions/2.7/Resources/Python.app/Contents/MacOS/Python inform.py
  501 15989 15987   0  5:56PM ttys000    0:00.00 grep Python

   /  '<Spe><Instance>StatusingProcessStr' : Python
   /}

*****End of the Attest *****



```

