

<!--
FrozenIsBool False
-->

#Mimicker

##Doc
----


>
> Mimicker...
>
>

----

<small>
View the Mimicker notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyo
ursystem.ouvaton.org/Mimicker.ipynb)
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


Mimicker...

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Classors.Switcher"
DecorationModuleStr="ShareYourSystem.Classors.Tester"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Classors import Doer
import six
#</ImportSpecificModules>

#<DefineLocals>
MimickingWrapPrefixStr="mimic_"
MimickingDecorationPrefixStr=""
MimickingDecorationTagStr="superMimic"
MimickingDecorationSuffixStr="_"
#</DefineLocals>

#<DefineFunctions>
def mimic(_InstanceVariable,*_LiargVariablesList,**_KwargVariablesDict):

        #Set
        MimicMethodStr=_KwargVariablesDict['MimicMethodStr']
        MimicClassStr=_KwargVariablesDict['MimicClassStr']
        MimicClass=getattr(SYS,MimicClassStr)
        MimicUnBoundMethod=getattr(
                MimicClass,
                MimicMethodStr
        )
        BaseClassStr=_KwargVariablesDict['BaseClassStr']
        BaseClass=getattr(SYS,BaseClassStr)
        del _KwargVariablesDict['MimicMethodStr']
        del _KwargVariablesDict['MimicClassStr']
        del _KwargVariablesDict['BaseClassStr']

        #Debug
        '''
        print('Mimicker l.48 inside of the function mimic')
        #print('_InstanceVariable is ',_InstanceVariable)
        print('_LiargVariablesList is ',_LiargVariablesList)
        print('_KwargVariablesDict is ',_KwargVariablesDict)
        print('')
        '''

        if len(_KwargVariablesDict)>0:

                #group by
                [
                        MimicTempAttributeItemTuplesList,
                        MimicTempNotAttributeItemTuplesList
                ]=SYS.groupby(
                        lambda __KwargItemTuple:
                        hasattr(_InstanceVariable,__KwargItemTuple[0]),
                        _KwargVariablesDict.items()
                )

                #Debug
                '''
                print('MimicTempAttributeItemTuplesList is
',MimicTempAttributeItemTuplesList)
                print('MimicTempNotItemTuplesList is
',MimicTempNotItemTuplesList)
                print('')
                '''

                #set in the instance the corresponding kwarged arguments
                map(
                                lambda __MimicTempAttributeItemTuple:
                                #set direct explicit attributes
_InstanceVariable.__setattr__(*__MimicTempAttributeItemTuple),
                                MimicTempAttributeItemTuplesList
                        )

                #Define
                MimicKwargDict=dict(MimicTempNotAttributeItemTuplesList)

        else:

                #Define
                MimicKwargDict={}

        #Init
        MimicOutputVariable=None

        #Debug
        '''
        print('Mimicker l.96 inside of the function mimic')
        print('MimicClass is ',MimicClass)
        print('MimicMethodStr is ',MimicMethodStr)
        print('MimicUnBoundMethod is ',MimicUnBoundMethod)
        print('')
        '''

        #call the Mimicked function
        if len(MimicKwargDict)>0:
                MimicOutputVariable=MimicUnBoundMethod(
                                                        _InstanceVariable,
                                                        *_LiargVariablesList,
                                                        **MimicKwargDict
                                                )
        else:
                MimicOutputVariable=MimicUnBoundMethod(
                                _InstanceVariable,
                                *_LiargVariablesList
                        )

        #Debug
        '''
        print('Mimicker l.117 inside of the function mimic')
        print('MimicOutputVariable is ',MimicOutputVariable)
        print('')
        '''

        #Check
        if BaseClass.DoingGetBool==False:

                #Return
                return _InstanceVariable

        else:

                #Return the
                return MimicOutputVariable
#</DefineFunctions>

#<DefineClass>
@DecorationClass()
class MimickerClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
                                        'MimickingDoMethodStr',
                                        'MimickedWrapMethodStr'
        ]

        def default_init(self,
                                        _MimickingDoMethodStr="",
                                        _MimickedWrapMethodStr="",
                                        **_KwargVariablesDict
                                ):

                #Call the init parent method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def __call__(self,_Class):

                #Call the parent init method
                BaseClass.__call__(self,_Class)

                #mimic
                self.mimic()

                #Return
                return _Class

        def do_mimic(self):

                #Debug
                '''
                print('l 174 Mimicker')
                print('self.MimickingDoMethodStr is ',self.MimickingDoMethodStr)
                print('')
                '''

                #Check
                if self.MimickingDoMethodStr!="":

                        #observ
                        self.observe(True,self.MimickingDoMethodStr)

                        #set
