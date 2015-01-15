

<!--
FrozenIsBool False
-->

#Notebooker

----------------------- ------------------------------------



@Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



The Installer directs a readme call in a ShareYourSystem directory.



----------------------------------------------------------------


View the Notebooker sources on [Github](https://github.com/Ledoux/ShareYourSyste
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
from ShareYourSystem.Guiders import Notebooker

#Definition a Notebooker
MyNotebooker=Notebooker.NotebookerClass().notebook(
    'Presentation.ipynb',
    **{
        'FolderingPathStr':
        SYS.ShareYourSystemLocalFolderPathStr+'/ShareYourSystem/Objects/Concluder',
        #SYS.ShareYourSystemLocalFolderPathStr+'/ShareYourSystem/Objects',
        'GuidingBookStr':'Doc'
    }
).notebook(
    **{
        'FolderingPathStr':
        SYS.ShareYourSystemLocalFolderPathStr+'/ShareYourSystem/Interfacers/Filer',
    }
)

#Definition the AttestedStr
SYS._attest(
    [
        'MyNotebooker is '+SYS._str(
        MyNotebooker,
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

                        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                        ////////////////////////////////
                        Doer/__init__.py do
                        From <string> superDo_debug | Notebooker/__init__.py
do_notebook | Doer/__init__.py do | <string> superDo_notebook |
Watcher/__init__.py watch | <string> watch_superDo_notebook | <string> <module>
| <string> <module> | site-packages/six.py exec_ | Celler/__init__.py do_cell |
Doer/__init__.py do | <string> superDo_cell | Watcher/__init__.py watch |
<string> watch_superDo_cell | Notebooker/__init__.py do_notebook |
Doer/__init__.py do | <string> superDo_notebook | Watcher/__init__.py watch |
<string> watch_superDo_notebook | Informer/__init__.py
getInformedReadmeInstanceVariableWithFolderPathStr | Informer/__init__.py
do_inform | Doer/__init__.py do | <string> superDo_inform | Watcher/__init__.py
watch | <string> watch_superDo_inform | inform.py <module>
                        ////////////////////////////////

                        l.180 :
                        *****
                        I am with []
                        *****
                        self.ScriptbookedSortDict is
                           /{
                           /  'ExampleDoc.md' : 00_ExampleDoc.md
                           /  'ExampleDoc.py' : 01_ExampleDoc.py
                           /  'GithubDoc.md' : 001_GithubDoc.md
                           /}

                        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                            ////////////////////////////////
                                            Doer/__init__.py do
                                            From <string> superDo_debug |
Celler/__init__.py do_cell | Doer/__init__.py do | <string> superDo_cell |
Watcher/__init__.py watch | <string> watch_superDo_cell | Notebooker/__init__.py
do_notebook | Doer/__init__.py do | <string> superDo_notebook |
Watcher/__init__.py watch | <string> watch_superDo_notebook | <string> <module>
| <string> <module> | site-packages/six.py exec_ | Celler/__init__.py do_cell |
Doer/__init__.py do | <string> superDo_cell | Watcher/__init__.py watch |
<string> watch_superDo_cell | Notebooker/__init__.py do_notebook |
Doer/__init__.py do | <string> superDo_notebook | Watcher/__init__.py watch |
<string> watch_superDo_notebook | Informer/__init__.py
getInformedReadmeInstanceVariableWithFolderPathStr | Informer/__init__.py
do_inform | Doer/__init__.py do | <string> superDo_inform | Watcher/__init__.py
watch | <string> watch_superDo_inform | inform.py <module>
                                            ////////////////////////////////

                                            l.180 :
                                            *****
                                            I am with []
                                            *****
                                            self.FolderingPathStr is
/Users/ledoux/Documents/ShareYourSystem/ShareYourSystem/Objects/Concluder/

                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                            ////////////////////////////////
                                            Doer/__init__.py do
                                            From <string> superDo_debug |
Celler/__init__.py do_cell | Doer/__init__.py do | <string> superDo_cell |
Watcher/__init__.py watch | <string> watch_superDo_cell | Notebooker/__init__.py
do_notebook | Doer/__init__.py do | <string> superDo_notebook |
Watcher/__init__.py watch | <string> watch_superDo_notebook | <string> <module>
| <string> <module> | site-packages/six.py exec_ | Celler/__init__.py do_cell |
Doer/__init__.py do | <string> superDo_cell | Watcher/__init__.py watch |
<string> watch_superDo_cell | Notebooker/__init__.py do_notebook |
Doer/__init__.py do | <string> superDo_notebook | Watcher/__init__.py watch |
<string> watch_superDo_notebook | Informer/__init__.py
getInformedReadmeInstanceVariableWithFolderPathStr | Informer/__init__.py
do_inform | Doer/__init__.py do | <string> superDo_inform | Watcher/__init__.py
watch | <string> watch_superDo_inform | inform.py <module>
                                            ////////////////////////////////

                                            l.180 :
                                            *****
                                            I am with []
                                            *****
                                            self.FolderingPathStr is
/Users/ledoux/Documents/ShareYourSystem/ShareYourSystem/Objects/Concluder/

                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                            ////////////////////////////////
                                            Doer/__init__.py do
                                            From <string> superDo_debug |
Celler/__init__.py do_cell | Doer/__init__.py do | <string> superDo_cell |
Watcher/__init__.py watch | <string> watch_superDo_cell | Notebooker/__init__.py
do_notebook | Doer/__init__.py do | <string> superDo_notebook |
Watcher/__init__.py watch | <string> watch_superDo_notebook | <string> <module>
| <string> <module> | site-packages/six.py exec_ | Celler/__init__.py do_cell |
Doer/__init__.py do | <string> superDo_cell | Watcher/__init__.py watch |
<string> watch_superDo_cell | Notebooker/__init__.py do_notebook |
Doer/__init__.py do | <string> superDo_notebook | Watcher/__init__.py watch |
<string> watch_superDo_notebook | Informer/__init__.py
getInformedReadmeInstanceVariableWithFolderPathStr | Informer/__init__.py
do_inform | Doer/__init__.py do | <string> superDo_inform | Watcher/__init__.py
watch | <string> watch_superDo_inform | inform.py <module>
                                            ////////////////////////////////

                                            l.180 :
                                            *****
                                            I am with []
                                            *****
                                            self.FolderingPathStr is
/Users/ledoux/Documents/ShareYourSystem/ShareYourSystem/Objects/Concluder/

                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                            ////////////////////////////////
                                            Doer/__init__.py do
                                            From <string> superDo_debug |
Writer/__init__.py do_write | Doer/__init__.py do | <string> superDo_write |
Watcher/__init__.py watch | <string> watch_superDo_write |
Notebooker/__init__.py do_notebook | Doer/__init__.py do | <string>
superDo_notebook | Watcher/__init__.py watch | <string> watch_superDo_notebook |
<string> <module> | <string> <module> | site-packages/six.py exec_ |
Celler/__init__.py do_cell | Doer/__init__.py do | <string> superDo_cell |
Watcher/__init__.py watch | <string> watch_superDo_cell | Notebooker/__init__.py
do_notebook | Doer/__init__.py do | <string> superDo_notebook |
Watcher/__init__.py watch | <string> watch_superDo_notebook |
Informer/__init__.py getInformedReadmeInstanceVariableWithFolderPathStr |
Informer/__init__.py do_inform | Doer/__init__.py do | <string> superDo_inform |
Watcher/__init__.py watch | <string> watch_superDo_inform | inform.py <module>
                                            ////////////////////////////////

                                            l.180 :
                                            *****
                                            I am with []
                                            *****
                                            we write in json...
                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                        ////////////////////////////////
                        Doer/__init__.py do
                        From <string> superDo_debug | Notebooker/__init__.py
do_notebook | Doer/__init__.py do | <string> superDo_notebook |
Watcher/__init__.py watch | <string> watch_superDo_notebook | <string> <module>
| <string> <module> | site-packages/six.py exec_ | Celler/__init__.py do_cell |
Doer/__init__.py do | <string> superDo_cell | Watcher/__init__.py watch |
<string> watch_superDo_cell | Notebooker/__init__.py do_notebook |
Doer/__init__.py do | <string> superDo_notebook | Watcher/__init__.py watch |
<string> watch_superDo_notebook | Informer/__init__.py
getInformedReadmeInstanceVariableWithFolderPathStr | Informer/__init__.py
do_inform | Doer/__init__.py do | <string> superDo_inform | Watcher/__init__.py
watch | <string> watch_superDo_inform | inform.py <module>
                        ////////////////////////////////

                        l.180 :
                        *****
                        I am with []
                        *****
                        self.ScriptbookedSortDict is
                           /{
                           /  'ExampleDoc.md' : 00_ExampleDoc.md
                           /  'ExampleDoc.py' : 01_ExampleDoc.py
                           /  'GithubDoc.md' : 001_GithubDoc.md
                           /}

                        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                            ////////////////////////////////
                                            Doer/__init__.py do
                                            From <string> superDo_debug |
Celler/__init__.py do_cell | Doer/__init__.py do | <string> superDo_cell |
Watcher/__init__.py watch | <string> watch_superDo_cell | Notebooker/__init__.py
do_notebook | Doer/__init__.py do | <string> superDo_notebook |
Watcher/__init__.py watch | <string> watch_superDo_notebook | <string> <module>
| <string> <module> | site-packages/six.py exec_ | Celler/__init__.py do_cell |
Doer/__init__.py do | <string> superDo_cell | Watcher/__init__.py watch |
<string> watch_superDo_cell | Notebooker/__init__.py do_notebook |
Doer/__init__.py do | <string> superDo_notebook | Watcher/__init__.py watch |
<string> watch_superDo_notebook | Informer/__init__.py
getInformedReadmeInstanceVariableWithFolderPathStr | Informer/__init__.py
do_inform | Doer/__init__.py do | <string> superDo_inform | Watcher/__init__.py
watch | <string> watch_superDo_inform | inform.py <module>
                                            ////////////////////////////////

                                            l.180 :
                                            *****
                                            I am with []
                                            *****
                                            self.FolderingPathStr is
/Users/ledoux/Documents/ShareYourSystem/ShareYourSystem/Interfacers/Filer/

                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                            ////////////////////////////////
                                            Doer/__init__.py do
                                            From <string> superDo_debug |
Celler/__init__.py do_cell | Doer/__init__.py do | <string> superDo_cell |
Watcher/__init__.py watch | <string> watch_superDo_cell | Notebooker/__init__.py
do_notebook | Doer/__init__.py do | <string> superDo_notebook |
Watcher/__init__.py watch | <string> watch_superDo_notebook | <string> <module>
| <string> <module> | site-packages/six.py exec_ | Celler/__init__.py do_cell |
Doer/__init__.py do | <string> superDo_cell | Watcher/__init__.py watch |
<string> watch_superDo_cell | Notebooker/__init__.py do_notebook |
Doer/__init__.py do | <string> superDo_notebook | Watcher/__init__.py watch |
<string> watch_superDo_notebook | Informer/__init__.py
getInformedReadmeInstanceVariableWithFolderPathStr | Informer/__init__.py
do_inform | Doer/__init__.py do | <string> superDo_inform | Watcher/__init__.py
watch | <string> watch_superDo_inform | inform.py <module>
                                            ////////////////////////////////

                                            l.180 :
                                            *****
                                            I am with []
                                            *****
                                            self.FolderingPathStr is
/Users/ledoux/Documents/ShareYourSystem/ShareYourSystem/Interfacers/Filer/

                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                            ////////////////////////////////
                                            Doer/__init__.py do
                                            From <string> superDo_debug |
Celler/__init__.py do_cell | Doer/__init__.py do | <string> superDo_cell |
Watcher/__init__.py watch | <string> watch_superDo_cell | Notebooker/__init__.py
do_notebook | Doer/__init__.py do | <string> superDo_notebook |
Watcher/__init__.py watch | <string> watch_superDo_notebook | <string> <module>
| <string> <module> | site-packages/six.py exec_ | Celler/__init__.py do_cell |
Doer/__init__.py do | <string> superDo_cell | Watcher/__init__.py watch |
<string> watch_superDo_cell | Notebooker/__init__.py do_notebook |
Doer/__init__.py do | <string> superDo_notebook | Watcher/__init__.py watch |
<string> watch_superDo_notebook | Informer/__init__.py
getInformedReadmeInstanceVariableWithFolderPathStr | Informer/__init__.py
do_inform | Doer/__init__.py do | <string> superDo_inform | Watcher/__init__.py
watch | <string> watch_superDo_inform | inform.py <module>
                                            ////////////////////////////////

                                            l.180 :
                                            *****
                                            I am with []
                                            *****
                                            self.FolderingPathStr is
/Users/ledoux/Documents/ShareYourSystem/ShareYourSystem/Interfacers/Filer/

                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                            ////////////////////////////////
                                            Doer/__init__.py do
                                            From <string> superDo_debug |
Writer/__init__.py do_write | Doer/__init__.py do | <string> superDo_write |
Watcher/__init__.py watch | <string> watch_superDo_write |
Notebooker/__init__.py do_notebook | Doer/__init__.py do | <string>
superDo_notebook | Watcher/__init__.py watch | <string> watch_superDo_notebook |
<string> <module> | <string> <module> | site-packages/six.py exec_ |
Celler/__init__.py do_cell | Doer/__init__.py do | <string> superDo_cell |
Watcher/__init__.py watch | <string> watch_superDo_cell | Notebooker/__init__.py
do_notebook | Doer/__init__.py do | <string> superDo_notebook |
Watcher/__init__.py watch | <string> watch_superDo_notebook |
Informer/__init__.py getInformedReadmeInstanceVariableWithFolderPathStr |
Informer/__init__.py do_inform | Doer/__init__.py do | <string> superDo_inform |
Watcher/__init__.py watch | <string> watch_superDo_inform | inform.py <module>
                                            ////////////////////////////////

                                            l.180 :
                                            *****
                                            I am with []
                                            *****
                                            we write in json...
                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



*****Start of the Attest *****

MyNotebooker is < (NotebookerClass), 4466232400>
   /{
   /  '<New><Instance>IdStr' : 4466232400
   /  '<New><Instance>NotebookedScriptStrsList' : ['Markdown', 'Markdown',
'Python']
   /  '<New><Instance>ScriptbookedSortDict' :
   /   /{
   /   /  'ExampleDoc.md' : 00_ExampleDoc.md
   /   /  'ExampleDoc.py' : 01_ExampleDoc.py
   /   /  'GithubDoc.md' : 001_GithubDoc.md
   /   /}
   /  '<New><Instance>_CapturingStopBool' : True
   /  '<Spe><Class>NotebookingWriteBool' : True
   /  '<Spe><Instance>NotebookedCodeDict' :
   /   /{
   /   /  'metadata' :
   /   /   /{
   /   /   /  'name' :
   /   /   /  'signature' :
   /   /   /}
   /   /  'nbformat' : 3
   /   /  'nbformat_minor' : 0
   /   /  'worksheets' :
   /   /   /[
   /   /   /  0 :
   /   /   /   /{
   /   /   /   /  'cells' :
   /   /   /   /   /[
   /   /   /   /   /  0 :
   /   /   /   /   /   /{
   /   /   /   /   /   /  'cell_type' : markdown
   /   /   /   /   /   /  'metadata' :
   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /  'slideshow' :
   /   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /   /  'slide_type' : slide
   /   /   /   /   /   /   /   /}
   /   /   /   /   /   /   /}
   /   /   /   /   /   /  'prompt_number' : 0
   /   /   /   /   /   /  'source' :
<!--
FrozenIsBool False
-->

#Filer

----------------------- ------------------------------------



@Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



The Notebooker takes piece of .md,.py,.tex files for putting them in a IPython
Notebook



----------------------------------------------------------------


View the Filer sources on [Github](https://github.com/Ledoux/ShareYourSystem/tre
e/master/ShareYourSystem.Guiders.Notebooker)


   /   /   /   /   /   /}
   /   /   /   /   /  1 :
   /   /   /   /   /   /{
   /   /   /   /   /   /  'cell_type' : markdown
   /   /   /   /   /   /  'metadata' :
   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /  'slideshow' :
   /   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /   /  'slide_type' : subslide
   /   /   /   /   /   /   /   /}
   /   /   /   /   /   /   /}
   /   /   /   /   /   /  'prompt_number' : 1
   /   /   /   /   /   /  'source' :
<!---
FrozenIsBool True
-->

##Example

Let's create an empty class, which will automatically receive
special attributes from the decorating ClassorClass,
specially the NameStr, that should be the ClassStr
without the TypeStr in the end.
   /   /   /   /   /   /}
   /   /   /   /   /  2 :
   /   /   /   /   /   /{
   /   /   /   /   /   /  'cell_type' : code
   /   /   /   /   /   /  'collapsed' : False
   /   /   /   /   /   /  'input' : ['#ImportModules\n', 'import ShareYourSystem
as SYS\n', 'from ShareYourSystem.Interfacers import Filer\n', '\n', '#Definition
of an instance Filer and make it find the current dir\n',
"MyFiler=Filer.FilerClass().file('MyFile.txt','w')\n",
'MyFiler.FiledFileVariable.close()\n', '\t\n', '#Definition the AttestedStr\n',
'SYS._attest(\n', '\t[\n', "\t\t'MyFiler is '+SYS._str(MyFiler,\n",
"\t\t**{'RepresentingAlineaIsBool':False})\n", '\t]\n', ') \n', '\n',
'#Print\n', '\n', '\n']
   /   /   /   /   /   /  'language' : python
   /   /   /   /   /   /  'metadata' :
   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /  'slideshow' :
   /   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /   /  'slide_type' : -
   /   /   /   /   /   /   /   /}
   /   /   /   /   /   /   /}
   /   /   /   /   /   /  'outputs' :
   /   /   /   /   /   /   /[
   /   /   /   /   /   /   /  0 :
   /   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /   /  'output_type' : stream
   /   /   /   /   /   /   /   /  'stream' : stdout
   /   /   /   /   /   /   /   /  'text' : ['\n', '\n', '*****Start of the
Attest *****\n', '\n', 'MyFiler is < (FilerClass), 4466404176>\n', '   /{ \n', "
/  '<New><Instance>IdStr' : 4466404176\n", "   /
'<Spe><Instance>FiledFileVariable' : <closed file
'/Users/ledoux/Documents/ShareYourSystem/MyFile.txt', mode 'w' at
0x10a30c390>\n", "   /  '<Spe><Instance>FiledPathStr' :
/Users/ledoux/Documents/ShareYourSystem/MyFile.txt\n", "   /
'<Spe><Instance>FilingKeyStr' : MyFile.txt\n", "   /
'<Spe><Instance>FilingModeStr' : w\n", '   /}\n', '\n', '*****End of the Attest
*****\n', '\n', '\n']
   /   /   /   /   /   /   /   /}
   /   /   /   /   /   /   /]
   /   /   /   /   /   /  'prompt_number' : 2
   /   /   /   /   /   /}
   /   /   /   /   /]
   /   /   /   /}
   /   /   /]
   /   /}
   /  '<Spe><Instance>NotebookedPageStrsList' : ['GithubDoc', 'ExampleDoc',
'ExampleDoc']
   /  '<Spe><Instance>NotebookedSubslideStrsList' : ['slide', 'subslide', '-']
   /  '<Spe><Instance>NotebookedTextStrsList' : ['\n<!--\nFrozenIsBool
False\n-->\n\n#Filer\n\n-----------------------
------------------------------------\n\n\n\n@Date : Fri Nov 14 13:20:38 2014
\n\n@Author : Erwan Ledoux \n\n\n\nThe Notebooker takes piece of .md,.py,.tex
files for putting them in a IPython Notebook\n\n\n\n----------------------------
------------------------------------\n\n\nView the Filer sources on [Github](htt
ps://github.com/Ledoux/ShareYourSystem/tree/master/ShareYourSystem.Guiders.Noteb
ooker)\n\n', "\n<!---\nFrozenIsBool True\n-->\n\n##Example\n\nLet's create an
empty class, which will automatically receive\nspecial attributes from the
decorating ClassorClass,\nspecially the NameStr, that should be the
ClassStr\nwithout the TypeStr in the end.", "#ImportModules\nimport
ShareYourSystem as SYS\nfrom ShareYourSystem.Interfacers import
Filer\n\n#Definition of an instance Filer and make it find the current dir\nMyFi
ler=Filer.FilerClass().file('MyFile.txt','w')\nMyFiler.FiledFileVariable.close()
\n\t\n#Definition the AttestedStr\nSYS._attest(\n\t[\n\t\t'MyFiler is
'+SYS._str(MyFiler,\n\t\t**{'RepresentingAlineaIsBool':False})\n\t]\n)
\n\n#Print\n\n"]
   /  '<Spe><Instance>NotebookingFileKeyStr' : Presentation.ipynb
   /}

*****End of the Attest *****



```

