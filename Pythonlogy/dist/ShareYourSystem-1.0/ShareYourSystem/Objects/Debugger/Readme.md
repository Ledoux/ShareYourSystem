
#Debugger


@Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



The Debugger from a DebuggerClass instance has a debug function that prints in
the console a state (to be defined) of the environnement. This print can be
indented with the number of function frames from  which the process has passed
through, for a nicer visualisation of the kind of hooked functions. More options
in the display can be possible like the number of the line in the corresponding
code or the pick of KeyStrs helping for precising the debugging instance
identity.





<!--
FrozenIsBool False
-->

View the Debugger sources on [Github](https://github.com/Ledoux/ShareYourSystem/
tree/master/ShareYourSystem/Objects/Installer)




<!---
FrozenIsBool True
-->

##Example

Let's create an empty class, which will automatically receive
special attributes from the decorating ClassorClass,
specially the NameStr, that should be the ClassStr
without the TypeStr in the end.

```python
# ImportModules
from ShareYourSystem.Classors import Doer
from ShareYourSystem.Classors.Representer import _print
from ShareYourSystem.Objects import Debugger

#Definition a debugging make class
@Doer.DoerClass()
class MakerClass(Debugger.DebuggerClass):

    def make1(self):

        #debug
        self.debug('I am in the make1 method')

        #Call the make2 method
        self.make2()

        #debug
        self.debug('I am back in the make1 method')

    def make2(self):

        #debug
        self.debug('I am in the make2 method')

        #Call the make3 method
        self.make3()

        #debug
        self.debug('I am back in the make2 method')

    def make3(self):

        #debug
        self.debug('I am in the make3 method')

        #Call the make4 method
        self.make4()

    def make4(self):

        #debug
        self.debug('I am in the make4 method')

        #debug
        self.debug('I am still in the make4 method')

#Call the make1
MyMaker=MakerClass()
MyMaker.make1()

#Call the make1 but with also showing the frame of the argumentinf function
MyMaker.DebuggingNotFrameFunctionStrsList=[]
MyMaker.make1()


```