self.MimickedWrapMethodStr=MimickingWrapPrefixStr+self.MimickingDoMethodStr

                        #Debug
                        '''
                        print('l 75 Mimicker ')
                        print('self.MimickedWrapMethodStr is
',self.MimickedWrapMethodStr)
                        print('')
                        '''

                        #Define
MimickedDoStr=self.MimickingDoMethodStr[0].upper()+self.MimickingDoMethodStr[1:]
MimickedDoerStr=Doer.DoStrToDoerStrOrderedDict[MimickedDoStr]

                        #Debug
                        '''
                        print('l 84 Mimicker ')
                        print('MimickedDoStr is ',MimickedDoStr)
                        print('MimickedDoerStr is ',MimickedDoerStr)
                        print('MimickedBaseModule is ',MimickedBaseModule)
                        print('')
                        '''

                        #Definitions
                        MimickedBaseClass=getattr(
                                SYS,
                                SYS.getClassStrWithNameStr(MimickedDoerStr)
                        )

                        #get
                        MimickedDoExecStr=getattr(
                                MimickedBaseClass,
                                'Do'+MimickedBaseClass.NameStr+'ExecStr'
                        )

                        #debug
                        '''
                        print('l 206 Mimicker')
                        print('MimickedDoExecStr is ')
                        print(MimickedDoExecStr)
                        print('')
                        '''

                        #replace
                        MimickedDecorationMethodStr=MimickingDecorationPrefixStr
+MimickingDecorationTagStr+MimickingDecorationSuffixStr
                        MimickedDecorationMethodStr+=self.ObservedWrapMethodStr

                        #Debug
                        '''
                        print('l 232 Mimicker')
                        print('MimickedDecorationMethodStr is
'+MimickedDecorationMethodStr)
                        print('')
                        '''

                        #replace
                        MimickedExecStr='def
