

<!--
FrozenIsBool False
-->

#Populater

##Doc
----


>
> A Populater
>
>

----

<small>
View the Populater notebook on [NbViewer](http://nbviewer.ipython.org/url/sharey
oursystem.ouvaton.org/Populater.ipynb)
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


A Populater

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Simulaters.Moniter"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<DefineClass>
@DecorationClass()
class PopulaterClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'PopulatingUnitsInt',
'PopulatingEquationStr',
'PopulatingThresholdStr',
'PopulatingResetStr',
'PopulatingCommunicationDictsList'
                                                        ]

        def default_init(self,
                                                _PopulatingUnitsInt=0,
                                                _PopulatingEquationStr='''
                                                        dv/dt =
(ge+gi-(v+49*mV))/(20*ms) : volt
                                                        dge/dt = -ge/(5*ms) :
volt
                                                        dgi/dt = -gi/(10*ms) :
volt
                                                ''',
_PopulatingThresholdStr='v>-50*mV',
                                                _PopulatingResetStr='v=-60*mV',
_PopulatingCommunicationDictsList=None,
                                                **_KwargVariablesDict
                                        ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_populate(self):

                #debug
                '''
                self.debug(('self.',self,[

                                        ]))
                '''

                #monit first
                self.monit()


                #Return self
                #return self

#</DefineClass>

```

<small>
View the Populater sources on <a href="https://github.com/Ledoux/ShareYourSystem
/tree/master/Pythonlogy/ShareYourSystem/Simulaters/Populater"
target="_blank">Github</a>
</small>

