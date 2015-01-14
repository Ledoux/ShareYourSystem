

<!--
FrozenIsBool False
-->

#Deployer

##Doc
----


>
> The Deployer
>
>

----

<small>
View the Deployer notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyo
ursystem.ouvaton.org/Deployer.ipynb)
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


The Deployer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Interfacers.Capturer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import os
import ftplib
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class DeployerClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
                                                'DeployingUrlStr',
                                                'DeployingLoginStr',
                                                'DeployingPwdStr',
'DeployingClientFilePathStrToServerFilePathStrOrderedDict',
                                                'DeployedFtplibVariable',
                                                'DeployedDirKeyStrsList'
                                        ]

        def default_init(self,
_DeployingUrlStr="ftp.ouvaton.coop",
_DeployingLoginStr="shareyoursystemhz",
                                                _DeployingPwdStr="share",
_DeployingClientFilePathStrToServerFilePathStrOrderedDict=None,
                                                _DeployedFtplibVariable=None,
                                                _DeployedDirKeyStrsList=None,
                                                **_KwargVariablesDict
                                        ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_deploy(self):

                #open and login
                self.DeployedFtplibVariable = ftplib.FTP(self.DeployingUrlStr);
                self.DeployedFtplibVariable.login(
                        user=self.DeployingLoginStr,
                        passwd=self.DeployingPwdStr
                );

                """
                #delete all the files in the root folder
self.DeployedFtplibVariable.cwd(self.DeployingServerFolderPathStr);
                for __ListedVariable in self.DeployedFtplibVariable.nlst():
                    try:
                        self.DeployedFtplibVariable.delete(__ListedVariable);
                    except Exception:
                        self.DeployedFtplibVariable.rmd(__ListedVariable);

                #delete the dir and create a new one
                try:
self.DeployedFtplibVariable.rmd(self.DeployingServerFolderPathStr);
                except Exception:
                    pass;
self.DeployedFtplibVariable.mkd(self.DeployingServerFolderPathStr);
                """

                #debug
                self.debug(('self.',self,[
'DeployingClientFilePathStrToServerFilePathStrOrderedDict'
                                                                ]))

                #store
                map(
                                lambda
__DeployingClientFilePathStrToServerFilePathStrItemTuple:
                                self.DeployedFtplibVariable.storbinary(
                                        'STOR
'+__DeployingClientFilePathStrToServerFilePathStrItemTuple[1],
                                        open(
__DeployingClientFilePathStrToServerFilePathStrItemTuple[0],
                                        'rb'
                                        )
                                ),
self.DeployingClientFilePathStrToServerFilePathStrOrderedDict.items()
                        )

                #ls
                self.DeployedDirKeyStrsList=map(
                        lambda
__DeployingClientFilePathStrToServerFilePathStrItemTuple:
                        self.DeployedFtplibVariable.nlst(
__DeployingClientFilePathStrToServerFilePathStrItemTuple[1]
                        ),
self.DeployingClientFilePathStrToServerFilePathStrOrderedDict.items()
                )

                #quit
                self.DeployedFtplibVariable.quit();

#</DefineClass>

```

<small>
View the Deployer sources on [Github](https://github.com/Ledoux/ShareYourSystem/
tree/master/ShareYourSystem/Interfacers/Deployer)
</small>



```python
#ImportModules
import ShareYourSystem as SYS

from ShareYourSystem.Interfacers import Folderer,Deployer

#Definition a Deployer
MyDeployer=Deployer.DeployerClass().deploy()

#Definition the AttestedStr
SYS._attest(
    [
        'MyDeployer is '+SYS._str(
        MyDeployer,
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

                    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                    ////////////////////////////////
                    Deployer/__init__.py do_deploy
                    From Deployer/__init__.py do_deploy | site-packages/six.py
exec_ | Celler/__init__.py do_cell | Notebooker/__init__.py do_notebook |
Informer/__init__.py do_inform | inform.py <module>
                    ////////////////////////////////

                    l.82 :
                    *****
                    I am with []
                    *****
self.DeployingClientFilePathStrToServerFilePathStrOrderedDict is
                       /{
                       /}

                    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



*****Start of the Attest *****

MyDeployer is < (DeployerClass), 4391206480>
   /{
   /  '<New><Instance>IdInt' : 4391206480
   /  '<Spe><Class>DeployingLoginStr' : shareyoursystemhz
   /  '<Spe><Class>DeployingPwdStr' : share
   /  '<Spe><Class>DeployingUrlStr' : ftp.ouvaton.coop
   /  '<Spe><Instance>DeployedDirKeyStrsList' : []
   /  '<Spe><Instance>DeployedFtplibVariable' : <ftplib.FTP instance at
0x105bb1050>
   /  '<Spe><Instance>DeployingClientFilePathStrToServerFilePathStrOrderedDict'
:
   /   /{
   /   /}
   /}

*****End of the Attest *****



```

