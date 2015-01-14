

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
'ShareYourSystem.Guiders.Informer.InformerClass'>, <class 'BuilderClass'>]

*****End of the Attest *****



```

