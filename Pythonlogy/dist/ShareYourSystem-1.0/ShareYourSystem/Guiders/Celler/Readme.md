

<!--
FrozenIsBool False
-->

#Celler

----------------------- ------------------------------------



@Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



The Installer directs a readme call in a ShareYourSystem directory.



----------------------------------------------------------------


View the Celler sources on [Github](https://github.com/Ledoux/ShareYourSystem/tr
ee/master/ShareYourSystem.Guiders.Informer)




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
from ShareYourSystem.Guiders import Celler

#Definition an instance
MyCeller=Celler.CellerClass().load(
    **{
        'FolderingPathStr':
        SYS.ShareYourSystemLocalFolderPathStr+'/ShareYourSystem/Objects/Rebooter',
        'FilingKeyStr':'01_ExampleDoc.py'
    }
)
MyCeller.cell(MyCeller.LoadedReadVariable,'Python')

#Definition the AttestedStr
SYS._attest(
    [
        'MyCeller is '+SYS._str(
                MyCeller,
                **{
                'RepresentingBaseKeyStrsListBool':False,
                'RepresentingAlineaIsBool':False
                }
            )
    ]
)



```


```console
>>>

                        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                        ////////////////////////////////
                        Doer/__init__.py do
                        From <string> superDo_debug | Celler/__init__.py do_cell
| Doer/__init__.py do | <string> superDo_cell | Watcher/__init__.py watch |
<string> watch_superDo_cell | <string> <module> | <string> <module> | site-
packages/six.py exec_ | Celler/__init__.py do_cell | Doer/__init__.py do |
<string> superDo_cell | Watcher/__init__.py watch | <string> watch_superDo_cell
| Notebooker/__init__.py do_notebook | Doer/__init__.py do | <string>
superDo_notebook | Watcher/__init__.py watch | <string> watch_superDo_notebook |
Informer/__init__.py getInformedReadmeInstanceVariableWithFolderPathStr |
Informer/__init__.py do_inform | Doer/__init__.py do | <string> superDo_inform |
Watcher/__init__.py watch | <string> watch_superDo_inform | inform.py <module>
                        ////////////////////////////////

                        l.180 :
                        *****
                        I am with []
                        *****
                        self.FolderingPathStr is
/Users/ledoux/Documents/ShareYourSystem/ShareYourSystem/Objects/Rebooter/

                        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



*****Start of the Attest *****

