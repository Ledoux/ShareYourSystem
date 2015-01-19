

<!--
FrozenIsBool False
-->

#Installer

##Doc
----


>
> The Installer collects ModuleStrs to write
>
>

----

<small>
View the Installer notebook on [NbViewer](http://nbviewer.ipython.org/url/sharey
oursystem.ouvaton.org/Installer.ipynb)
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


The Installer collects ModuleStrs to write

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Guiders.Nbconverter"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import os
import copy
from ShareYourSystem.Interfacers import Loader,Writer
#</ImportSpecificModules>

#<DefineLocals>
InstallingSysFolderPathStr=SYS.PythonlogyLocalFolderPathStr
InstallingLibraryFolderPathStr=InstallingSysFolderPathStr+'/docs/LibraryReferenc
e/'
#</DefineLocals>

#<DefineClass>
@DecorationClass(**{
        'ClassingSwitchMethodStrsList':['install']
})
class InstallerClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'InstallingModuleStrsList',
'InstallingAllBool'
                                                                ]

        def default_init(self,
                                                _InstallingModuleStrsList=None,
                                                _InstallingAllBool=False,
                                                **_KwargVariablesDict
                                        ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)


        def do_install(self):

                #Definition
                self.load(
                        **{
                                'FolderingPathStr':InstallingSysFolderPathStr,
                                'FilingKeyStr':'setup.py'
                        }
                )

                #chunk to set the InstalledModuleStrsList
                InstalledPackageStr=SYS.chunk(
                        ['packages=[','],'],self.LoadedReadVariable
                )[0]
                InstalledTextStrsList=InstalledPackageStr.split('\n')
                InstalledTextStrListsList=SYS._filter(
                        lambda __InstalledChunkList:
                        len(__InstalledChunkList)>0,
                        map(
                                        lambda __InstalledTextStr:
                                        SYS.chunk(
                                                ["'ShareYourSystem","',"],
                                                __InstalledTextStr
                                        ),
                                        InstalledTextStrsList
                        )
                )

                self.InstallingModuleStrsList=map(
                        lambda __InstalledTextStrList:
                        ('ShareYourSystem'+__InstalledTextStrList[0])
                        if __InstalledTextStrList[0]!="'"
                        else 'ShareYourSystem',
                        InstalledTextStrListsList
                )

                #debug
                '''
                self.debug(('self.',self,['InstallingModuleStrsList']))
                '''

                #map
                self.InstalledModulePathStrsList=map(
                        lambda __InstallingModuleStr:
                        __InstallingModuleStr.replace('.','/'),
                        self.InstallingModuleStrsList
                )

                #debug
                '''
                self.debug(('self.',self,['InstalledModulePathStrsList']))
                '''

                #set with all the NameStrs
                self.InstalledNameStrsList=map(
                                        lambda __InstalledModulePathStr:
                                        __InstalledModulePathStr.split('/')[-1],
                                        self.InstalledModulePathStrsList
                        )

                #Return self
                #return self

#</DefineClass>

