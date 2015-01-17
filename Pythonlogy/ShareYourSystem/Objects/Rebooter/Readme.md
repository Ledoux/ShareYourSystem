

<!--
FrozenIsBool False
-->

#Rebooter

##Doc
----


>
> The Rebooter
>
>

----

<small>
View the Rebooter notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyo
ursystem.ouvaton.org/Rebooter.ipynb)
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


The Rebooter

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Objects.Concluder"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import copy
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class RebooterClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
                'RebootingDoStrsList',
                'RebootingNameStrsList',
                'RebootingAllDoBool',
                'RebootingAllNameBool',
                'RebootingDoingIsBool',
                'RebootedWatchBoolKeyStrsList',
                'RebootingSetDoIsBool'
        ]

        def default_init(self,
                                                _RebootingNameStrsList=None,
                                                _RebootingDoStrsList=None,
                                                _RebootingAllNameBool=True,
                                                _RebootingAllDoBool=True,
                                                _RebootingSetDoIsBool=True,
_RebootedWatchBoolKeyStrsList=None,
                                                **_KwargVariablesDict
                                        ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_reboot(self):

                #set
                if self.RebootingAllNameBool:

                        #filter
                        self.RebootingNameStrsList=SYS.filterNone(
                                map(
                                        lambda __MroClass:
                                        __MroClass.NameStr
                                        if hasattr(__MroClass,'DoStr')
                                        else None,
                                        self.__class__.__mro__
                                )
                        )

                #set
                if self.RebootingAllDoBool:

                        #filter
                        self.RebootingDoStrsList=SYS.filterNone(
                                map(
                                        lambda __MroClass:
                                        __MroClass.DoStr
                                        if hasattr(__MroClass,'DoStr')
                                        else None,
                                        self.__class__.__mro__
                                )
                        )

                #debug
                '''
                self.debug(
                                        ('self.',self,[
                                                'RebootingDoStrsList',
                                                'RebootingNameStrsList'
                                                ])
                                )
                '''

                #map
                map(
                                lambda __RebootingNameStr:
                                self.setSwitch(
                                        __RebootingNameStr,
                                        self.RebootingDoStrsList
                                ),
                                self.RebootingNameStrsList
                        )


                #Check
                if self.RebootingSetDoIsBool:

                        #debug
                        '''
                        self.debug(('self.',self,['RebootingNameStrsList']))
                        '''

                        #map
                        map(
                                        lambda __RebootingClass:
                                        self.setDone(
                                                __RebootingClass
                                        )
                                        #if
hasattr(__RebootingClass,'DoneAttributeVariablesOrderedDict')
                                        #else None,
                                        ,map(
                                                        lambda
__RebootingClassStr:
                                                        getattr(
                                                                SYS,
__RebootingClassStr
                                                        )
                                                        #if
hasattr(SYS,__RebootingClassStr)
                                                        #else None
,map(SYS.getClassStrWithNameStr,self.RebootingNameStrsList)
                                                )
                                )


#</DefineClass>


```

<small>
View the Rebooter sources on <a href="https://github.com/Ledoux/ShareYourSystem/
tree/master/Pythonlogy/ShareYourSystem/Objects/Rebooter"
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
from ShareYourSystem.Objects import Rebooter

#Definition
@Classer.ClasserClass(**
{
    'ClassingSwitchMethodStrsList':['make']
})
class MakerClass(Rebooter.RebooterClass):

    #Definition
    RepresentingKeyStrsList=[
                                'MakingMyFloat',
                                'MadeMyInt'
                            ]

    def default_init(self,
                    _MakingMyFloat=0.,
                    _MadeMyInt=0,
                    **_KwarVariablesDict
                ):
        Rebooter.RebooterClass.__init__(self,**_KwarVariablesDict)

    def do_make(self):

        #print
        print('I am in the do_make of the Maker')

        #cast
        self.MadeMyInt=int(self.MakingMyFloat)

#Definition
@Classer.ClasserClass(**{
    'ClassingSwitchMethodStrsList':["make"]
})
class BuilderClass(MakerClass):

    #Definition
    RepresentingKeyStrsList=[
                            ]

    def default_init(self,
                    **_KwarVariablesDict
                ):
        MakerClass.__init__(self,**_KwarVariablesDict)

    def mimic_make(self):

        #print
        print('I am in the mimic_make of the Builder')

        #call the parent method
        MakerClass.make(self)

        #cast
        self.MadeMyInt+=10

    def do_build(self):
        pass


#Definition an instance
MyBuilder=BuilderClass()

#Print
print('Before make, MyBuilder is ')
SYS._print(MyBuilder,**{
    'RepresentingKeyStrsList':[
    'MakingMyFloat',
    'MadeMyInt',
    ]
})

#make once
MyBuilder.make(3.)

#Print
print('After the first make, MyBuilder is ')
SYS._print(MyBuilder,**{
    'RepresentingKeyStrsList':[
    'MakingMyFloat',
    'MadeMyInt',
    ]
})

#make again
MyBuilder.make(5.)

#Print
print('After the second make, MyBuilder is ')
SYS._print(MyBuilder,**{
    'RepresentingKeyStrsList':[
    'MakingMyFloat',
    'MadeMyInt',
    ]
})

#make again
print('Now we reboot')
MyBuilder.reboot(
                    #_NameStrsList=['Maker','Builder'],
                    #_DoStrsList=['Make'],
                    #_AllDoBool=True,
                    #_AllNameBool=True,
                )

#Print
print('After the reboot, MyBuilder is ')
SYS._print(MyBuilder,**{
    'RepresentingKeyStrsList':[
    'MakingMyFloat',
    'MadeMyInt',
    ]
})

#make again
MyBuilder.make(8.)

#Definition the AttestedStr
SYS._attest(
    [
        'MyBuilder is '+SYS._str(
        MyBuilder,
        **{
            'RepresentingAlineaIsBool':False,
            'RepresentingKeyStrsList':[
                'MakingMyFloat',
                'MadeMyInt',
                'RebootedWatchBoolKeyStrsList'
            ]
            }
        )
    ]
)

```


```console
>>>
Before make, MyBuilder is
< (BuilderClass), 4537162128>
   /{
   /  '<Base><Class>MadeMyInt' : 0
   /  '<Base><Class>MakingMyFloat' : 0.0
   /  '<New><Instance>IdInt' : 4537162128
   /}
I am in the mimic_make of the Builder
I am in the do_make of the Maker
After the first make, MyBuilder is
< (BuilderClass), 4537162128>
   /{
   /  '<New><Instance>IdInt' : 4537162128
   /  '<Spe><Instance>MadeMyInt' : 13
   /  '<Spe><Instance>MakingMyFloat' : 3.0
   /}
After the second make, MyBuilder is
< (BuilderClass), 4537162128>
   /{
   /  '<New><Instance>IdInt' : 4537162128
   /  '<Spe><Instance>MadeMyInt' : 13
   /  '<Spe><Instance>MakingMyFloat' : 3.0
   /}
Now we reboot
After the reboot, MyBuilder is
< (BuilderClass), 4537162128>
   /{
   /  '<New><Instance>IdInt' : 4537162128
   /  '<Spe><Instance>MadeMyInt' : 0
   /  '<Spe><Instance>MakingMyFloat' : 3.0
   /}
I am in the mimic_make of the Builder
I am in the do_make of the Maker


*****Start of the Attest *****

MyBuilder is < (BuilderClass), 4537162128>
   /{
   /  '<New><Instance>IdInt' : 4537162128
   /  '<Spe><Instance>MadeMyInt' : 18
   /  '<Spe><Instance>MakingMyFloat' : 8.0
   /  '<Spe><Instance>RebootedWatchBoolKeyStrsList' : []
   /}

*****End of the Attest *****



```

