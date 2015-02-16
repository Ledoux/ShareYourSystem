

<!--
FrozenIsBool False
-->

#Grasper

##Doc
----


>
> A Grasper can get a GraspedGetVariable depending if the GraspingGetVariable
> is a PathStr, a GraspDict or directly the Variable itself.
>
>

----

<small>
View the Grasper notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyou
rsystem.ouvaton.org/Grasper.ipynb)
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


A Grasper can get a GraspedGetVariable depending if the GraspingGetVariable
is a PathStr, a GraspDict or directly the Variable itself.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Pather"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
#</ImportSpecificModules>

#<DefineLocals>
class GraspDictClass(collections.OrderedDict):pass
SYS.GraspDictClass=GraspDictClass
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class GrasperClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'GraspingClueVariable',
'GraspedAnswerVariable',
'GraspedClueVariableType'
                                                        ]

        def default_init(self,
                                _GraspingClueVariable=None,
                                _GraspedAnswerVariable=None,
                                _GraspedClueVariableType=None,
                                **_KwargVariablesDict
                                ):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_grasp(self):

                #type
                self.GraspedClueVariableType=type(self.GraspingClueVariable)

                #debug
                '''
                self.debug(
                                        [
                                                ('self.',self,[
'GraspedClueVariableType',
'GraspingClueVariable'
                                                                        ])
                                        ]
                                )
                '''

                #Check
                if self.GraspedClueVariableType in SYS.StrTypesList:

                        #debug
                        '''
                        self.debug('We get with a pathstr')
                        '''

                        #It is a get through a PathStr
self.GraspedAnswerVariable=self[self.GraspingClueVariable]

                elif self.GraspedClueVariableType==GraspDictClass:

                        #debug
                        '''
                        self.debug('We get with a GraspDict')
                        '''

                        #Check
                        if type(self.GraspingClueVariable['HintVariable']) in
SYS.StrTypesList:

                                #debug
                                '''
                                self.debug(
                                                        [
                                                                'We get with a
pathstr in the GraspDict',
"self.GraspingClueVariable['HintVariable'] is
"+self.GraspingClueVariable['HintVariable']
                                                        ]
                                                )
                                '''

                                #The GraspDict has maybe a path str to get the
thing
self.GraspedAnswerVariable=self[self.GraspingClueVariable['HintVariable']]

                        else:

                                #debug
                                '''
                                self.debug('We get direct in the GraspDict')
                                '''

                                #The GraspDict has maybe a path str to get the
thing
self.GraspedAnswerVariable=self.GraspingClueVariable['HintVariable']

                else:

                        #It is already getted
                        self.GraspedAnswerVariable=self.GraspingClueVariable


#</DefineClass>


```

<small>
View the Grasper sources on <a href="https://github.com/Ledoux/ShareYourSystem/t
ree/master/Pythonlogy/ShareYourSystem/Itemizers/Grasper"
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
from ShareYourSystem.Standards.Itemizers import Grasper

#Explicit expression
MyGrasper=Grasper.GrasperClass().__setitem__(
    'ChildGrasper',
    Grasper.GrasperClass().__setitem__('MyStr',"hello")
)

#Return
SYS._attest(
    [
        "MyGrasper.grasp('/ChildGrasper/MyStr').GraspedAnswerVariable is "+
        str(
            MyGrasper.grasp('/ChildGrasper/MyStr').GraspedAnswerVariable
            ),
        "MyGrasper.grasp(MyGrasper.ChildGrasper).GraspedAnswerVariable is "+
        str(
            MyGrasper.grasp(MyGrasper.ChildGrasper).GraspedAnswerVariable
            ),
        "MyGrasper.grasp(SYS.GraspDictClass(**{'HintVariable':'/ChildGrasper/MyS
tr'})).GraspedAnswerVariable is "+
        str(
MyGrasper.grasp(SYS.GraspDictClass(**{'HintVariable':'/ChildGrasper/MyStr'})
            ).GraspedAnswerVariable),
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

MyGrasper.grasp('/ChildGrasper/MyStr').GraspedAnswerVariable is hello

------

MyGrasper.grasp(MyGrasper.ChildGrasper).GraspedAnswerVariable is <
(GrasperClass), 4554553936>
   /{
   /  '<New><Instance>IdInt' : 4554553936
   /  '<New><Instance>MyStr' : hello
   /  '<Spe><Class>GraspedAnswerVariable' : None
   /  '<Spe><Class>GraspedClueVariableType' : None
   /  '<Spe><Class>GraspingClueVariable' : None
   /}

------

MyGrasper.grasp(SYS.GraspDictClass(**{'HintVariable':'/ChildGrasper/MyStr'})).Gr
aspedAnswerVariable is hello

*****End of the Attest *****



```

