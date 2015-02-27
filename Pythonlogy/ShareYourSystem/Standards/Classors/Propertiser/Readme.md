

<!--
FrozenIsBool False
-->

#Propertiser

##Doc
----


>
> The Propertiser is an augmented Defaultor because it will set defaults
attributes
> possibly in properties for the new-style decorated classes. This can set
objects
> with high controlling features thanks to the binding
>
>

----

<small>
View the Propertiser notebook on [NbViewer](http://nbviewer.ipython.org/url/shar
eyoursystem.ouvaton.org/Propertiser.ipynb)
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


The Propertiser is an augmented Defaultor because it will set defaults
attributes
possibly in properties for the new-style decorated classes. This can set objects
with high controlling features thanks to the binding

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Classors.Deriver"
DecorationModuleStr=BaseModuleStr
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import inspect
import collections

from ShareYourSystem.Standards.Objects import Initiator
#</ImportSpecificModules>

#<DefineLocals>
PropertizingGetStr="_"
PropertizingRepresentationStr="p:"
#</DefineLocals>

#<DefineFunctions>
def getPropertizedTupleWithItemTupleAndClass(_ItemTuple,_Class):

        #Get the KeyStr, and the ValueVariable that should be a dict
        PropertizedKeyStr=_ItemTuple[0]
        PropertizedValueVariable=_ItemTuple[1]
        PropertizedHideKeyStr=PropertizingGetStr+PropertizedKeyStr

        #Check that this is a property yet or not
        if type(PropertizedValueVariable)!=property:

                #Init
                PropertizedValueVariable=property()

                #Definition the get function
                PropertizedGetFunctionStr='get'+PropertizedKeyStr
                if hasattr(_Class,PropertizedGetFunctionStr):

                        #Check for an already defined method
PropertizedGetFunction=getattr(_Class,PropertizedGetFunctionStr)

                else:

                        #Definition a default one
                        def PropertizedGetFunction(self):
                                return getattr(self,PropertizedHideKeyStr)
PropertizedGetFunction.__name__=PropertizedGetFunctionStr

                #Definition the set function
                PropertizedSetFunctionStr='set'+PropertizedKeyStr

                #Check
                if hasattr(_Class,PropertizedSetFunctionStr):

                        #Check for an already defined method
PropertizedSetFunction=getattr(_Class,PropertizedSetFunctionStr)
                else:

                        #Definition a default one
                        def PropertizedSetFunction(self,_SettingValueVariable):
self.__setattr__(PropertizedHideKeyStr,_SettingValueVariable)
                        PropertizedSetFunction.__name__='set'+PropertizedKeyStr


                #Definition the del function
                PropertizedDelFunctionStr='del'+PropertizedKeyStr
                if hasattr(_Class,PropertizedDelFunctionStr):

                        #Check for an already defined method
PropertizedDelFunction=getattr(_Class,PropertizedDelFunctionStr)

                else:

                        #Definition a default one
                        def PropertizedDelFunction(self):
                                self.__delattr__(PropertizedHideKeyStr)
                        PropertizedDelFunction.__name__='del'+PropertizedKeyStr

                #Redefine
                PropertizedValueVariable=property(
                                                        PropertizedGetFunction,
                                                        PropertizedSetFunction,
                                                        PropertizedDelFunction,
_ItemTuple[1]['PropertyDocStr'
                                                        ]if 'PropertyDocStr'
in _ItemTuple[1]
                                                        else "This is here a
property but with no more details..."
                                                )

        #Definition the property
        return (
                                PropertizedKeyStr,
                                PropertizedValueVariable
                        )

def getPropertizedVariableWithItemTuple(_ItemTuple):

        #Maybe it is already defined
        if 'PropertyInitVariable' in _ItemTuple[1]:
                return _ItemTuple[1]['PropertyInitVariable']
        else:

                #Return the default one associated with the type
                return
SYS.getTypeClassWithTypeStr(SYS.getWordStrsListWithStr(_ItemTuple[0])[-1])

#</DefineFunctions>

#<Define_Class>
@DecorationClass()
class PropertiserClass(BaseClass):

        def default_init(self,
                                                **_KwargVariablesDict
                                        ):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def __call__(self,_Class):

                #debug
                '''
                print('Defaultor l.31 __call__ method')
                print('_Class is ',_Class)
                print('')
                '''

                #Call the parent init method
                BaseClass.__call__(self,_Class)

                #Debug
                '''
                print('l.146 : We are going to propertize')
                print('')
                '''

                #propertize
                self.propertize()

                #Debug
                '''
                print('l.153 : propertize is done')
                print('')
                '''

                #Return
                return _Class

        def do_propertize(self):

                #Alias
                PropertizedClass=self.DoClass

                #Debug
                '''
                print('PropertizedClass is ',PropertizedClass)
                print('')
                '''

                #debug
                '''
                print('Propertiser l.47 default method')
                print('Class is ',Class)
                print('')
                '''

                #Check
                if
hasattr(PropertizedClass,"DefaultAttributeVariablesOrderedDict"):

                        #debug
                        '''
print('PropertizedClass.DefaultAttributeVariablesOrderedDict
is',PropertizedClass.DefaultAttributeVariablesOrderedDict)
                        print('')
                        '''

                        #set the PropertizedDefaultTuplesList
