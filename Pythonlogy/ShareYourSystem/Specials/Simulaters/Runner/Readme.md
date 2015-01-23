

<!--
FrozenIsBool False
-->

#Runner

##Doc
----


>
> A Runner
>
>

----

<small>
View the Runner notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyour
system.ouvaton.org/Runner.ipynb)
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


A Runner

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Specials.Simulaters.Simulater"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class RunnerClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'RunningTimeFloat'
                                                                ]

        def default_init(self,
                                                _RunningTimeFloat=0.,
                                                **_KwargVariablesDict
                                        ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_run(
                                self
                        ):

                pass

                #Return self
                #return self

#</DefineClass>

```

<small>
View the Runner sources on <a href="https://github.com/Ledoux/ShareYourSystem/tr
ee/master/Pythonlogy/ShareYourSystem/Simulaters/Runner"
target="_blank">Github</a>
</small>


