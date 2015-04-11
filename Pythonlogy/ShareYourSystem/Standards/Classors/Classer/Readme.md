

<!--
FrozenIsBool False
-->

#Classer

##Doc
----


>
> The Classer
>
>

----

<small>
View the Classer notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyou
rsystem.ouvaton.org/Classer.ipynb)
</small>




<!---
FrozenIsBool True
-->

##Example

Note that now setting a propertize method in a derived class works also and
overwrite the previous one. (without redefine the property)

```python
#ImportModules
import ShareYourSystem as SYS

#Define
@SYS.ClasserClass()
class MakerClass(object):

    def default_init(self,
            _MakingMyFloat={
                            'DefaultValueType':property,
                            'PropertyInitVariable':3.,
                            'PropertyDocStr':'I am doing the thing here'
                            },
            _MakingMyList={
                            'DefaultValueType':property,
                            'PropertyInitVariable':[],
                            'PropertyDocStr':'I am doing the thing here'
                            },
            _MakingMyInt={'DefaultValueType':int},
            _MadeMyInt=0
        ):
        object.__init__(self)

    def propertize_setMakingMyFloat(self,_SettingValueVariable):

        #Print
        #print('I am going to make the job directly !')

        #set the value of the "hidden" property variable
        self._MakingMyFloat=_SettingValueVariable

        #Bind with MadeInt setting
        self.MadeMyInt=int(self._MakingMyFloat)

    def propertize_setMakingMyList(self,_SettingValueVariable):

        #set the value of the "hidden" property variable
        self._MakingMyList=_SettingValueVariable+['Hellllllo']


#Define
@SYS.ClasserClass()
class BuilderClass(MakerClass):

    def default_init(
                        self
                    ):
        SYS.MakerClass.__init__(self)

    def propertize_setMakingMyList(self,_SettingValueVariable):

        #call the base method
        MakerClass.propertize_setMakingMyList(self,_SettingValueVariable)

        #set the value of the "hidden" property variable
        self._MakingMyList+=['Build en plus !']

#Definition a special instance
SpecialBuilder=BuilderClass(_MakingMyFloat=5,_MakingMyList=[4])

#Definition the AttestedStr
print('\n'.join(
    [
        'What are you saying SpecialBuilder ?',
        'SpecialBuilder.__dict__ is '+str(SpecialBuilder.__dict__),
        'SpecialBuilder.MakingMyFloat is '+str(SpecialBuilder.MakingMyFloat),
        'SpecialBuilder.MakingMyList is '+str(SpecialBuilder.MakingMyList),
        'SpecialBuilder.MadeMyInt is '+str(SpecialBuilder.MadeMyInt),
    ]
    )
)

#Print


```


```console
>>>
What are you saying SpecialBuilder ?
SpecialBuilder.__dict__ is {'DefaultInitBool': True}
SpecialBuilder.MakingMyFloat is 3.0
SpecialBuilder.MakingMyList is []
SpecialBuilder.MadeMyInt is 0

```



<!--
FrozenIsBool False
-->

##Code

----

<ClassDocStr>

<small>
View the Classer sources on <a href="https://github.com/Ledoux/ShareYourSystem/t
ree/master/Pythonlogy/ShareYourSystem/Standards/Classors/Classer"
target="_blank">Github</a>
</small>

----

