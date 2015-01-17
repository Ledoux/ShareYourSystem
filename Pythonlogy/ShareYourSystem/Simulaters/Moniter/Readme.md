

<!--
FrozenIsBool False
-->

#Moniter

##Doc
----


>
> A Moniter
>
>

----

<small>
View the Moniter notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyou
rsystem.ouvaton.org/Moniter.ipynb)
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


A Moniter

"""


#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Simulaters.Runner"
DecorationModuleStr="ShareYourSystem.Classors.Representer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineDoStrsList>
DoStrsList=["Moniter","Monit","Monitering","Monitered"]
#<DefineDoStrsList>

#<DefineClass>
@DecorationClass()
class MoniterClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'MonitoringTrackTuplesList'
                                                                ]

        def default_init(self,
                                                _MoniteringTrackTuplesList=None,
                                                **_KwargVariablesDict
                                        ):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        #<DefineDoMethod>
        def do_monit(self):

                pass

#</DefineClass>


```

<small>
View the Moniter sources on <a href="https://github.com/Ledoux/ShareYourSystem/t
ree/master/Pythonlogy/ShareYourSystem/Simulaters/Moniter"
target="_blank">Github</a>
</small>


