

<!--
FrozenIsBool False
-->

#Documenter

----------------------- ------------------------------------



@Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



The Installer directs a readme call in a ShareYourSystem directory.



----------------------------------------------------------------


View the Documenter sources on [Github](https://github.com/Ledoux/ShareYourSyste
m/tree/master/ShareYourSystem.Guiders.Informer)




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

from ShareYourSystem.Guiders import Documenter

#Definition a Documenter instance
MyDocumenter=Documenter.DocumenterClass().document(
    map(
            lambda __BaseClass:
            __BaseClass.__module__.replace('.','/'),
            SYS.reverse(SYS.FilerClass.__mro__)[1:]
        )
    #_AllBool=True
)

#Definition the AttestedStr
SYS._attest(
    [
        'MyDocumenter is '+SYS._str(
        MyDocumenter,
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
Doer l.132 : DoerStr is Documenter
DoStr is Document
DoMethodStr is document
DoingStr is Documenting
DoneStr is Documented



*****Start of the Attest *****

MyDocumenter is < (DocumenterClass), 4558748560>
   /{
   /  '<New><Instance>DocumentedMkdocsDict' :
   /   /{
   /   /  'pages' :
   /   /   /[
   /   /   /  0 : ['index.md', 'Home']
   /   /   /  1 : ['Introduction.md', 'Introduction']
   /   /   /  2 : ['About/Manifest.md', 'About', 'Manifest']
   /   /   /  3 : ['About/StateArt.md', 'About', 'State of the art']
   /   /   /  4 : ['About/FAQs.md', 'About', 'FAQs']
   /   /   /  5 : ['GettingStarted/Install.md', 'GettingStarted', 'Install
ShareYourSystem']
   /   /   /  6 : ['GettingStarted/FirstToyObject.md', 'GettingStarted', 'Build
a first hierarching Python object']
   /   /   /  7 : ['GettingStarted/UseMeteorApi.md', 'GettingStarted', 'Use the
Meteror API']
   /   /   /  8 : ['GettingStarted/VisitLibrary.md', 'GettingStarted', 'Visit
the Library of specialized Modules']
   /   /   /  9 : ['CookBook/Classors.md', 'CookBook', 'Classors']
   /   /   /  10 : ['CookBook/Functers.md', 'CookBook', 'Functers']
   /   /   /  11 : ['CookBook/Objects.md', 'CookBook', 'Objects']
   /   /   /  12 : ['CookBook/TestAndShare.md', 'CookBook', 'Debug Attest Test
Notebook Document Github framework in SYS']
   /   /   /  13 : ['LibraryReference/Object.md', 'Library Reference', 'Object']
   /   /   /  14 : ['LibraryReference/Initiator.md', 'Library Reference',
'Initiator']
   /   /   /  15 : ['LibraryReference/Printer.md', 'Library Reference',
'Printer']
   /   /   /  16 : ['LibraryReference/Debugger.md', 'Library Reference',
'Debugger']
   /   /   /  17 : ['LibraryReference/Moduler.md', 'Library Reference',
'Moduler']
   /   /   /  18 : ['LibraryReference/Conditioner.md', 'Library Reference',
'Conditioner']
   /   /   /  19 : ['LibraryReference/Concluder.md', 'Library Reference',
'Concluder']
   /   /   /  20 : ['LibraryReference/Rebooter.md', 'Library Reference',
'Rebooter']
   /   /   /  21 : ['LibraryReference/Interfacer.md', 'Library Reference',
'Interfacer']
   /   /   /  22 : ['LibraryReference/Folderer.md', 'Library Reference',
'Folderer']
   /   /   /  23 : ['LibraryReference/Filer.md', 'Library Reference', 'Filer']
   /   /   /  24 : ['LibraryReference/Object.md', 'Library Reference', 'Object']
   /   /   /  25 : ['LibraryReference/Initiator.md', 'Library Reference',
'Initiator']
   /   /   /  26 : ['LibraryReference/Printer.md', 'Library Reference',
'Printer']
   /   /   /  27 : ['LibraryReference/Debugger.md', 'Library Reference',
'Debugger']
   /   /   /  28 : ['LibraryReference/Packager.md', 'Library Reference',
'Packager']
   /   /   /  29 : ['LibraryReference/Conditioner.md', 'Library Reference',
'Conditioner']
   /   /   /  30 : ['LibraryReference/Concluder.md', 'Library Reference',
'Concluder']
   /   /   /  31 : ['LibraryReference/Rebooter.md', 'Library Reference',
'Rebooter']
   /   /   /  32 : ['LibraryReference/Interfacer.md', 'Library Reference',
'Interfacer']
   /   /   /  33 : ['LibraryReference/Folderer.md', 'Library Reference',
'Folderer']
   /   /   /  34 : ['LibraryReference/Filer.md', 'Library Reference', 'Filer']
   /   /   /  35 : ['LibraryReference/Object.md', 'Library Reference', 'Object']
   /   /   /  36 : ['LibraryReference/Initiator.md', 'Library Reference',
'Initiator']
   /   /   /  37 : ['LibraryReference/Printer.md', 'Library Reference',
'Printer']
   /   /   /  38 : ['LibraryReference/Debugger.md', 'Library Reference',
'Debugger']
   /   /   /  39 : ['LibraryReference/Packager.md', 'Library Reference',
'Packager']
   /   /   /  40 : ['LibraryReference/Conditioner.md', 'Library Reference',
'Conditioner']
   /   /   /  41 : ['LibraryReference/Concluder.md', 'Library Reference',
'Concluder']
   /   /   /  42 : ['LibraryReference/Rebooter.md', 'Library Reference',
'Rebooter']
   /   /   /  43 : ['LibraryReference/Interfacer.md', 'Library Reference',
'Interfacer']
   /   /   /  44 : ['LibraryReference/Folderer.md', 'Library Reference',
'Folderer']
   /   /   /  45 : ['LibraryReference/Filer.md', 'Library Reference', 'Filer']
   /   /   /  46 : ['LibraryReference/Object.md', 'Library Reference', 'Object']
   /   /   /  47 : ['LibraryReference/Initiator.md', 'Library Reference',
'Initiator']
   /   /   /  48 : ['LibraryReference/Printer.md', 'Library Reference',
'Printer']
   /   /   /  49 : ['LibraryReference/Debugger.md', 'Library Reference',
'Debugger']
   /   /   /  50 : ['LibraryReference/Packager.md', 'Library Reference',
'Packager']
   /   /   /  51 : ['LibraryReference/Conditioner.md', 'Library Reference',
'Conditioner']
   /   /   /  52 : ['LibraryReference/Concluder.md', 'Library Reference',
'Concluder']
   /   /   /  53 : ['LibraryReference/Rebooter.md', 'Library Reference',
'Rebooter']
   /   /   /  54 : ['LibraryReference/Interfacer.md', 'Library Reference',
'Interfacer']
   /   /   /  55 : ['LibraryReference/Folderer.md', 'Library Reference',
'Folderer']
   /   /   /  56 : ['LibraryReference/Filer.md', 'Library Reference', 'Filer']
   /   /   /  57 : ['LibraryReference/Object.md', 'Library Reference', 'Object']
   /   /   /  58 : ['LibraryReference/Initiator.md', 'Library Reference',
'Initiator']
   /   /   /  59 : ['LibraryReference/Printer.md', 'Library Reference',
'Printer']
   /   /   /  60 : ['LibraryReference/Debugger.md', 'Library Reference',
'Debugger']
   /   /   /  61 : ['LibraryReference/Packager.md', 'Library Reference',
'Packager']
   /   /   /  62 : ['LibraryReference/Conditioner.md', 'Library Reference',
'Conditioner']
   /   /   /  63 : ['LibraryReference/Concluder.md', 'Library Reference',
'Concluder']
   /   /   /  64 : ['LibraryReference/Rebooter.md', 'Library Reference',
'Rebooter']
   /   /   /  65 : ['LibraryReference/Interfacer.md', 'Library Reference',
'Interfacer']
   /   /   /  66 : ['LibraryReference/Folderer.md', 'Library Reference',
'Folderer']
   /   /   /  67 : ['LibraryReference/Filer.md', 'Library Reference', 'Filer']
   /   /   /  68 : ['LibraryReference/Object.md', 'Library Reference', 'Object']
   /   /   /  69 : ['LibraryReference/Initiator.md', 'Library Reference',
'Initiator']
   /   /   /  70 : ['LibraryReference/Printer.md', 'Library Reference',
'Printer']
   /   /   /  71 : ['LibraryReference/Debugger.md', 'Library Reference',
'Debugger']
   /   /   /  72 : ['LibraryReference/Packager.md', 'Library Reference',
'Packager']
   /   /   /  73 : ['LibraryReference/Conditioner.md', 'Library Reference',
'Conditioner']
   /   /   /  74 : ['LibraryReference/Concluder.md', 'Library Reference',
'Concluder']
   /   /   /  75 : ['LibraryReference/Rebooter.md', 'Library Reference',
'Rebooter']
   /   /   /  76 : ['LibraryReference/Interfacer.md', 'Library Reference',
'Interfacer']
   /   /   /  77 : ['LibraryReference/Folderer.md', 'Library Reference',
'Folderer']
   /   /   /  78 : ['LibraryReference/Filer.md', 'Library Reference', 'Filer']
   /   /   /]
   /   /  'site_name' : ShareYourSystem
   /   /  'theme' : readthedocs
   /   /}
   /  '<New><Instance>DocumentedModulePathStrsList' :
['ShareYourSystem/Objects/Object', 'ShareYourSystem/Objects/Initiator',
'ShareYourSystem/Objects/Printer', 'ShareYourSystem/Objects/Debugger',
'ShareYourSystem/Objects/Packager', 'ShareYourSystem/Objects/Conditioner',
'ShareYourSystem/Objects/Concluder', 'ShareYourSystem/Objects/Rebooter',
'ShareYourSystem/Interfacers/Interfacer',
'ShareYourSystem/Interfacers/Folderer', 'ShareYourSystem/Interfacers/Filer']
   /  '<New><Instance>DocumentedNameStrsList' : ['Object', 'Initiator',
'Printer', 'Debugger', 'Packager', 'Conditioner', 'Concluder', 'Rebooter',
'Interfacer', 'Folderer', 'Filer']
   /  '<New><Instance>IdStr' : 4558748560
   /  '<Spe><Class>DocumentingAllBool' : False
   /  '<Spe><Instance>DocumentingModuleStrsList' :
['ShareYourSystem/Objects/Object', 'ShareYourSystem/Objects/Initiator',
'ShareYourSystem/Objects/Printer', 'ShareYourSystem/Objects/Debugger',
'ShareYourSystem/Objects/Packager', 'ShareYourSystem/Objects/Conditioner',
'ShareYourSystem/Objects/Concluder', 'ShareYourSystem/Objects/Rebooter',
'ShareYourSystem/Interfacers/Interfacer',
'ShareYourSystem/Interfacers/Folderer', 'ShareYourSystem/Interfacers/Filer']
   /}

*****End of the Attest *****



```

