

<!--
FrozenIsBool False
-->

#Deriver

##Doc
----


>
> The Deriver helps for building a base-derive relationships between the
classes.
> Once a <Class> with based classes is defined, a decorating DeriverClass
instance
> append to these corresponding BaseClasses the <Class> as a derived class.
>
>

----

<small>
View the Deriver notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyou
rsystem.ouvaton.org/Deriver.ipynb)
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


The Deriver helps for building a base-derive relationships between the classes.
Once a <Class> with based classes is defined, a decorating DeriverClass instance
append to these corresponding BaseClasses the <Class> as a derived class.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Classors.Doer"
DecorationModuleStr=BaseModuleStr
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import sys
#</ImportSpecificModules>

#<DefineFunctions>
def getIsDerivedBoolWithParentClassAndDeriveClass(_ParentClass,_DeriveClass):

        #Debug
        '''
        print('Deriver l.37')
        print('_ParentClass is ',_ParentClass)
        print('_DeriveClass is ',_DeriveClass)
        print('')
        '''

        #Return
        return _DeriveClass in _ParentClass.__mro__
#</DefineFunctions>

#<DefineClass>
@DecorationClass()
class DeriverClass(BaseClass):

        def default_init(self,
                                                _DerivedModule=None,
                                                **_KwargVariablesDict
                                        ):


                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def __call__(self,_Class):

                #debug
                '''
                print('Deriver l.30 __call__ method')
                print('_Class is ',_Class)
                print('')
                '''

                #Call the parent __call__ method
                BaseClass.__call__(self,_Class)

                #Debug
                '''
                print('Deriver l.54 We are going to derive')
                print('self.derive is ',self.derive)
                print('')
                '''

                #Derive
                self.derive()

                #Debug
                '''
                print('derive is done')
                print('')
                '''

                #Return
                return _Class

        def do_derive(self):

                #Debug
                '''
                print('self.DoClass is ',self.DoClass)
                print('')
                '''

                #alias
                DoClass=self.DoClass

                #Link
                self.DerivedModule=sys.modules[DoClass.__module__]

                #set
                if len(DoClass.__bases__)>0:

                        #set the DerivedBaseClas
                        DerivedBaseClass=DoClass.__bases__[0]

                        #Debug
                        '''
                        print('l. 83 Deriver')
                        print('We can set derived bases for the parent')
                        print('DerivedBaseClass is ',DerivedBaseClass)
                        print('')
                        '''

                        #Append to the parent class
                        if hasattr(DerivedBaseClass,'DerivedClassesList'):
DerivedBaseClass.DerivedClassesList.append(DoClass)
                        else:
                                DerivedBaseClass.DerivedClassesList=[DoClass]

                        #Add to the KeyStrsList
DoClass.KeyStrsList+=SYS.getKeyStrsListWithClass(DoClass)

#</DefineClass>

```

<small>
View the Deriver sources on <a href="https://github.com/Ledoux/ShareYourSystem/t
ree/master/Pythonlogy/ShareYourSystem/Classors/Deriver"
target="_blank">Github</a>
</small>




<!--
FrozenIsBool False
-->

##More Descriptions at the level of the class

Special attributes of the ClassorsClass are :


```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Doer,Deriver,Attester
from ShareYourSystem.Objects import Initiator

#Definition of a MakerClass decorated by a DoerClass instance
@Doer.DoerClass()
class MakerClass(Initiator.InitiatorClass):
    pass

#Definition of a derived BuilderClass decorated by a Deriver
@Deriver.DeriverClass()
class BuilderClass(MakerClass):
    pass

#Print
#print('MakerClass.DerivedClassesList is '+str(MakerClass.DerivedClassesList))

#Definition the AttestedStr
SYS._attest(
    [
        'MakerClass.DerivedClassesList is '+str(MakerClass.DerivedClassesList)
    ]
)

#Print


```


```console
>>>


*****Start of the Attest *****

MakerClass.DerivedClassesList is [<class
'ShareYourSystem.Objects.Printer.PrinterClass'>, <class
'ShareYourSystem.Objects.Debugger.DebuggerClass'>, <class
'ShareYourSystem.Objects.Conditioner.ConditionerClass'>, <class
'ShareYourSystem.Objects.Concluder.ConcluderClass'>, <class
'ShareYourSystem.Objects.Rebooter.RebooterClass'>, <class
'ShareYourSystem.Interfacers.Interfacer.InterfacerClass'>, <class
'ShareYourSystem.Interfacers.Folderer.FoldererClass'>, <class
'ShareYourSystem.Objects.Packager.PackagerClass'>, <class
'ShareYourSystem.Interfacers.Filer.FilerClass'>, <class
'ShareYourSystem.Interfacers.Closer.CloserClass'>, <class
'ShareYourSystem.Interfacers.Loader.LoaderClass'>, <class
'ShareYourSystem.Interfacers.Writer.WriterClass'>, <class
'ShareYourSystem.Interfacers.Hdformater.HdformaterClass'>, <class
'ShareYourSystem.Interfacers.Capturer.CapturerClass'>, <class
'ShareYourSystem.Interfacers.Deployer.DeployerClass'>, <class
'ShareYourSystem.Guiders.Guider.GuiderClass'>, <class
'ShareYourSystem.Guiders.Scriptbooker.ScriptbookerClass'>, <class
'ShareYourSystem.Guiders.Celler.CellerClass'>, <class
'ShareYourSystem.Guiders.Notebooker.NotebookerClass'>, <class
'ShareYourSystem.Guiders.Nbconverter.NbconverterClass'>, <class
'ShareYourSystem.Guiders.Installer.InstallerClass'>, <class
'ShareYourSystem.Guiders.Documenter.DocumenterClass'>, <class
'ShareYourSystem.Guiders.Informer.InformerClass'>, <class
'ShareYourSystem.Objects.Caller.CallerClass'>, <class
'ShareYourSystem.Objects.Cloner.ClonerClass'>, <class 'MakerClass'>, <class
'BuilderClass'>, <class 'MakerClass'>, <class 'BuilderClass'>, <class
'BuilderClass'>]

*****End of the Attest *****



```

