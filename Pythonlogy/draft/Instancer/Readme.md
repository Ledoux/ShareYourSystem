

<!--
FrozenIsBool False
-->

#Instancer

##Doc
----


>
> An Appender append by doing a set in a NodedOrderedDict thanks to the
<AppendedNodeStr><AppendedNodeKeyStr>
>
>

----

<small>
View the Instancer notebook on [NbViewer](http://nbviewer.ipython.org/url/sharey
oursystem.ouvaton.org/Instancer.ipynb)
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


An Appender append by doing a set in a NodedOrderedDict thanks to the
<AppendedNodeStr><AppendedNodeKeyStr>

"""


#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Noders.Appender"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>

Appender=BaseModule
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class InstancerClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'InstancingVariable',
'InstancingClass',
'InstancingIsBool',
'InstancedVariable'
                                                                ]

        def default_init(self,
                                                _InstancingVariable=None,
                                                _InstancingClass=None,
                                                _InstancingIsBool=False,
                                                _InstancedVariable=None,
                                                **_KwargVariablesDict
                                        ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        #@Imitater.ImitaterClass()
        def mimic_append(self):

                #Instance first
                self.instance()

                #Append then
                Appender.AppenderClass.append(self,self.InstancedVariable)

                #Return self
                return self

        def do_instance(self):
                """ """

                #Check
                if self.InstancingIsBool:

                        #Init
                        InstancingClass=None

                        #TuplesList Case
                        if SYS.getIsTuplesListBool(self.InstancingVariable):

                                #debug
                                '''
                                self.debug('This is a tuples list')
                                '''

                                if self.InstancingClass==None:

                                        #debug
                                        '''
                                        self.debug('Find the instancing class')
                                        '''

                                        #Definition the KeyStrsList
KeyStrsList=SYS.unzip(self.InstancingVariable,[0])

                                        try:
InstancingClass=self.InstancingVariable[KeyStrsList.index('InstancingClass')][1]
                                        except:
                                                pass

                                else:
                                        InstancingClass=self.InstancingClass

                                #Check
                                if InstancingClass!=None:

                                        #Init
                                        self.InstancedVariable=InstancingClass()

                                        #Map
                                        map(
                                                        lambda __ItemTuple:
self.InstancedVariable.__setattr__(*__ItemTuple),
                                                        self.InstancingVariable
                                                )

                                        #debug
                                        '''
                                        self.debug(('vars
',vars(),['InstancedVariable']))
                                        '''

                        elif hasattr(self.InstancingVariable,'items'):

                                #debug
                                '''
                                self.debug('This is an itemizing thing')
                                '''

                                if self.InstancingClass==None:

                                        #debug
                                        '''
                                        self.debug('Find the instancing class')
                                        '''

                                        try:
InstancingClass=self.InstancingVariable['InstancingClass']
                                        except:
                                                pass
                                else:

                                        #Definition
                                        InstancingClass=self.InstancingClass

                                if InstancingClass!=None:

                                        #Init
                                        self.InstancedVariable=InstancingClass()

                                        #Map
                                        map(
                                                        lambda __ItemTuple:
self.InstancedVariable.__setattr__(*__ItemTuple),
self.InstancingVariable.items()
                                                )

                        elif hasattr(self.InstancingVariable,'__dict__'):

                                #Check
                                if self.InstancingClass!=None:

                                        #Init
self.InstancedVariable=self.InstancingClass()

                #Return self
                #return self

#</DefineClass>

```

<small>
View the Instancer sources on <a href="https://github.com/Ledoux/ShareYourSystem
/tree/master/Pythonlogy/ShareYourSystem/Noders/Instancer"
target="_blank">Github</a>
</small>



```python
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Appender,Instancer

#Append with a TuplesList
MyInstancer=Instancer.InstancerClass(**{'InstancingIsBool':True}).instance([
                                    ('AppendingNodeCollectionStr','Structure'),
                                    ('NodeKeyStr','MyInstancedAppender'),
                                    ('MyStr','Hello'),
                                    ('InstancingClass',Appender.AppenderClass)
                                ]
                            )

#Definition the AttestedStr
SYS._attest(
    [
        'MyInstancer is '+SYS._str(
        MyInstancer,
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

MyInstancer is < (InstancerClass), 4556355984>
   /{
   /  '<New><Instance>IdInt' : 4556355984
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopInstancer
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<Spe><Class>InstancingClass' : None
   /  '<Spe><Instance>InstancedVariable' : < (AppenderClass), 4556356304>
   /   /{
   /   /  '<New><Instance>AppendingNodeCollectionStr' : Structure
   /   /  '<New><Instance>IdInt' : 4556356304
   /   /  '<New><Instance>InstancingClass' : <class
'ShareYourSystem.Noders.Appender.AppenderClass'>
   /   /  '<New><Instance>MyStr' : Hello
   /   /  '<New><Instance>NodeCollectionStr' : Globals
   /   /  '<New><Instance>NodeIndexInt' : -1
   /   /  '<New><Instance>NodeKeyStr' : MyInstancedAppender
   /   /  '<New><Instance>NodePointDeriveNoder' : None
   /   /  '<New><Instance>NodePointOrderedDict' : None
   /   /  '<Spe><Class>AppendedNodeCollectionStr' :
   /   /  '<Spe><Class>AppendedNodeKeyStr' :
   /   /  '<Spe><Class>AppendingCollectionVariable' : None
   /   /}
   /  '<Spe><Instance>InstancingIsBool' : True
   /  '<Spe><Instance>InstancingVariable' :
   /   /[
   /   /  0 : ('AppendingNodeCollectionStr', 'Structure')
   /   /  1 : ('NodeKeyStr', 'MyInstancedAppender')
   /   /  2 : ('MyStr', 'Hello')
   /   /  3 :
   /   /   /(
   /   /   /  0 : InstancingClass
   /   /   /  1 : {...}< (type), 140476488391344>
   /   /   /)
   /   /]
   /}

*****End of the Attest *****



```

