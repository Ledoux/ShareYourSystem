

<!--
FrozenIsBool False
-->

#Binder

##Doc
----


>
> Binder helps for setting a method in a Class,
> taking inspiration (like a decoration) from another one.
>
>
>

----

<small>
View the Binder notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyour
system.ouvaton.org/Binder.ipynb)
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


Binder helps for setting a method in a Class,
taking inspiration (like a decoration) from another one.


"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Classors.Observer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Tester"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
Observer=BaseModule
import six
#</ImportSpecificModules>

#<DefineLocals>
BindingDecorationPrefixStr=""
BindingDecorationSuffixStr="_"
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class BinderClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
                                                        'BindingIsBool',
'BindingDecorationUnboundMethod',
'BindingDecorationMethodStr',
'BindingDecorationTagStr',
                                                        'BindingItemTuplesList',
'BindedDecorationMethodStr',
'BindedDecorationUnboundMethod'
                                                ]

        def default_init(self,
                                        _BindingIsBool=False,
                                        _BindingDecorationUnboundMethod=None,
                                        _BindingDecorationMethodStr='',
                                        _BindingDecorationTagStr="",
                                        _BindingItemTuplesList=None,
                                        _BindedDecorationMethodStr="",
                                        _BindedDecorationUnboundMethod=None,
                                        **_KwargVariablesDict
                                ):

                #Call the init parent method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def __call__(self,_Class):

                #Call the parent method
                Observer.ObserverClass.__bases__[0].__call__(self,_Class)

                #bind
                self.bind()

                #Return
                return _Class

        def do_bind(self):

                #Check
                if self.BindingIsBool:

                        #Debug
                        '''
                        print('l 77 Binder')
                        print('self.BindingDecorationUnboundMethod is
',self.BindingDecorationUnboundMethod)
                        print('self.BindingDecorationMethodStr is
',self.BindingDecorationMethodStr)
                        print('')
                        '''

                        #Check
                        if self.BindingDecorationUnboundMethod!=None or
self.BindingDecorationMethodStr!="":

                                #Debug
                                '''
                                print('l 73 Binder')
                                print('we observe first')
                                print('')
                                '''

                                #observe without linking
                                self.observe(True)

                                #Debug
                                '''
                                print('l 81 Binder')
                                print('self.ObservingWrapMethodStr is
',self.ObservingWrapMethodStr)
                                print('self.ObservedWrapMethodStr is
',self.ObservedWrapMethodStr)
                                print('')
                                '''

                                #Check
                                if self.BindingDecorationUnboundMethod==None:

                                        #Get
self.BindingDecorationUnboundMethod=getattr(
                                                self.DoClass,
                                                self.BindingDecorationMethodStr
                                        )

                                else:

                                        #set
self.BindingDecorationMethodStr=self.BindingDecorationUnboundMethod.__name__

                                #Debug
                                '''
                                print('Binder l.119')
                                print('self.BindingDecorationUnboundMethod is')
                                print(self.BindingDecorationUnboundMethod)
                                print('')
                                '''

                                #Check
                                if self.BindingDecorationTagStr=="":
self.BindingDecorationTagStr=self.BindingDecorationMethodStr

                                #set the new
                                self.BindedDecorationMethodStr=BindingDecoration
PrefixStr+self.BindingDecorationTagStr+BindingDecorationSuffixStr
self.BindedDecorationMethodStr+=self.ObservingWrapMethodStr

                                #Debug
                                '''
                                print('Binder l.102')
                                print('self.BindedDecorationMethodStr is')
                                print(self.BindedDecorationMethodStr)
                                print('')
                                '''

                                #set to the class the BindingDecorationMethod
                                setattr(
                                                self.DoClass,
                                                self.BindingDecorationMethodStr,
self.BindingDecorationUnboundMethod
                                        )

                                #Define
                                BindedExecStr='def