```console
>>>
Doer l.132 : DoerStr is Maker
DoStr is Make
DoMethodStr is make
DoingStr is Making
DoneStr is Made


                                                    xxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
////////////////////////////////
                                                    Doer/__init__.py do
                                                    From <string> superDo_debug
| <string> make1 | <string> <module> | <string> <module> | site-packages/six.py
exec_ | Celler/__init__.py do_cell | Doer/__init__.py do | <string> superDo_cell
| Watcher/__init__.py watch | <string> watch_superDo_cell |
Notebooker/__init__.py do_notebook | Doer/__init__.py do | <string>
superDo_notebook | Watcher/__init__.py watch | <string> watch_superDo_notebook |
Readmer/__init__.py do_readme | Doer/__init__.py do | <string> superDo_readme |
Watcher/__init__.py watch | <string> watch_superDo_readme |
python2.7/posixpath.py walk | python2.7/posixpath.py walk | Directer/__init__.py
do_direct | Doer/__init__.py do | <string> superDo_direct | Watcher/__init__.py
watch | <string> watch_superDo_direct | Installer/__init__.py do_install |
Doer/__init__.py do | <string> superDo_install | Watcher/__init__.py watch |
<string> watch_superDo_install | ShareYourSystem/Install.py <module>
////////////////////////////////

                                                    l.180 :
                                                    *****
                                                    I am with []
                                                    *****
                                                    I am in the make1 method
                                                    xxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                                        xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
////////////////////////////////
                                                        Doer/__init__.py do
                                                        From <string>
superDo_debug | <string> make2 | <string> make1 | <string> <module> | <string>
<module> | site-packages/six.py exec_ | Celler/__init__.py do_cell |
Doer/__init__.py do | <string> superDo_cell | Watcher/__init__.py watch |
<string> watch_superDo_cell | Notebooker/__init__.py do_notebook |
Doer/__init__.py do | <string> superDo_notebook | Watcher/__init__.py watch |
<string> watch_superDo_notebook | Readmer/__init__.py do_readme |
Doer/__init__.py do | <string> superDo_readme | Watcher/__init__.py watch |
<string> watch_superDo_readme | python2.7/posixpath.py walk |
python2.7/posixpath.py walk | Directer/__init__.py do_direct | Doer/__init__.py
do | <string> superDo_direct | Watcher/__init__.py watch | <string>
watch_superDo_direct | Installer/__init__.py do_install | Doer/__init__.py do |
<string> superDo_install | Watcher/__init__.py watch | <string>
watch_superDo_install | ShareYourSystem/Install.py <module>
////////////////////////////////

                                                        l.180 :
                                                        *****
                                                        I am with []
                                                        *****
                                                        I am in the make2 method
                                                        xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                                            xxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
////////////////////////////////
                                                            Doer/__init__.py do
                                                            From <string>
superDo_debug | <string> make3 | <string> make2 | <string> make1 | <string>
<module> | <string> <module> | site-packages/six.py exec_ | Celler/__init__.py
do_cell | Doer/__init__.py do | <string> superDo_cell | Watcher/__init__.py
watch | <string> watch_superDo_cell | Notebooker/__init__.py do_notebook |
Doer/__init__.py do | <string> superDo_notebook | Watcher/__init__.py watch |
<string> watch_superDo_notebook | Readmer/__init__.py do_readme |
Doer/__init__.py do | <string> superDo_readme | Watcher/__init__.py watch |
<string> watch_superDo_readme | python2.7/posixpath.py walk |
python2.7/posixpath.py walk | Directer/__init__.py do_direct | Doer/__init__.py
do | <string> superDo_direct | Watcher/__init__.py watch | <string>
watch_superDo_direct | Installer/__init__.py do_install | Doer/__init__.py do |
<string> superDo_install | Watcher/__init__.py watch | <string>
watch_superDo_install | ShareYourSystem/Install.py <module>
////////////////////////////////

                                                            l.180 :
                                                            *****
                                                            I am with []
                                                            *****
                                                            I am in the make3
method
                                                            xxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                                                xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
////////////////////////////////
                                                                Doer/__init__.py
do
                                                                From <string>
superDo_debug | <string> make4 | <string> make3 | <string> make2 | <string>
make1 | <string> <module> | <string> <module> | site-packages/six.py exec_ |
Celler/__init__.py do_cell | Doer/__init__.py do | <string> superDo_cell |
Watcher/__init__.py watch | <string> watch_superDo_cell | Notebooker/__init__.py
do_notebook | Doer/__init__.py do | <string> superDo_notebook |
Watcher/__init__.py watch | <string> watch_superDo_notebook |
Readmer/__init__.py do_readme | Doer/__init__.py do | <string> superDo_readme |
Watcher/__init__.py watch | <string> watch_superDo_readme |
python2.7/posixpath.py walk | python2.7/posixpath.py walk | Directer/__init__.py
do_direct | Doer/__init__.py do | <string> superDo_direct | Watcher/__init__.py
watch | <string> watch_superDo_direct | Installer/__init__.py do_install |
Doer/__init__.py do | <string> superDo_install | Watcher/__init__.py watch |
<string> watch_superDo_install | ShareYourSystem/Install.py <module>
////////////////////////////////

                                                                l.180 :
                                                                *****
                                                                I am with []
                                                                *****
                                                                I am in the
make4 method
                                                                xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                                                xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
////////////////////////////////
                                                                Doer/__init__.py
do
                                                                From <string>
superDo_debug | <string> make4 | <string> make3 | <string> make2 | <string>
make1 | <string> <module> | <string> <module> | site-packages/six.py exec_ |
Celler/__init__.py do_cell | Doer/__init__.py do | <string> superDo_cell |
Watcher/__init__.py watch | <string> watch_superDo_cell | Notebooker/__init__.py
do_notebook | Doer/__init__.py do | <string> superDo_notebook |
Watcher/__init__.py watch | <string> watch_superDo_notebook |
Readmer/__init__.py do_readme | Doer/__init__.py do | <string> superDo_readme |
Watcher/__init__.py watch | <string> watch_superDo_readme |
python2.7/posixpath.py walk | python2.7/posixpath.py walk | Directer/__init__.py
do_direct | Doer/__init__.py do | <string> superDo_direct | Watcher/__init__.py
watch | <string> watch_superDo_direct | Installer/__init__.py do_install |
Doer/__init__.py do | <string> superDo_install | Watcher/__init__.py watch |
<string> watch_superDo_install | ShareYourSystem/Install.py <module>
////////////////////////////////

                                                                l.180 :
                                                                *****
                                                                I am with []
                                                                *****
                                                                I am still in
the make4 method
                                                                xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                                        xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
////////////////////////////////
                                                        Doer/__init__.py do
                                                        From <string>
superDo_debug | <string> make2 | <string> make1 | <string> <module> | <string>
<module> | site-packages/six.py exec_ | Celler/__init__.py do_cell |
Doer/__init__.py do | <string> superDo_cell | Watcher/__init__.py watch |
<string> watch_superDo_cell | Notebooker/__init__.py do_notebook |
Doer/__init__.py do | <string> superDo_notebook | Watcher/__init__.py watch |
<string> watch_superDo_notebook | Readmer/__init__.py do_readme |
Doer/__init__.py do | <string> superDo_readme | Watcher/__init__.py watch |
<string> watch_superDo_readme | python2.7/posixpath.py walk |
python2.7/posixpath.py walk | Directer/__init__.py do_direct | Doer/__init__.py
do | <string> superDo_direct | Watcher/__init__.py watch | <string>
watch_superDo_direct | Installer/__init__.py do_install | Doer/__init__.py do |
<string> superDo_install | Watcher/__init__.py watch | <string>
watch_superDo_install | ShareYourSystem/Install.py <module>
////////////////////////////////

                                                        l.180 :
                                                        *****
                                                        I am with []
                                                        *****
                                                        I am back in the make2
method
                                                        xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                                    xxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
////////////////////////////////
                                                    Doer/__init__.py do
                                                    From <string> superDo_debug
| <string> make1 | <string> <module> | <string> <module> | site-packages/six.py
exec_ | Celler/__init__.py do_cell | Doer/__init__.py do | <string> superDo_cell
| Watcher/__init__.py watch | <string> watch_superDo_cell |
Notebooker/__init__.py do_notebook | Doer/__init__.py do | <string>
superDo_notebook | Watcher/__init__.py watch | <string> watch_superDo_notebook |
Readmer/__init__.py do_readme | Doer/__init__.py do | <string> superDo_readme |
Watcher/__init__.py watch | <string> watch_superDo_readme |
python2.7/posixpath.py walk | python2.7/posixpath.py walk | Directer/__init__.py
do_direct | Doer/__init__.py do | <string> superDo_direct | Watcher/__init__.py
watch | <string> watch_superDo_direct | Installer/__init__.py do_install |
Doer/__init__.py do | <string> superDo_install | Watcher/__init__.py watch |
<string> watch_superDo_install | ShareYourSystem/Install.py <module>
////////////////////////////////

                                                    l.180 :
                                                    *****
                                                    I am with []
                                                    *****
                                                    I am back in the make1
method
                                                    xxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                                            xxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
////////////////////////////////
                                                            Doer/__init__.py do
                                                            From <string>
superDo_debug | <string> make1 | <string> <module> | <string> <module> | site-
packages/six.py exec_ | Celler/__init__.py do_cell | Doer/__init__.py do |
<string> superDo_cell | Watcher/__init__.py watch | <string> watch_superDo_cell
| Notebooker/__init__.py <lambda> | Notebooker/__init__.py do_notebook |
Doer/__init__.py do | <string> superDo_notebook | Watcher/__init__.py watch |
<string> watch_superDo_notebook | Readmer/__init__.py do_readme |
Doer/__init__.py do | <string> superDo_readme | Watcher/__init__.py watch |
<string> watch_superDo_readme | Installer/__init__.py <lambda> |
python2.7/posixpath.py walk | python2.7/posixpath.py walk | Directer/__init__.py
do_direct | Doer/__init__.py do | <string> superDo_direct | Watcher/__init__.py
watch | <string> watch_superDo_direct | Installer/__init__.py do_install |
Doer/__init__.py do | <string> superDo_install | Watcher/__init__.py watch |
<string> watch_superDo_install | ShareYourSystem/Install.py <module>
////////////////////////////////

                                                            l.180 :
                                                            *****
                                                            I am with []
                                                            *****
                                                            I am in the make1
method
                                                            xxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                                                xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
////////////////////////////////
                                                                Doer/__init__.py
do
                                                                From <string>
superDo_debug | <string> make2 | <string> make1 | <string> <module> | <string>
<module> | site-packages/six.py exec_ | Celler/__init__.py do_cell |
Doer/__init__.py do | <string> superDo_cell | Watcher/__init__.py watch |
<string> watch_superDo_cell | Notebooker/__init__.py <lambda> |
Notebooker/__init__.py do_notebook | Doer/__init__.py do | <string>
superDo_notebook | Watcher/__init__.py watch | <string> watch_superDo_notebook |
Readmer/__init__.py do_readme | Doer/__init__.py do | <string> superDo_readme |
Watcher/__init__.py watch | <string> watch_superDo_readme |
Installer/__init__.py <lambda> | python2.7/posixpath.py walk |
python2.7/posixpath.py walk | Directer/__init__.py do_direct | Doer/__init__.py
do | <string> superDo_direct | Watcher/__init__.py watch | <string>
watch_superDo_direct | Installer/__init__.py do_install | Doer/__init__.py do |
<string> superDo_install | Watcher/__init__.py watch | <string>
watch_superDo_install | ShareYourSystem/Install.py <module>
////////////////////////////////

                                                                l.180 :
                                                                *****
                                                                I am with []
                                                                *****
                                                                I am in the
make2 method
                                                                xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                                                    xxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
////////////////////////////////
Doer/__init__.py do
                                                                    From
<string> superDo_debug | <string> make3 | <string> make2 | <string> make1 |
<string> <module> | <string> <module> | site-packages/six.py exec_ |
Celler/__init__.py do_cell | Doer/__init__.py do | <string> superDo_cell |
Watcher/__init__.py watch | <string> watch_superDo_cell | Notebooker/__init__.py
<lambda> | Notebooker/__init__.py do_notebook | Doer/__init__.py do | <string>
superDo_notebook | Watcher/__init__.py watch | <string> watch_superDo_notebook |
Readmer/__init__.py do_readme | Doer/__init__.py do | <string> superDo_readme |
Watcher/__init__.py watch | <string> watch_superDo_readme |
Installer/__init__.py <lambda> | python2.7/posixpath.py walk |
python2.7/posixpath.py walk | Directer/__init__.py do_direct | Doer/__init__.py
do | <string> superDo_direct | Watcher/__init__.py watch | <string>
watch_superDo_direct | Installer/__init__.py do_install | Doer/__init__.py do |
<string> superDo_install | Watcher/__init__.py watch | <string>
watch_superDo_install | ShareYourSystem/Install.py <module>
////////////////////////////////

                                                                    l.180 :
                                                                    *****
                                                                    I am with []
                                                                    *****
                                                                    I am in the
make3 method
                                                                    xxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                                                        xxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxx
////////////////////////////////
Doer/__init__.py do
                                                                        From
<string> superDo_debug | <string> make4 | <string> make3 | <string> make2 |
<string> make1 | <string> <module> | <string> <module> | site-packages/six.py
exec_ | Celler/__init__.py do_cell | Doer/__init__.py do | <string> superDo_cell
| Watcher/__init__.py watch | <string> watch_superDo_cell |
Notebooker/__init__.py <lambda> | Notebooker/__init__.py do_notebook |
Doer/__init__.py do | <string> superDo_notebook | Watcher/__init__.py watch |
<string> watch_superDo_notebook | Readmer/__init__.py do_readme |
Doer/__init__.py do | <string> superDo_readme | Watcher/__init__.py watch |
<string> watch_superDo_readme | Installer/__init__.py <lambda> |
python2.7/posixpath.py walk | python2.7/posixpath.py walk | Directer/__init__.py
do_direct | Doer/__init__.py do | <string> superDo_direct | Watcher/__init__.py
watch | <string> watch_superDo_direct | Installer/__init__.py do_install |
Doer/__init__.py do | <string> superDo_install | Watcher/__init__.py watch |
<string> watch_superDo_install | ShareYourSystem/Install.py <module>
////////////////////////////////

                                                                        l.180 :
                                                                        *****
                                                                        I am
with []
                                                                        *****
                                                                        I am in
the make4 method
                                                                        xxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxx


                                                                        xxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxx
////////////////////////////////
Doer/__init__.py do
                                                                        From
<string> superDo_debug | <string> make4 | <string> make3 | <string> make2 |
<string> make1 | <string> <module> | <string> <module> | site-packages/six.py
exec_ | Celler/__init__.py do_cell | Doer/__init__.py do | <string> superDo_cell
| Watcher/__init__.py watch | <string> watch_superDo_cell |
Notebooker/__init__.py <lambda> | Notebooker/__init__.py do_notebook |
Doer/__init__.py do | <string> superDo_notebook | Watcher/__init__.py watch |
<string> watch_superDo_notebook | Readmer/__init__.py do_readme |
Doer/__init__.py do | <string> superDo_readme | Watcher/__init__.py watch |
<string> watch_superDo_readme | Installer/__init__.py <lambda> |
python2.7/posixpath.py walk | python2.7/posixpath.py walk | Directer/__init__.py
do_direct | Doer/__init__.py do | <string> superDo_direct | Watcher/__init__.py
watch | <string> watch_superDo_direct | Installer/__init__.py do_install |
Doer/__init__.py do | <string> superDo_install | Watcher/__init__.py watch |
<string> watch_superDo_install | ShareYourSystem/Install.py <module>
////////////////////////////////

                                                                        l.180 :
                                                                        *****
                                                                        I am
with []
                                                                        *****
                                                                        I am
still in the make4 method
                                                                        xxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxx


                                                                xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
////////////////////////////////
                                                                Doer/__init__.py
do
                                                                From <string>
superDo_debug | <string> make2 | <string> make1 | <string> <module> | <string>
<module> | site-packages/six.py exec_ | Celler/__init__.py do_cell |
Doer/__init__.py do | <string> superDo_cell | Watcher/__init__.py watch |
<string> watch_superDo_cell | Notebooker/__init__.py <lambda> |
Notebooker/__init__.py do_notebook | Doer/__init__.py do | <string>
superDo_notebook | Watcher/__init__.py watch | <string> watch_superDo_notebook |
Readmer/__init__.py do_readme | Doer/__init__.py do | <string> superDo_readme |
Watcher/__init__.py watch | <string> watch_superDo_readme |
Installer/__init__.py <lambda> | python2.7/posixpath.py walk |
python2.7/posixpath.py walk | Directer/__init__.py do_direct | Doer/__init__.py
do | <string> superDo_direct | Watcher/__init__.py watch | <string>
watch_superDo_direct | Installer/__init__.py do_install | Doer/__init__.py do |
<string> superDo_install | Watcher/__init__.py watch | <string>
watch_superDo_install | ShareYourSystem/Install.py <module>
////////////////////////////////

                                                                l.180 :
                                                                *****
                                                                I am with []
                                                                *****
                                                                I am back in the
make2 method
                                                                xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                                            xxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
////////////////////////////////
                                                            Doer/__init__.py do
                                                            From <string>
superDo_debug | <string> make1 | <string> <module> | <string> <module> | site-
packages/six.py exec_ | Celler/__init__.py do_cell | Doer/__init__.py do |
<string> superDo_cell | Watcher/__init__.py watch | <string> watch_superDo_cell
| Notebooker/__init__.py <lambda> | Notebooker/__init__.py do_notebook |
Doer/__init__.py do | <string> superDo_notebook | Watcher/__init__.py watch |
<string> watch_superDo_notebook | Readmer/__init__.py do_readme |
Doer/__init__.py do | <string> superDo_readme | Watcher/__init__.py watch |
<string> watch_superDo_readme | Installer/__init__.py <lambda> |
python2.7/posixpath.py walk | python2.7/posixpath.py walk | Directer/__init__.py
do_direct | Doer/__init__.py do | <string> superDo_direct | Watcher/__init__.py
watch | <string> watch_superDo_direct | Installer/__init__.py do_install |
Doer/__init__.py do | <string> superDo_install | Watcher/__init__.py watch |
<string> watch_superDo_install | ShareYourSystem/Install.py <module>
////////////////////////////////

                                                            l.180 :
                                                            *****
                                                            I am with []
                                                            *****
                                                            I am back in the
make1 method
                                                            xxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


```