MyCeller is < (CellerClass), 4466233296>
   /{
   /  '<New><Instance>IdStr' : 4466233296
   /  '<New><Instance>_CapturingStopBool' : True
   /  '<Spe><Instance>CelledNoteDict' :
   /   /{
   /   /  'cell_type' : code
   /   /  'collapsed' : False
   /   /  'input' : ['#ImportModules\n', 'import ShareYourSystem as SYS\n',
'from ShareYourSystem.Classors import Classer\n', 'from ShareYourSystem.Objects
import Rebooter\n', '\n', '#Definition \n', '@Classer.ClasserClass(**\n', '{\n',
"\t'ClassingSwitchMethodStrsList':['make']\n", '})\n', 'class
MakerClass(Rebooter.RebooterClass):\n', '\n', '\t#Definition\n',
'\tRepresentingKeyStrsList=[\n', "\t\t\t\t\t\t\t\t'MakingMyFloat',\n",
"\t\t\t\t\t\t\t\t'MadeMyInt'\n", '\t\t\t\t\t\t\t]\n', '\n', '\tdef
__init__(self,\n', '\t\t\t\t\t_MakingMyFloat=0.,\n',
'\t\t\t\t\t_MadeMyInt=0,\n', '\t\t\t\t\t**_KwarVariablesDict\n', '\t\t\t\t):\n',
'\t\tRebooter.RebooterClass.__init__(self,**_KwarVariablesDict)\n', '\n',
'\t#<DefineDoMethod>\n', '\tdef do_make(self):\n', '\t\t\n', '\t\t#print\n',
"\t\tprint('I am in the do_make of the Maker')\n", '\n', '\t\t#cast\n',
'\t\tself.MadeMyInt=int(self.MakingMyFloat)\n', '\n', '#Definition\n',
'@Classer.ClasserClass(**{\n', '\t\'ClassingSwitchMethodStrsList\':["make"]\n',
'})\n', 'class BuilderClass(MakerClass):\n', '\n', '\t#Definition\n',
'\tRepresentingKeyStrsList=[\n', '\t\t\t\t\t\t\t]\n', '\n', '\tdef
__init__(self,\n', '\t\t\t\t\t**_KwarVariablesDict\n', '\t\t\t\t):\n',
'\t\tMakerClass.__init__(self,**_KwarVariablesDict)\n', '\n', '\tdef
mimic_make(self):\n', '\t\t\n', '\t\t#print\n', "\t\tprint('I am in the
mimic_make of the Builder')\n", '\n', '\t\t#call the parent method\n',
'\t\tMakerClass.make(self)\n', '\n', '\t\t#cast\n', '\t\tself.MadeMyInt+=10\n',
'\n', '\t#<DefineDoMethod>\n', '\tdef do_build(self):\n', '\t\tpass\n', '\n',
'\n', '#Definition an instance\n', 'MyBuilder=BuilderClass()\n', '\n',
'#Print\n', "print('Before make, MyBuilder is ')\n",
'SYS._print(MyBuilder,**{\n', "\t'RepresentingKeyStrsList':[\n",
"\t'MakingMyFloat',\n", "\t'MadeMyInt',\n", '\t]\n', '})\n', '\n', '#make
once\n', 'MyBuilder.make(3.)\n', '\n', '#Print\n', "print('After the first make,
MyBuilder is ')\n", 'SYS._print(MyBuilder,**{\n',
"\t'RepresentingKeyStrsList':[\n", "\t'MakingMyFloat',\n", "\t'MadeMyInt',\n",
"\t'_WatchMakeWithMakerBool'\n", '\t]\n', '})\n', '\n', '#make again\n',
'MyBuilder.make(5.)\n', '\n', '#Print\n', "print('After the second make,
MyBuilder is ')\n", 'SYS._print(MyBuilder,**{\n',
"\t'RepresentingKeyStrsList':[\n", "\t'MakingMyFloat',\n", "\t'MadeMyInt',\n",
"\t'_WatchMakeWithMakerBool'\n", '\t]\n', '})\n', '\n', '\n', '#make again\n',
"print('Now we reboot')\n", "MyBuilder.reboot(['Make'])\n", '\n', '#Print\n',
"print('After the reboot, MyBuilder is ')\n", 'SYS._print(MyBuilder,**{\n',
"\t'RepresentingKeyStrsList':[\n", "\t'MakingMyFloat',\n", "\t'MadeMyInt',\n",
"\t'_WatchMakeWithMakerBool'\n", '\t]\n', '})\n', '\n', '#make again\n',
'MyBuilder.make(8.)\n', '\n', '#Definition the AttestedStr\n', 'SYS._attest(\n',
'\t[\n', "\t\t'MyBuilder is '+SYS._str(\n", '\t\tMyBuilder,\n', '\t\t**{\n',
"\t\t\t'RepresentingAlineaIsBool':False,\n",
"\t\t\t'RepresentingKeyStrsList':[\n", "\t\t\t\t'MakingMyFloat',\n",
"\t\t\t\t'MadeMyInt',\n", "\t\t\t\t'_WatchMakeWithMakerBool',\n",
"\t\t\t\t'RebootedWatchBoolKeyStrsList'\n", '\t\t\t]\n', '\t\t\t}\n', '\t\t)\n',
'\t]\n', ') \n']
   /   /  'language' : python
   /   /  'metadata' :
   /   /   /{
   /   /   /  'slideshow' :
   /   /   /   /{
   /   /   /   /  'slide_type' : slide
   /   /   /   /}
   /   /   /}
   /   /  'outputs' :
   /   /   /[
   /   /   /  0 :
   /   /   /   /{
   /   /   /   /  'output_type' : stream
   /   /   /   /  'stream' : stdout
   /   /   /   /  'text' : ['Doer l.132 : DoerStr is Maker\n', 'DoStr is
Make\n', 'DoMethodStr is make\n', 'DoingStr is Making\n', 'DoneStr is Made\n',
'\n', 'Doer l.132 : DoerStr is Builder\n', 'DoStr is Build\n', 'DoMethodStr is
build\n', 'DoingStr is Building\n', 'DoneStr is Built\n', '\n', 'Before make,
MyBuilder is \n', '< (BuilderClass), 4466182800>\n', '   /{ \n', "   /
'<Base><Class>MadeMyInt' : 0\n", "   /  '<Base><Class>MakingMyFloat' : 0.0\n", "
/  '<New><Instance>IdStr' : 4466182800\n", '   /}\n', 'l 35\n', 'In the switch
function \n', '_KwargVariablesDict is \n', "{'BindObserveWrapMethodStr':
'watch_superMimic_switch_watch_superDo_make', 'WatchDoBoolKeyStr':
'WatchMakeWithBuilderBool', 'BindDoClassStr': 'BuilderClass'}\n", '\n', 'I am in
the mimic_make of the Builder\n', 'l 35\n', 'In the switch function \n',
'_KwargVariablesDict is \n', "{'BindObserveWrapMethodStr': 'watch_superDo_make',
'WatchDoBoolKeyStr': 'WatchMakeWithMakerBool', 'BindDoClassStr':
'MakerClass'}\n", '\n', 'I am in the do_make of the Maker\n', 'After the first
make, MyBuilder is \n', '< (BuilderClass), 4466182800>\n', '   /{ \n', "   /
'<New><Instance>IdStr' : 4466182800\n", "   /
'<New><Instance>WatchMakeWithBuilderBool' : True\n", "   /
'<Spe><Instance>MadeMyInt' : 13\n", "   /  '<Spe><Instance>MakingMyFloat' :
3.0\n", "   /  '<Spe><Instance>_WatchMakeWithMakerBool' : True\n", '   /}\n', 'l
35\n', 'In the switch function \n', '_KwargVariablesDict is \n',
"{'BindObserveWrapMethodStr': 'watch_superMimic_switch_watch_superDo_make',
'WatchDoBoolKeyStr': 'WatchMakeWithBuilderBool', 'BindDoClassStr':
'BuilderClass'}\n", '\n', 'After the second make, MyBuilder is \n', '<
(BuilderClass), 4466182800>\n', '   /{ \n', "   /  '<New><Instance>IdStr' :
4466182800\n", "   /  '<New><Instance>WatchMakeWithBuilderBool' : True\n", "   /
'<Spe><Instance>MadeMyInt' : 13\n", "   /  '<Spe><Instance>MakingMyFloat' :
3.0\n", "   /  '<Spe><Instance>_WatchMakeWithMakerBool' : True\n", '   /}\n',
'Now we reboot\n', 'After the reboot, MyBuilder is \n', '< (BuilderClass),
4466182800>\n', '   /{ \n', "   /  '<New><Instance>IdStr' : 4466182800\n", "   /
'<New><Instance>WatchMakeWithBuilderBool' : False\n", "   /
'<Spe><Instance>MadeMyInt' : 0\n", "   /  '<Spe><Instance>MakingMyFloat' :
3.0\n", "   /  '<Spe><Instance>_WatchMakeWithMakerBool' : False\n", '   /}\n',
'l 35\n', 'In the switch function \n', '_KwargVariablesDict is \n',
"{'BindObserveWrapMethodStr': 'watch_superMimic_switch_watch_superDo_make',
'WatchDoBoolKeyStr': 'WatchMakeWithBuilderBool', 'BindDoClassStr':
'BuilderClass'}\n", '\n', 'I am in the mimic_make of the Builder\n', 'l 35\n',
'In the switch function \n', '_KwargVariablesDict is \n',
"{'BindObserveWrapMethodStr': 'watch_superDo_make', 'WatchDoBoolKeyStr':
'WatchMakeWithMakerBool', 'BindDoClassStr': 'MakerClass'}\n", '\n', 'I am in the
do_make of the Maker\n', '\n', '\n', '*****Start of the Attest *****\n', '\n',
'MyBuilder is < (BuilderClass), 4466182800>\n', '   /{ \n', "   /
'<New><Instance>IdStr' : 4466182800\n", "   /
'<New><Instance>WatchMakeWithBuilderBool' : True\n", "   /
'<Spe><Instance>MadeMyInt' : 18\n", "   /  '<Spe><Instance>MakingMyFloat' :
8.0\n", "   /  '<Spe><Instance>RebootedWatchBoolKeyStrsList' :
['WatchMakeWithBuilderBool', '_WatchMakeWithMakerBool']\n", "   /
'<Spe><Instance>_WatchMakeWithMakerBool' : True\n", '   /}\n', '\n', '*****End
of the Attest *****\n', '\n', '\n']
   /   /   /   /}
   /   /   /]
   /   /  'prompt_number' : 0
   /   /}
   /  '<Spe><Instance>CelledOutputStr' : Doer l.132 : DoerStr is Maker
DoStr is Make
DoMethodStr is make
DoingStr is Making
DoneStr is Made

Doer l.132 : DoerStr is Builder
DoStr is Build
DoMethodStr is build
DoingStr is Building
DoneStr is Built

Before make, MyBuilder is
< (BuilderClass), 4466182800>
   /{
   /  '<Base><Class>MadeMyInt' : 0
   /  '<Base><Class>MakingMyFloat' : 0.0
   /  '<New><Instance>IdStr' : 4466182800
   /}
l 35
In the switch function
_KwargVariablesDict is
{'BindObserveWrapMethodStr': 'watch_superMimic_switch_watch_superDo_make',
'WatchDoBoolKeyStr': 'WatchMakeWithBuilderBool', 'BindDoClassStr':
'BuilderClass'}

I am in the mimic_make of the Builder
l 35
In the switch function
_KwargVariablesDict is
{'BindObserveWrapMethodStr': 'watch_superDo_make', 'WatchDoBoolKeyStr':
'WatchMakeWithMakerBool', 'BindDoClassStr': 'MakerClass'}

I am in the do_make of the Maker
After the first make, MyBuilder is
< (BuilderClass), 4466182800>
   /{
   /  '<New><Instance>IdStr' : 4466182800
   /  '<New><Instance>WatchMakeWithBuilderBool' : True
   /  '<Spe><Instance>MadeMyInt' : 13
   /  '<Spe><Instance>MakingMyFloat' : 3.0
   /  '<Spe><Instance>_WatchMakeWithMakerBool' : True
   /}
l 35
In the switch function
_KwargVariablesDict is
{'BindObserveWrapMethodStr': 'watch_superMimic_switch_watch_superDo_make',
'WatchDoBoolKeyStr': 'WatchMakeWithBuilderBool', 'BindDoClassStr':
'BuilderClass'}

After the second make, MyBuilder is
< (BuilderClass), 4466182800>
   /{
   /  '<New><Instance>IdStr' : 4466182800
   /  '<New><Instance>WatchMakeWithBuilderBool' : True
   /  '<Spe><Instance>MadeMyInt' : 13
   /  '<Spe><Instance>MakingMyFloat' : 3.0
   /  '<Spe><Instance>_WatchMakeWithMakerBool' : True
   /}
Now we reboot
After the reboot, MyBuilder is
< (BuilderClass), 4466182800>
   /{
   /  '<New><Instance>IdStr' : 4466182800
   /  '<New><Instance>WatchMakeWithBuilderBool' : False
   /  '<Spe><Instance>MadeMyInt' : 0
   /  '<Spe><Instance>MakingMyFloat' : 3.0
   /  '<Spe><Instance>_WatchMakeWithMakerBool' : False
   /}
l 35
In the switch function
_KwargVariablesDict is
{'BindObserveWrapMethodStr': 'watch_superMimic_switch_watch_superDo_make',
'WatchDoBoolKeyStr': 'WatchMakeWithBuilderBool', 'BindDoClassStr':
'BuilderClass'}

I am in the mimic_make of the Builder
l 35
In the switch function
_KwargVariablesDict is
{'BindObserveWrapMethodStr': 'watch_superDo_make', 'WatchDoBoolKeyStr':
'WatchMakeWithMakerBool', 'BindDoClassStr': 'MakerClass'}

I am in the do_make of the Maker


*****Start of the Attest *****

MyBuilder is < (BuilderClass), 4466182800>
   /{
   /  '<New><Instance>IdStr' : 4466182800
   /  '<New><Instance>WatchMakeWithBuilderBool' : True
   /  '<Spe><Instance>MadeMyInt' : 18
   /  '<Spe><Instance>MakingMyFloat' : 8.0
   /  '<Spe><Instance>RebootedWatchBoolKeyStrsList' :
['WatchMakeWithBuilderBool', '_WatchMakeWithMakerBool']
   /  '<Spe><Instance>_WatchMakeWithMakerBool' : True
   /}

*****End of the Attest *****


   /  '<Spe><Instance>CellingScriptStr' : Python
   /  '<Spe><Instance>CellingTextStr' : #ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Classer
from ShareYourSystem.Objects import Rebooter

#Definition
@Classer.ClasserClass(**
{
        'ClassingSwitchMethodStrsList':['make']
})
class MakerClass(Rebooter.RebooterClass):

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
                Rebooter.RebooterClass.__init__(self,**_KwarVariablesDict)

        #<DefineDoMethod>
        def do_make(self):

                #print
                print('I am in the do_make of the Maker')

                #cast
                self.MadeMyInt=int(self.MakingMyFloat)

#Definition
@Classer.ClasserClass(**{
        'ClassingSwitchMethodStrsList':["make"]
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

        #<DefineDoMethod>
        def do_build(self):
                pass


#Definition an instance
MyBuilder=BuilderClass()

#Print
print('Before make, MyBuilder is ')
SYS._print(MyBuilder,**{
        'RepresentingKeyStrsList':[
        'MakingMyFloat',
        'MadeMyInt',
        ]
})

#make once
MyBuilder.make(3.)

#Print
print('After the first make, MyBuilder is ')
SYS._print(MyBuilder,**{
        'RepresentingKeyStrsList':[
        'MakingMyFloat',
        'MadeMyInt',
        '_WatchMakeWithMakerBool'
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
        '_WatchMakeWithMakerBool'
        ]
})


#make again
print('Now we reboot')
MyBuilder.reboot(['Make'])

#Print
print('After the reboot, MyBuilder is ')
SYS._print(MyBuilder,**{
        'RepresentingKeyStrsList':[
        'MakingMyFloat',
        'MadeMyInt',
        '_WatchMakeWithMakerBool'
        ]
})

#make again
MyBuilder.make(8.)

#Definition the AttestedStr
SYS._attest(
        [
                'MyBuilder is '+SYS._str(
                MyBuilder,
                **{
                        'RepresentingAlineaIsBool':False,
                        'RepresentingKeyStrsList':[
                                'MakingMyFloat',
                                'MadeMyInt',
                                '_WatchMakeWithMakerBool',
                                'RebootedWatchBoolKeyStrsList'
                        ]
                        }
                )
        ]
)
   /}

*****End of the Attest *****



```

