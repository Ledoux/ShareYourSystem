

<!--
FrozenIsBool False
-->

#Attributer

##Doc
----


> An Attributer instance has a __setitem__ method for setting things in the
<InstanceVariable>.__dict__
> This is helpful for setting Propertized mutable variables in the instance
different
> from the propertized value setted at the level of the class
>
>

----

<small>
View the Attributer notebook on [NbViewer](http://nbviewer.ipython.org/url/share
yoursystem.ouvaton.org/Attributer.ipynb)
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

An Attributer instance has a __setitem__ method for setting things in the
<InstanceVariable>.__dict__
This is helpful for setting Propertized mutable variables in the instance
different
from the propertized value setted at the level of the class

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Deleter"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineLocals>
AttributingStartStr='Attr_'
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class AttributerClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'AttributingKeyStr',
'AttributingValueVariable',
'AttributedSetKeyStr'
                                                                ]

        def default_init(self,
                                                _AttributingKeyStr="",
                                                _AttributingValueVariable=None,
                                                _AttributedSetKeyStr="",
                                                **_KwargVariablesDict
                                        ):
                """ """

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)


        def do_attribute(self):

                #set
                self.AttributedSetKeyStr=AttributingStartStr.join(
                        self.AttributingKeyStr.split(AttributingStartStr)[1:])

                #Call the __setattr__ method
self.__setattr__(self.AttributedSetKeyStr,self.AttributingValueVariable)

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
                if self.SettingKeyVariable.startswith(AttributingStartStr):

                        #debug
                        '''
                        self.debug('We are going to share')
                        '''

                        #Path
self.attribute(self.SettingKeyVariable,self.SettingValueVariable)

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

                        #debug
                        '''
                        self.debug(
                                                [
                                                        'BaseClass is
'+str(BaseClass),
                                                        'BaseClass.set is
'+str(BaseClass.set)
                                                ]
                                )
                        '''

                        #Set and return
                        return BaseClass.set(self)

                else:

                        #return
                        return OutputDict

#</DefineClass>

```

<small>
View the Attributer sources on <a href="https://github.com/Ledoux/ShareYourSyste
m/tree/master/Pythonlogy/ShareYourSystem/Itemizers/Attributer"
target="_blank">Github</a>
</small>



```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Standards.Itemizers import Attributer

#Definition a Attributer and set with the __setitem__
MyAttributer=Attributer.AttributerClass().__setitem__('Attr_MyInt',0)

#Definition the AttestedStr
SYS._attest(
    [
    'MyAttributer is '+SYS._str(
            MyAttributer,
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

MyAttributer is < (AttributerClass), 4554376528>
   /{
   /  '<New><Instance>IdInt' : 4554376528
   /  '<New><Instance>MyInt' : 0
   /  '<Spe><Instance>AttributedSetKeyStr' : MyInt
   /  '<Spe><Instance>AttributingKeyStr' : Attr_MyInt
   /  '<Spe><Instance>AttributingValueVariable' : 0
   /}

*****End of the Attest *****



```

