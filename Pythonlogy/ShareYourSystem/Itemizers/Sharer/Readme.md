

<!--
FrozenIsBool False
-->

#Sharer

##Doc
----


>
> A Sharer can set attributes at the level of the class
>
>

----

<small>
View the Sharer notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyour
system.ouvaton.org/Sharer.ipynb)
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


A Sharer can set attributes at the level of the class

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Itemizers.Grasper"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Itemizers import Pather
#</ImportSpecificModules>

#<DefineLocals>
SharingStartStr="__class__."
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class SharerClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'SharingKeyStr',
'SharingValueVariable',
'SharedSetKeyStr',
'SharedClassDict'
                                                                ]

        def default_init(self,
                                _SharingKeyStr="",
                                _SharingValueVariable=None,
                                _SharedSetKeyStr="" ,
                                _SharedClassDict=None,
                                **_KwargVariablesDict
                                ):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_share(self):

                #set
                self.SharedSetKeyStr=SharingStartStr.join(self.SharingKeyStr.spl
it(SharingStartStr)[1:])

                #set at the level of the class
setattr(self.__class__,self.SharedSetKeyStr,self.SharingValueVariable)

                #debug
                '''
                self.debug(
                                        ('self.',self,[
'SharedSetKeyStr',
                                                                ])
                                )
                '''

#<Hook>@Hooker.HookerClass(**{'HookingAfterVariablesList':[BaseClass.get]})
        #@Imitater.ImitaterClass()
        def mimic_get(self):

                #debug
                '''
                self.debug(('self.',self,['GettingKeyVariable']))
                '''

                #Deep get
                if self.GettingKeyVariable=='__class__':

                        #set
                        self.GettedValueVariable=self.__class__

                        #Return
                        return {'HookingIsBool':False}

                elif self.GettingKeyVariable.startswith(SharingStartStr):

                        #Define
                        SharedGetString=SharingStartStr.join(
self.GettingKeyVariable.split(SharingStartStr)[1:]
                                )

                        #debug
                        '''
                        self.debug('SharedGetString is '+SharedGetString)
                        '''

                        #Define
                        self.SharedClassDict=dict(
                                        map(
                                                lambda __KeyString:
                                                (
                                                        __KeyString,
                                                        getattr(
                                                                self.__class__,
                                                                __KeyString
                                                        )
                                                ),
                                                dir(self.__class__)
                                        )+[('__mro__',self.__class__.__mro__)]
                                )

                        #debug
                        '''
                        self.debug(('self.',self,['SharedClassDict']))
                        '''

                        #get in the __class__
self.GettedValueVariable=Pather.getVariableWithDictatedVariableAndKeyVariable(
                                self.SharedClassDict,
                                SharedGetString
                        )

                        #Return
                        return {'HookingIsBool':False}


                else:

                        #debug
                        '''
                        self.debug('BaseClass.get is '+str(BaseClass.get))
                        '''

                        #Get before with the parent method
                        OutputDict=BaseClass.get(self)

                        #Check that we have still to hook
                        if OutputDict==None or OutputDict["HookingIsBool"]:

                                #Check
                                if self.GettingKeyVariable in
self.__class__.__dict__:

                                        #Get from the class
self.GettedValueVariable=self.__class__.__dict__[self.GettingKeyVariable]

                                        #Return
                                        return {'HookingIsBool':False}

                        #Return
                        return {'HookingIsBool':True}

#<Hook>@Hooker.HookerClass(**{'HookingAfterVariablesList':[BaseClass.set]})
        #@Imitater.ImitaterClass()
        def mimic_set(self):
                """ """

                #debug
                '''
self.debug(('self.',self,['SettingKeyVariable','SettingValueVariable']))
                '''

                #Definition
                OutputDict={'HookingIsBool':True}

                #Deep set
                if self.SettingKeyVariable.startswith(SharingStartStr):

                        #debug
                        '''
                        self.debug('We are going to share')
                        '''

                        #Path
self.share(self.SettingKeyVariable,self.SettingValueVariable)

                        #debug
                        '''
                        self.debug(('self.',self,[
"SharedKeyStr",
"SharedChildKeyStr",
"SharedValueVariable"
                                                                        ]
                                                                ))
                        '''

                        #Stop the setting
                        OutputDict["HookingIsBool"]=False
                        #<Hook>return OutputDict

                #Call the parent get method
                if OutputDict['HookingIsBool']:
                        BaseClass.set(self)


#</DefineClass>


```

<small>
View the Sharer sources on <a href="https://github.com/Ledoux/ShareYourSystem/tr
ee/master/Pythonlogy/ShareYourSystem/Itemizers/Sharer"
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
from ShareYourSystem.Itemizers import Sharer

#Explicit expression
MySharer=Sharer.SharerClass().__setitem__(
    '__class__.MyStr',
    'I am setted at the level of the class'
)

#Return
SYS._attest(
    [

        'MySharer is '+SYS._str(
                MySharer,
                **{
                'RepresentingBaseKeyStrsListBool':False
                }
            ),
        'MySharer.__class__.MyStr is '+MySharer.__class__.MyStr,
        'MySharer["__class__.MyStr"] is '+MySharer['__class__.MyStr'],
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

MySharer is < (SharerClass), 4554554512>
   /{
   /  '<New><Class>MyStr' : I am setted at the level of the class
   /  '<New><Instance>IdInt' : 4554554512
   /  '<Spe><Instance>SharedClassDict' :
   /   /{
   /   /}
   /  '<Spe><Instance>SharedSetKeyStr' : MyStr
   /  '<Spe><Instance>SharingKeyStr' : __class__.MyStr
   /  '<Spe><Instance>SharingValueVariable' : I am setted at the level of the
class
   /}

------

MySharer.__class__.MyStr is I am setted at the level of the class

------

MySharer["__class__.MyStr"] is I am setted at the level of the class

*****End of the Attest *****



```