'+MimickedDecorationMethodStr+'('+'('.join(
                                MimickedDoExecStr.split('(')[1:]
                        )

                        #Debug
                        '''
                        print('l 208 Mimicker')
                        print('MimickedExecStr is ')
                        print(MimickedExecStr)
                        print('')
                        '''

                        #Add to the ImitatedDoneExecStr
                        MimickedExecStr+='\n\treturn
mimic(_InstanceVariable,*_LiargVariablesList,'
                        MimickedExecStr+='**dict({\'MimicMethodStr\':\''+self.Mi
mickedWrapMethodStr+'\','
MimickedExecStr+='\'MimicClassStr\':\''+self.DoClass.__name__+'\','
MimickedExecStr+='\'BaseClassStr\':\''+MimickedBaseClass.__name__+'\''
                        MimickedExecStr+='},**_KwargVariablesDict))'

                        #Debug
                        '''
                        print('l 223 Mimicker')
                        print('MimickedExecStr is ')
                        print(MimickedExecStr)
                        print('')
                        '''

                        #exec
                        six.exec_(MimickedExecStr)

                        #set
self.MimickedDecorationUnboundMethod=locals()[MimickedDecorationMethodStr]

                        #set in the __class__
                        setattr(
                                                self.DoClass,
                                                MimickedDecorationMethodStr,
self.MimickedDecorationUnboundMethod
                                        )

                        #make the amalgam
                        setattr(
                                                self.DoClass,
                                                self.MimickingDoMethodStr,
self.MimickedDecorationUnboundMethod
                                        )

                        #Return self
                        #return self

#</DefineClass>


```

<small>
View the Mimicker sources on <a href="https://github.com/Ledoux/ShareYourSystem/
tree/master/Pythonlogy/ShareYourSystem/Classors/Mimicker"
target="_blank">Github</a>
</small>




<!---
FrozenIsBool True
-->

##Example

It is possible to cumulate mimick and switch properties...
Note that only the do_make is a switched method as the
mimic_make continue to work after the first call of make.

```python
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Switcher,Mimicker
from ShareYourSystem.Objects import Initiator

#Definition a MakerClass with decorated make by a Switcher
@Switcher.SwitcherClass(**{
    'SwitchingIsBool':True,
    'SwitchingWrapMethodStr':'make'
})
class MakerClass(Initiator.InitiatorClass):

    #Definition
    RepresentingKeyStrsList=[
                                'MakingMyFloat',
                                'MadeMyInt'
                            ]

    def default_init(self,
                _MakingMyFloat=1.,
                _MadeMyInt=0
                ):
        Initiator.InitiatorClass.__init__(self)

    def do_make(self):

        #print
        print('self.MakingMyFloat is '+str(self.MakingMyFloat))
        print('self.MadeMyInt is '+str(self.MadeMyInt))
        print('')

        #Cast
        self.MadeMyInt=int(self.MakingMyFloat)

#Definition
@Mimicker.MimickerClass(**{
    'MimickingDoMethodStr':"make"
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
    'MadeMyInt']
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
print('Now we switch')
MyBuilder.setSwitch('Maker',['Make'])

#Print
print('After the switch MyBuilder is ')
SYS._print(MyBuilder,**{
    'RepresentingKeyStrsList':[
    'MakingMyFloat',
    'MadeMyInt'
    ]
})

#make again
MyBuilder.make(7.)

#Print
print('After the third make, MyBuilder is ')
SYS._print(MyBuilder,**{
    'RepresentingKeyStrsList':[
    'MakingMyFloat',
    'MadeMyInt',
    'WatchMakeWithMakerBool']
})

#Definition the AttestedStr
SYS._attest(
    [
        'BuilderClass.WatchMakeWithMakerBool is
'+str(BuilderClass.WatchMakeWithMakerBool),
        'BuilderClass.make is '+str(BuilderClass.make),
        'MyBuilder is '+SYS._str(
            MyBuilder,**{
            'RepresentingAlineaIsBool':False,
            'RepresentingKeyStrsList':[
            'MakingMyFloat',
            'MadeMyInt'
            ]
        }
        ),
    ]
)

#Print


```


```console
>>>
Before make, MyBuilder is
< (BuilderClass), 4538552080>
   /{
   /  '<Base><Class>MadeMyInt' : 0
   /  '<Base><Class>MakingMyFloat' : 1.0
   /  '<New><Instance>IdInt' : 4538552080
   /}
I am in the mimic_make of the Builder
self.MakingMyFloat is 3.0
self.MadeMyInt is 0

After the first make, MyBuilder is
< (BuilderClass), 4538552080>
   /{
   /  '<New><Instance>IdInt' : 4538552080
   /  '<Spe><Instance>MadeMyInt' : 13
   /  '<Spe><Instance>MakingMyFloat' : 3.0
   /}
I am in the mimic_make of the Builder
After the second make, MyBuilder is
< (BuilderClass), 4538552080>
   /{
   /  '<New><Instance>IdInt' : 4538552080
   /  '<Spe><Instance>MadeMyInt' : 23
   /  '<Spe><Instance>MakingMyFloat' : 5.0
   /}
Now we switch
After the switch MyBuilder is
< (BuilderClass), 4538552080>
   /{
   /  '<New><Instance>IdInt' : 4538552080
   /  '<Spe><Instance>MadeMyInt' : 23
   /  '<Spe><Instance>MakingMyFloat' : 5.0
   /}
I am in the mimic_make of the Builder
self.MakingMyFloat is 7.0
self.MadeMyInt is 23

After the third make, MyBuilder is
< (BuilderClass), 4538552080>
   /{
   /  '<New><Instance>IdInt' : 4538552080
   /  '<Spe><Instance>MadeMyInt' : 17
   /  '<Spe><Instance>MakingMyFloat' : 7.0
   /  '<Spe><Instance>WatchMakeWithMakerBool' : True
   /}


*****Start of the Attest *****

BuilderClass.WatchMakeWithMakerBool is False

------

BuilderClass.make is <unbound method
BuilderClass.superMimic_switch_watch_superDo_make>

------

MyBuilder is < (BuilderClass), 4538552080>
   /{
   /  '<New><Instance>IdInt' : 4538552080
   /  '<Spe><Instance>MadeMyInt' : 17
   /  '<Spe><Instance>MakingMyFloat' : 7.0
   /}

*****End of the Attest *****



```