'+self.BindedDecorationMethodStr+'(_InstanceVariable,*_LiargVariablesList'
                                BindedExecStr+=',**_KwargVariablesDict):'
                                BindedExecStr+='\n\treturn
_InstanceVariable.__class__.'+self.BindingDecorationMethodStr
BindedExecStr+='(_InstanceVariable,*_LiargVariablesList'

                                #Debug
                                '''
                                print('Binder l 159')
                                print('self.BindingItemTuplesList is ')
                                print(self.BindingItemTuplesList)
                                print('')
                                '''

                                #Add
                                self.BindingItemTuplesList+=[
('BindObserveWrapMethodStr',self.ObservingWrapMethodStr),
('BindDoClassStr',self.DoClass.__name__),
                                ]
                                self.BindedItemTuplesList=','.join(
                                        map(
                                                lambda __BindingItemTuple:
"'"+__BindingItemTuple[0]+"':'"+str(__BindingItemTuple[1])+"'",
                                                self.BindingItemTuplesList
                                        )
                                )
                                BindedExecStr+=',**dict({'
                                BindedExecStr+=self.BindedItemTuplesList
                                BindedExecStr+='},**_KwargVariablesDict))\n'

                                #Debug
                                '''
                                print('Binder l 176')
                                print('BindedExecStr is ')
                                print(BindedExecStr)
                                print('')
                                '''

                                #exec
                                six.exec_(BindedExecStr)

                                #set
self.BindedDecorationUnboundMethod=locals()[self.BindedDecorationMethodStr]

                                #set to the class the BindingDecorationMethod
                                setattr(
                                                self.DoClass,
                                                self.BindedDecorationMethodStr,
self.BindedDecorationUnboundMethod
                                        )

                                #Debug
                                '''
                                print('l 175 Binder')
                                print('self.BindedDecorationMethodStr is ')
                                print(self.BindedDecorationMethodStr)
                                print('self.BindedDecorationUnboundMethod is ')
                                print(self.BindedDecorationUnboundMethod)
                                print('')
                                '''

                                #Return self
                                #return self

#</DefineClass>


```

<small>
View the Binder sources on <a href="https://github.com/Ledoux/ShareYourSystem/tr
ee/master/Pythonlogy/ShareYourSystem/Classors/Binder" target="_blank">Github</a>
</small>




<!---
FrozenIsBool True
-->

##Example

Here this is to check that the class checks that
this is useless to watch a watch method, therefore it
just lets it as the first version.

```python
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Standards.Classors import Binder
from ShareYourSystem.Standards.Objects import Initiator
import operator

#Define a Unbound method like function
def foo(_InstanceVariable,*_LiargVariablesList,**_KwargVariablesDict):

    #print
    print('In the foo function ')
    print('_KwargVariablesDict is ')
    print(_KwargVariablesDict)
    print('')

    #get the wrapped method
    WrapUnboundMethod=getattr(
        getattr(
            SYS,
            _KwargVariablesDict['BindDoClassStr']
        ),
        _KwargVariablesDict['BindObserveWrapMethodStr']
    )

    #call
    WrapUnboundMethod(_InstanceVariable,10.*_InstanceVariable.MakingMyFloat)


#Definition a MakerClass decorated by the BinderClass
@Binder.BinderClass(**{
    'ObservingWrapMethodStr':'make',
    'BindingIsBool':True,
    'BindingDecorationUnboundMethod':foo,
    'BindingItemTuplesList':[('MyFooInt',1)]
})
class MakerClass(Initiator.InitiatorClass):

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
        pass

    def do_make(self):

        #Print
        print('I make')

        #cast
        self.MadeMyInt=int(self.MakingMyFloat)

#Definition and do a first make
MyMaker=MakerClass().make(3.)

#Use the other binded method that is completely fooooo
MyMaker.foo_make()

#Definition the AttestedStr
SYS._attest(
    [
        'MakerClass.foo is '+str(MakerClass.foo),
        'MakerClass.foo_make is '+str(MakerClass.foo_make),
        'MyMaker is '+SYS._str(
        MyMaker,
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
I make
In the foo function
_KwargVariablesDict is
{'MyFooInt': '1', 'BindDoClassStr': 'MakerClass', 'BindObserveWrapMethodStr':
'make'}

I make


*****Start of the Attest *****

MakerClass.foo is <unbound method MakerClass.foo>

------

MakerClass.foo_make is <unbound method MakerClass.foo_make>

------

MyMaker is < (MakerClass), 4539083472>
   /{
   /  '<New><Instance>IdInt' : 4539083472
   /  '<Spe><Instance>MadeMyInt' : 30
   /  '<Spe><Instance>MakingMyFloat' : 30.0
   /}

*****End of the Attest *****



```