PropertizedClass.PropertizedDefaultTuplesList=SYS._filter(
                                lambda __DefaultSetTuple:
                                type(__DefaultSetTuple[1]
                                        )==property or (
                                        hasattr(__DefaultSetTuple[1],'items'
                                                ) and 'DefaultValueType' in
__DefaultSetTuple[1
                                        ] and __DefaultSetTuple[1
                                        ]['DefaultValueType']==property),
PropertizedClass.DefaultAttributeVariablesOrderedDict.items()
                        )

                        #debug
                        '''
                        print('Before set
PropertizedClass.PropertizedDefaultTuplesList is
',PropertizedClass.PropertizedDefaultTuplesList)
                        print('')
                        '''

                        #set at the level of the class the
PropertizingGetStr+KeyStr
                        map(
                                        lambda __PropertizedDefaultTuple:
                                        setattr(
PropertizedClass,
PropertizingGetStr+__PropertizedDefaultTuple[0],
getPropertizedVariableWithItemTuple(__PropertizedDefaultTuple)
                                                        ),
PropertizedClass.PropertizedDefaultTuplesList
                                )

                        #set the PropertizedTuple for each at the level of the
class
                        PropertizedClass.PropertizedDefaultTuplesList=map(
                                        lambda __PropertizedDefaultTuple:
getPropertizedTupleWithItemTupleAndClass(
                                                __PropertizedDefaultTuple,
                                                PropertizedClass
                                        ),
PropertizedClass.PropertizedDefaultTuplesList
                                )

                        #debug
                        '''
                        print('After set
PropertizedClass.PropertizedDefaultTuplesList is
',PropertizedClass.PropertizedDefaultTuplesList)
                        print('')
                        '''

                        #Reset at the level of the class the properties
                        map(
                                        lambda __PropertizedDefaultTuple:
                                        setattr(
PropertizedClass,
*__PropertizedDefaultTuple
                                                        ),
PropertizedClass.PropertizedDefaultTuplesList
                                )



                        #Add to the KeyStrsList
                        PropertizedClass.KeyStrsList+=[
"PropertizedDefaultTuplesList"
                                                                        ]




#</Define_Class>




```

<small>
View the Propertiser sources on <a href="https://github.com/Ledoux/ShareYourSyst
em/tree/master/Pythonlogy/ShareYourSystem/Classors/Propertiser"
target="_blank">Github</a>
</small>




<!---
FrozenIsBool True
-->

##Example

Going back to the Doer cell when we invented a very minimalist Maker.
We now define its MakingMyFloat as a property that can be then defined as
a "binding" attribute thanks to the setMakingMyFloat method definition,
that will be linked to the fset attribute of the property object.

```python
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Standards.Classors import Propertiser,Attester
from ShareYourSystem.Standards.Objects import Initiator

#Definition a MakerClass decorated by the PropertiserClass
@Propertiser.PropertiserClass()
class MakerClass(Initiator.InitiatorClass):

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
        pass

    #Definition a binding function
    def setMakingMyFloat(self,_SettingValueVariable):

        #Print
        #print('I am going to make the job directly !')

        #set the value of the "hidden" property variable
        self._MakingMyFloat=_SettingValueVariable

        #Bind with MadeInt setting
        self.MadeMyInt=int(self._MakingMyFloat)

    #Definition a binding function
    def setMakingMyList(self,_SettingValueVariable):

        #set the value of the "hidden" property variable
        self._MakingMyList=_SettingValueVariable+['Hellllllo']


#Definition a default instance
DefaultMaker=MakerClass()

#Definition a special instance
SpecialMaker=MakerClass(_MakingMyFloat=5,_MakingMyList=[4])

#Definition the AttestedStr
SYS._attest(
    [
        'MakerClass.PropertizedDefaultTuplesList is '+SYS._str(
            MakerClass.PropertizedDefaultTuplesList),
        'What are you saying DefaultMaker ?',
        'DefaultMaker.__dict__ is '+str(DefaultMaker.__dict__),
        'DefaultMaker.MakingMyFloat is '+str(DefaultMaker.MakingMyFloat),
        'DefaultMaker.MakingMyList is '+str(DefaultMaker.MakingMyList),
        'DefaultMaker.MadeMyInt is '+str(DefaultMaker.MadeMyInt),
        'What are you saying SpecialMaker ?',
        'SpecialMaker.__dict__ is '+str(SpecialMaker.__dict__),
        'SpecialMaker.MakingMyFloat is '+str(SpecialMaker.MakingMyFloat),
        'SpecialMaker.MakingMyList is '+str(SpecialMaker.MakingMyList),
        'SpecialMaker.MadeMyInt is '+str(SpecialMaker.MadeMyInt),
    ]
)

#Print


```


```console
>>>


*****Start of the Attest *****

MakerClass.PropertizedDefaultTuplesList is
   /[
   /  0 :
   /   /(
   /   /  0 : MakingMyFloat
   /   /  1 : <property object at 0x10e7fb628>
   /   /)
   /  1 :
   /   /(
   /   /  0 : MakingMyList
   /   /  1 : <property object at 0x10e7fbd60>
   /   /)
   /]

------

What are you saying DefaultMaker ?

------

DefaultMaker.__dict__ is {'IdInt': 4537523408}

------

DefaultMaker.MakingMyFloat is 3.0

------

DefaultMaker.MakingMyList is []

------

DefaultMaker.MadeMyInt is 0

------

What are you saying SpecialMaker ?

------

SpecialMaker.__dict__ is {'IdInt': 4537523600, 'MadeMyInt': 5, '_MakingMyFloat':
5, '_MakingMyList': [4, 'Hellllllo']}

------

SpecialMaker.MakingMyFloat is 5

------

SpecialMaker.MakingMyList is [4, 'Hellllllo']

------

SpecialMaker.MadeMyInt is 5

*****End of the Attest *****



```