```

<small>
View the Installer sources on <a href="https://github.com/Ledoux/ShareYourSystem
/tree/master/Pythonlogy/ShareYourSystem/Guiders/Installer"
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
from ShareYourSystem.Guiders import Installer

#Definition a Installer instance
MyInstaller=Installer.InstallerClass().install(_AllBool=True)

#Definition the AttestedStr
SYS._attest(
    [
        'MyInstaller is '+SYS._str(
        MyInstaller,
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


*****Start of the Attest *****

MyInstaller is < (InstallerClass), 4540624784>
   /{
   /  '<New><Instance>IdInt' : 4540624784
   /  '<New><Instance>InstalledModulePathStrsList' : ['ShareYourSystem',
'ShareYourSystem/Objects/Object', 'ShareYourSystem/Objects/Initiator',
'ShareYourSystem/Classors/Classor', 'ShareYourSystem/Classors/Defaultor',
'ShareYourSystem/Classors/Doer', 'ShareYourSystem/Classors/Deriver',
'ShareYourSystem/Classors/Propertiser', 'ShareYourSystem/Classors/Inspecter',
'ShareYourSystem/Classors/Representer', 'ShareYourSystem/Objects/Printer',
'ShareYourSystem/Objects/Debugger', 'ShareYourSystem/Functers/Functer',
'ShareYourSystem/Classors/Attester', 'ShareYourSystem/Classors/Tester',
'ShareYourSystem/Functers/Functer', 'ShareYourSystem/Functers/Hooker',
'ShareYourSystem/Functers/Triggerer', 'ShareYourSystem/Objects/Conditioner',
'ShareYourSystem/Objects/Concluder', 'ShareYourSystem/Classors/Observer',
'ShareYourSystem/Classors/Binder', 'ShareYourSystem/Classors/Watcher',
'ShareYourSystem/Classors/Resetter', 'ShareYourSystem/Classors/Switcher',
'ShareYourSystem/Classors/Mimicker', 'ShareYourSystem/Objects/Caller',
'ShareYourSystem/Objects/Cloner', 'ShareYourSystem/Classors/Classer',
'ShareYourSystem/Objects/Rebooter', 'ShareYourSystem/Functers/Argumenter',
'ShareYourSystem/Functers/Imitater', 'ShareYourSystem/Functers/Alerter',
'ShareYourSystem/Interfacers/Interfacer',
'ShareYourSystem/Interfacers/Folderer', 'ShareYourSystem/Objects/Packager',
'ShareYourSystem/Interfacers/Filer', 'ShareYourSystem/Interfacers/Closer',
'ShareYourSystem/Interfacers/Loader', 'ShareYourSystem/Interfacers/Writer',
'ShareYourSystem/Interfacers/Deployer',
'ShareYourSystem/Interfacers/Hdformater',
'ShareYourSystem/Interfacers/Capturer', 'ShareYourSystem/Interfacers/Processer',
'ShareYourSystem/Interfacers/Statuser', 'ShareYourSystem/Interfacers/Killer',
'ShareYourSystem/Interfacers/Directer', 'ShareYourSystem/Guiders/Guider',
'ShareYourSystem/Guiders/Scriptbooker', 'ShareYourSystem/Guiders/Celler',
'ShareYourSystem/Guiders/Notebooker', 'ShareYourSystem/Guiders/Nbconverter',
'ShareYourSystem/Guiders/Installer', 'ShareYourSystem/Guiders/Documenter',
'ShareYourSystem/Guiders/Documenter', 'ShareYourSystem/Itemizers/Itemizer',
'ShareYourSystem/Itemizers/Getter', 'ShareYourSystem/Itemizers/Setter',
'ShareYourSystem/Itemizers/Deleter', 'ShareYourSystem/Itemizers/Attributer',
'ShareYourSystem/Itemizers/Restricter', 'ShareYourSystem/Itemizers/Pather',
'ShareYourSystem/Itemizers/Grasper', 'ShareYourSystem/Itemizers/Sharer',
'ShareYourSystem/Itemizers/Executer', 'ShareYourSystem/Applyiers/Applyier',
'ShareYourSystem/Applyiers/Mapper', 'ShareYourSystem/Applyiers/Picker',
'ShareYourSystem/Applyiers/Gatherer', 'ShareYourSystem/Applyiers/Updater',
'ShareYourSystem/Itemizers/Pointer', 'ShareYourSystem/Applyiers/Linker',
'ShareYourSystem/Applyiers/Weaver', 'ShareYourSystem/Applyiers/Filterer',
'ShareYourSystem/Noders/Noder', 'ShareYourSystem/Functers/Outputer',
'ShareYourSystem/Noders/Appender', 'ShareYourSystem/Noders/Instancer',
'ShareYourSystem/Noders/Adder', 'ShareYourSystem/Noders/Distinguisher',
'ShareYourSystem/Noders/Parenter', 'ShareYourSystem/Noders/Collecter',
'ShareYourSystem/Applyiers/Pusher', 'ShareYourSystem/Applyiers/Producer',
'ShareYourSystem/Noders/Catcher', 'ShareYourSystem/Noders/Attentioner',
'ShareYourSystem/Noders/Coupler', 'ShareYourSystem/Noders/Settler',
'ShareYourSystem/Applyiers/Commander', 'ShareYourSystem/Walkers/Walker',
'ShareYourSystem/Walkers/Cumulater', 'ShareYourSystem/Walkers/Visiter',
'ShareYourSystem/Walkers/Recruiter', 'ShareYourSystem/Walkers/Mobilizer',
'ShareYourSystem/Walkers/Router', 'ShareYourSystem/Walkers/Grabber',
'ShareYourSystem/Applyiers/Poker', 'ShareYourSystem/Noders/Connecter',
'ShareYourSystem/Noders/Networker', 'ShareYourSystem/Noders/Transmitter',
'ShareYourSystem/Noders/Grouper', 'ShareYourSystem/Noders/Structurer',
'ShareYourSystem/Noders/Organizer', 'ShareYourSystem/Storers/Storer',
'ShareYourSystem/Databasers', 'ShareYourSystem/Databasers/Databaser',
'ShareYourSystem/Databasers/Modeler', 'ShareYourSystem/Databasers/Tabularer',
'ShareYourSystem/Databasers/Tabler', 'ShareYourSystem/Databasers/Rower',
'ShareYourSystem/Databasers/Flusher', 'ShareYourSystem/Databasers/Retriever',
'ShareYourSystem/Databasers/Findoer', 'ShareYourSystem/Databasers/Recoverer',
'ShareYourSystem/Databasers/Shaper', 'ShareYourSystem/Databasers/Merger',
'ShareYourSystem/Databasers/Joiner', 'ShareYourSystem/Databasers/Hierarchizer',
'ShareYourSystem/Storers/Grider', 'ShareYourSystem/Storers/Explorer',
'ShareYourSystem/Storers/Controller', 'ShareYourSystem/Databasers/Featurer',
'ShareYourSystem/Databasers/Recuperater', 'ShareYourSystem/Ploters/Ploter',
'ShareYourSystem/Ploters/Axer', 'ShareYourSystem/Ploters/Paneler',
'ShareYourSystem/Ploters/Figurer', 'ShareYourSystem/Ploters/Pyploter',
'ShareYourSystem/Tutorials/Incrementer',
'ShareYourSystem/Tutorials/Decrementer', 'ShareYourSystem/Tutorials/Multiplier',
'ShareYourSystem/Tutorials/Sumer', 'ShareYourSystem/Tutorials/Modulizer',
'ShareYourSystem/Simulaters/Simulater', 'ShareYourSystem/Simulaters/Runner',
'ShareYourSystem/Simulaters/Moniter', 'ShareYourSystem/Simulaters/Populater',
'ShareYourSystem/Simulaters/Dynamizer', 'ShareYourSystem/Simulaters/Lifer',
'ShareYourSystem/Simulaters/Rater', 'ShareYourSystem/Simulaters/Brianer',
'ShareYourSystem/Simulaters/Pydelayer', 'ShareYourSystem/Muzikers/Muziker',
'ShareYourSystem/Muzikers/Vexflower', 'ShareYourSystem/Muzikers/Permuter',
'ShareYourSystem/Muzikers/Differenciater', 'ShareYourSystem/Muzikers/Pooler',
'ShareYourSystem/Muzikers/Harmonizer', 'ShareYourSystem/Objects',
'ShareYourSystem/Classors', 'ShareYourSystem/Functers',
'ShareYourSystem/Interfacers', 'ShareYourSystem/Guiders',
'ShareYourSystem/Itemizers', 'ShareYourSystem/Applyiers',
'ShareYourSystem/Walkers', 'ShareYourSystem/Noders', 'ShareYourSystem/Storers',
'ShareYourSystem/Databasers', 'ShareYourSystem/Ploters',
'ShareYourSystem/Tutorials', 'ShareYourSystem/Simulaters',
"ShareYourSystem/Muzikers'", "ShareYourSystem':["]
   /  '<New><Instance>InstalledNameStrsList' : ['ShareYourSystem', 'Object',
'Initiator', 'Classor', 'Defaultor', 'Doer', 'Deriver', 'Propertiser',
'Inspecter', 'Representer', 'Printer', 'Debugger', 'Functer', 'Attester',
'Tester', 'Functer', 'Hooker', 'Triggerer', 'Conditioner', 'Concluder',
'Observer', 'Binder', 'Watcher', 'Resetter', 'Switcher', 'Mimicker', 'Caller',
'Cloner', 'Classer', 'Rebooter', 'Argumenter', 'Imitater', 'Alerter',
'Interfacer', 'Folderer', 'Packager', 'Filer', 'Closer', 'Loader', 'Writer',
'Deployer', 'Hdformater', 'Capturer', 'Processer', 'Statuser', 'Killer',
'Directer', 'Guider', 'Scriptbooker', 'Celler', 'Notebooker', 'Nbconverter',
'Installer', 'Documenter', 'Documenter', 'Itemizer', 'Getter', 'Setter',
'Deleter', 'Attributer', 'Restricter', 'Pather', 'Grasper', 'Sharer',
'Executer', 'Applyier', 'Mapper', 'Picker', 'Gatherer', 'Updater', 'Pointer',
'Linker', 'Weaver', 'Filterer', 'Noder', 'Outputer', 'Appender', 'Instancer',
'Adder', 'Distinguisher', 'Parenter', 'Collecter', 'Pusher', 'Producer',
'Catcher', 'Attentioner', 'Coupler', 'Settler', 'Commander', 'Walker',
'Cumulater', 'Visiter', 'Recruiter', 'Mobilizer', 'Router', 'Grabber', 'Poker',
'Connecter', 'Networker', 'Transmitter', 'Grouper', 'Structurer', 'Organizer',
'Storer', 'Databasers', 'Databaser', 'Modeler', 'Tabularer', 'Tabler', 'Rower',
'Flusher', 'Retriever', 'Findoer', 'Recoverer', 'Shaper', 'Merger', 'Joiner',
'Hierarchizer', 'Grider', 'Explorer', 'Controller', 'Featurer', 'Recuperater',
'Ploter', 'Axer', 'Paneler', 'Figurer', 'Pyploter', 'Incrementer',
'Decrementer', 'Multiplier', 'Sumer', 'Modulizer', 'Simulater', 'Runner',
'Moniter', 'Populater', 'Dynamizer', 'Lifer', 'Rater', 'Brianer', 'Pydelayer',
'Muziker', 'Vexflower', 'Permuter', 'Differenciater', 'Pooler', 'Harmonizer',
'Objects', 'Classors', 'Functers', 'Interfacers', 'Guiders', 'Itemizers',
'Applyiers', 'Walkers', 'Noders', 'Storers', 'Databasers', 'Ploters',
'Tutorials', 'Simulaters', "Muzikers'", "ShareYourSystem':["]
   /  '<Spe><Instance>InstallingAllBool' : True
   /  '<Spe><Instance>InstallingModuleStrsList' : ['ShareYourSystem',
'ShareYourSystem.Objects.Object', 'ShareYourSystem.Objects.Initiator',
'ShareYourSystem.Classors.Classor', 'ShareYourSystem.Classors.Defaultor',
'ShareYourSystem.Classors.Doer', 'ShareYourSystem.Classors.Deriver',
'ShareYourSystem.Classors.Propertiser', 'ShareYourSystem.Classors.Inspecter',
'ShareYourSystem.Classors.Representer', 'ShareYourSystem.Objects.Printer',
'ShareYourSystem.Objects.Debugger', 'ShareYourSystem.Functers.Functer',
'ShareYourSystem.Classors.Attester', 'ShareYourSystem.Classors.Tester',
'ShareYourSystem.Functers.Functer', 'ShareYourSystem.Functers.Hooker',
'ShareYourSystem.Functers.Triggerer', 'ShareYourSystem.Objects.Conditioner',
'ShareYourSystem.Objects.Concluder', 'ShareYourSystem.Classors.Observer',
'ShareYourSystem.Classors.Binder', 'ShareYourSystem.Classors.Watcher',
'ShareYourSystem.Classors.Resetter', 'ShareYourSystem.Classors.Switcher',
'ShareYourSystem.Classors.Mimicker', 'ShareYourSystem.Objects.Caller',
'ShareYourSystem.Objects.Cloner', 'ShareYourSystem.Classors.Classer',
'ShareYourSystem.Objects.Rebooter', 'ShareYourSystem.Functers.Argumenter',
'ShareYourSystem.Functers.Imitater', 'ShareYourSystem.Functers.Alerter',
'ShareYourSystem.Interfacers.Interfacer',
'ShareYourSystem.Interfacers.Folderer', 'ShareYourSystem.Objects.Packager',
'ShareYourSystem.Interfacers.Filer', 'ShareYourSystem.Interfacers.Closer',
'ShareYourSystem.Interfacers.Loader', 'ShareYourSystem.Interfacers.Writer',
'ShareYourSystem.Interfacers.Deployer',
'ShareYourSystem.Interfacers.Hdformater',
'ShareYourSystem.Interfacers.Capturer', 'ShareYourSystem.Interfacers.Processer',
'ShareYourSystem.Interfacers.Statuser', 'ShareYourSystem.Interfacers.Killer',
'ShareYourSystem.Interfacers.Directer', 'ShareYourSystem.Guiders.Guider',
'ShareYourSystem.Guiders.Scriptbooker', 'ShareYourSystem.Guiders.Celler',
'ShareYourSystem.Guiders.Notebooker', 'ShareYourSystem.Guiders.Nbconverter',
'ShareYourSystem.Guiders.Installer', 'ShareYourSystem.Guiders.Documenter',
'ShareYourSystem.Guiders.Documenter', 'ShareYourSystem.Itemizers.Itemizer',
'ShareYourSystem.Itemizers.Getter', 'ShareYourSystem.Itemizers.Setter',
'ShareYourSystem.Itemizers.Deleter', 'ShareYourSystem.Itemizers.Attributer',
'ShareYourSystem.Itemizers.Restricter', 'ShareYourSystem.Itemizers.Pather',
'ShareYourSystem.Itemizers.Grasper', 'ShareYourSystem.Itemizers.Sharer',
'ShareYourSystem.Itemizers.Executer', 'ShareYourSystem.Applyiers.Applyier',
'ShareYourSystem.Applyiers.Mapper', 'ShareYourSystem.Applyiers.Picker',
'ShareYourSystem.Applyiers.Gatherer', 'ShareYourSystem.Applyiers.Updater',
'ShareYourSystem.Itemizers.Pointer', 'ShareYourSystem.Applyiers.Linker',
'ShareYourSystem.Applyiers.Weaver', 'ShareYourSystem.Applyiers.Filterer',
'ShareYourSystem.Noders.Noder', 'ShareYourSystem.Functers.Outputer',
'ShareYourSystem.Noders.Appender', 'ShareYourSystem.Noders.Instancer',
'ShareYourSystem.Noders.Adder', 'ShareYourSystem.Noders.Distinguisher',
'ShareYourSystem.Noders.Parenter', 'ShareYourSystem.Noders.Collecter',
'ShareYourSystem.Applyiers.Pusher', 'ShareYourSystem.Applyiers.Producer',
'ShareYourSystem.Noders.Catcher', 'ShareYourSystem.Noders.Attentioner',
'ShareYourSystem.Noders.Coupler', 'ShareYourSystem.Noders.Settler',
'ShareYourSystem.Applyiers.Commander', 'ShareYourSystem.Walkers.Walker',
'ShareYourSystem.Walkers.Cumulater', 'ShareYourSystem.Walkers.Visiter',
'ShareYourSystem.Walkers.Recruiter', 'ShareYourSystem.Walkers.Mobilizer',
'ShareYourSystem.Walkers.Router', 'ShareYourSystem.Walkers.Grabber',
'ShareYourSystem.Applyiers.Poker', 'ShareYourSystem.Noders.Connecter',
'ShareYourSystem.Noders.Networker', 'ShareYourSystem.Noders.Transmitter',
'ShareYourSystem.Noders.Grouper', 'ShareYourSystem.Noders.Structurer',
'ShareYourSystem.Noders.Organizer', 'ShareYourSystem.Storers.Storer',
'ShareYourSystem.Modelers', 'ShareYourSystem.Modelers.Databaser',
'ShareYourSystem.Modelers.Modeler', 'ShareYourSystem.Modelers.Tabularer',
'ShareYourSystem.Modelers.Tabler', 'ShareYourSystem.Modelers.Rower',
'ShareYourSystem.Modelers.Flusher', 'ShareYourSystem.Modelers.Retriever',
'ShareYourSystem.Modelers.Findoer', 'ShareYourSystem.Modelers.Recoverer',
'ShareYourSystem.Modelers.Shaper', 'ShareYourSystem.Modelers.Merger',
'ShareYourSystem.Modelers.Joiner', 'ShareYourSystem.Modelers.Hierarchizer',
'ShareYourSystem.Storers.Grider', 'ShareYourSystem.Storers.Explorer',
'ShareYourSystem.Storers.Controller', 'ShareYourSystem.Modelers.Featurer',
'ShareYourSystem.Modelers.Recuperater', 'ShareYourSystem.Ploters.Ploter',
'ShareYourSystem.Ploters.Axer', 'ShareYourSystem.Ploters.Paneler',
'ShareYourSystem.Ploters.Figurer', 'ShareYourSystem.Ploters.Pyploter',
'ShareYourSystem.Tutorials.Incrementer',
'ShareYourSystem.Tutorials.Decrementer', 'ShareYourSystem.Tutorials.Multiplier',
'ShareYourSystem.Tutorials.Sumer', 'ShareYourSystem.Tutorials.Modulizer',
'ShareYourSystem.Simulaters.Simulater', 'ShareYourSystem.Simulaters.Runner',
'ShareYourSystem.Simulaters.Moniter', 'ShareYourSystem.Simulaters.Populater',
'ShareYourSystem.Simulaters.Dynamizer', 'ShareYourSystem.Simulaters.Lifer',
'ShareYourSystem.Simulaters.Rater', 'ShareYourSystem.Simulaters.Brianer',
'ShareYourSystem.Simulaters.Pydelayer', 'ShareYourSystem.Muzikers.Muziker',
'ShareYourSystem.Muzikers.Vexflower', 'ShareYourSystem.Muzikers.Permuter',
'ShareYourSystem.Muzikers.Differenciater', 'ShareYourSystem.Muzikers.Pooler',
'ShareYourSystem.Muzikers.Harmonizer', 'ShareYourSystem.Objects',
'ShareYourSystem.Classors', 'ShareYourSystem.Functers',
'ShareYourSystem.Interfacers', 'ShareYourSystem.Guiders',
'ShareYourSystem.Itemizers', 'ShareYourSystem.Applyiers',
'ShareYourSystem.Walkers', 'ShareYourSystem.Noders', 'ShareYourSystem.Storers',
'ShareYourSystem.Modelers', 'ShareYourSystem.Ploters',
'ShareYourSystem.Tutorials', 'ShareYourSystem.Simulaters',
"ShareYourSystem.Muzikers'", "ShareYourSystem':["]
   /}

*****End of the Attest *****



```