```python
# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Classer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Classors.Mimicker"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Tester"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
Mimicker=BaseModule
from ShareYourSystem.Standards.Classors import Propertiser
#</ImportSpecificModules>

#<Define_Class>
@DecorationClass()
class ClasserClass(BaseClass):

        def default_init(self,
_ClassingSwitchMethodStrsList=None,
_ClassingWatchMethodStrsList=None,
                                                _ClassingStructureVariable=None,
                                                **_KwargVariablesDict
                                ):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def __call__(self,_Class):

                #Call the parent method
                Mimicker.MimickerClass.__bases__[0].__call__(self,_Class)

                #class
                self._class()

                #Return
                return _Class

        def do__class(self):

                #Definition the MethodsList
                ClassedFunctionsList=SYS._filter(
                        lambda __ListedVariable:
                                type(__ListedVariable).__name__=="function"
                                if hasattr(__ListedVariable,'__name__')
                                else False,
                                self.DoClass.__dict__.values()
                )

                #debug
                '''
                print('l 66 Classer')
                print("ClassedFunctionsList is ",WatchedFunctionsList)
                print('Set all the mimick methods')
                print('')
                '''

                #/###################/#
                # Mimic all that you can find
                #

                #Get all the hooking methods
                ClassedMimickFunctionsList=SYS._filter(
                        lambda __ListedVariable:
                        __ListedVariable.__name__.startswith(
                                        Mimicker.MimickingWrapPrefixStr
                        )
                        if hasattr(__ListedVariable,'__name__')
                        else False,
                        ClassedFunctionsList
                )

                #debug
                '''
                print('l 82 Classer')
                print("ClassedMimickFunctionsList is
",ClassedMimickFunctionsList)
                print('')
                '''

                #map
                map(
                                lambda __ClassedMimickFunction:
                                self.mimic(
                                        Mimicker.MimickingWrapPrefixStr.join(
__ClassedMimickFunction.__name__.split(
Mimicker.MimickingWrapPrefixStr)[1:]
                                                )
                                ),
                                ClassedMimickFunctionsList
                        )

                #/###################/#
                # Set the watch methods
                #

                #debug
                '''
                print('l 104 Classer')
                print('set the watch functions')
                print('self.ClassingWatchMethodStrsList is
',self.ClassingWatchMethodStrsList)
                print('self.DoClass.DoMethodStr is ',self.DoClass.DoMethodStr)
                print('')
                '''

                #map
                map(
                                lambda __ClassingWatchUnboundMethodStr:
                                self.watch(
                                        True,
**{'ObservingWrapMethodStr':__ClassingWatchUnboundMethodStr}
                                ),
                                self.ClassingWatchMethodStrsList
                        )

                #/###################/#
                # Set the switch methods
                #

                #debug
                '''
                print('l 104 Classer')
                print('set the switch functions')
                print('self.ClassingSwitchMethodStrsList is
',self.ClassingSwitchMethodStrsList)
                print('self.DoClass.DoMethodStr is ',self.DoClass.DoMethodStr)
                print('')
                '''

                #map
                map(
                                lambda __ClassingSwitchUnboundMethodStr:
                                self.switch(
                                        True,
                                        __ClassingSwitchUnboundMethodStr
                                ),
                                self.ClassingSwitchMethodStrsList
                        )

                #/###################/#
                # Check for overriden propertize_ methods
                #

                #Debug
                '''
                print('Classer l 125')
                print('Check for overriden propertize_ methods ')
                print('self.DoClass.InspectMethodDict')
                print(self.DoClass.InspectMethodDict)
                print('')
                '''

                #filter
                ClassedPropertyNewMethodDict=dict(
                        SYS._filter(
                                lambda __MethodItemTuple:
                                __MethodItemTuple[0].startswith(
                                                Propertiser.PropertyPrefixStr
                                        ) and (
SYS.getNewMethodBool(self.DoClass,__MethodItemTuple[0])
                                        #getattr(
                                        #       self.DoClass.__bases__[0],
                                        #       __MethodItemTuple[0]
                                        #)!=__MethodItemTuple[1]
                                        #if hasattr(self.DoClass.__bases__[0],
                                        #       __MethodItemTuple[0]
                                        #) else True
                                ),
                                self.DoClass.InspectMethodDict.items()
                        )
                )

                #Debug
                '''
                print('Classer l 147')
                print('self.DoClass is ')
                print(self.DoClass)
                print('ClassedPropertyNewMethodDict is')
                print(SYS.indent(ClassedPropertyNewMethodDict))
                print('')
                '''

                #map
                ClassedPropertyKeyStrsList=map(
                                lambda __PropertizedKeyStr:
                                SYS.deprefix(
                                        __PropertizedKeyStr,
                                        Propertiser.PropertyPrefixStr
                                )[3:],
                                ClassedPropertyNewMethodDict.keys()
                        )

                #map reset the properties
                map(
                                lambda __PropertyKeyStr:
                                setattr(
                                                self.DoClass,
                                                __PropertyKeyStr,
                                                property(
                                                                getattr(
self.DoClass,
Propertiser.PropertyPrefixStr+'get'+__PropertyKeyStr
                                                                ),
                                                                getattr(
self.DoClass,
Propertiser.PropertyPrefixStr+'set'+__PropertyKeyStr
                                                                ),
                                                                getattr(
self.DoClass,
Propertiser.PropertyPrefixStr+'del'+__PropertyKeyStr
                                                                )
                                                        )
                                        ),
                                ClassedPropertyKeyStrsList
                        )

                #/###################/#
                # Set maybe a structure
                #

                #Check
                if self.ClassingStructureVariable!=None:

                        #Check
                        if hasattr(
                                        self.ClassingStructureVariable,'items'
                                ):
ClassedStructureVariable=self.ClassingStructureVariable.items()
                        else:
ClassedStructureVariable=self.ClassingStructureVariable


                        #debug
                        '''
                        print('Classer l 241')
                        print('We structure here')
                        print('self.ClassingStructureVariable is ')
                        print(self.ClassingStructureVariable)
                        print('')
                        '''

                        #map add the sing plurals
                        map(
                                lambda __ItemTuple:
                                SYS.addSingPlural(
                                        *__ItemTuple
                                ),
                                ClassedStructureVariable
                        )

                        #Define a class
                        class StructureClass(SYS.StructurerClass):pass
                        StructureClass.__name__=SYS.getClassStrWithNameStr(self.
DoClass.NameStr+'sStructurer')
                        StructureClass.ManagingValueClass=self.DoClass

                        #set
                        setattr(
                                self.Module,
                                StructureClass.__name__,
                                StructureClass
                        )

                        #dict
                        ClassesDict=dict(
                                        map(
                                                lambda __ItemTuple:
                                                (__ItemTuple[1],StructureClass),
                                                ClassedStructureVariable
                                        )
                                )

                        #map
                        if self.DoClass.TeamingClassesDict==None:
                                self.DoClass.TeamingClassesDict=ClassesDict
                        else:
                                self.DoClass.TeamingClassesDict.update(
                                        ClassesDict
                                )


#</DefineClass>


```


