

<!--
FrozenIsBool False
-->

#Rater

##Doc
----


>
> A Rater
>
>

----

<small>
View the Rater notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyours
ystem.ouvaton.org/Rater.ipynb)
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


A Rater

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Simulaters.Dynamizer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<DefineClass>
@DecorationClass()
class RaterClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'RatingMatrixStr',
'RatedPreStr'
                                                                ]

        def default_init(self,
                                                _RatingMatrixStr='J',
                                                _RatingConstantTimeFloat='tau',
                                                _RatedPreStr="",
                                                **_KwargVariablesDict
                                        ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_rate(
                                self,
                        ):


                #debug
                '''
                self.debug(('self.',self,[

                                        ]))
                '''

                #add the connection variable
                self.RatedPreStr+=self.RatingMatrixStr+self.DynamizingTraceStr

                #add the constant time
                #self.RatedPreStr+=')/('+self.RatingConstantTimeStr+'*'+self.Dyn
amizingTimeDimensionStr+')'
                self.RatedPreStr+=')/('+self.RatingConstantTimeStr+')'

        def mimic_dynamize(self):

                #parent method
                BaseClass.dynamize(self)

                #rate first
                self.rate()

                #add in the DynamizedPreStr
                if self.DynamizedPreStr!='(':
                        self.DynamizedPreStr+=' + '
                self.DynamizedPreStr+=self.RatedPreStr

                #Check
                if self.RatingMatrixStr!="":
self.DynamizedParamStr+=self.RatingMatrixStr+self.DynamizingTraceStr+' :
'+self.DynamizingTraceDimensionStr+'\n'

                #Check
                if self.RatingConstantTimeStr!="":
                        self.DynamizedParamStr+=self.RatingConstantTimeStr+' :
'+self.DynamizingTimeDimensionStr+'\n'

                #set
                self.DynamizingRateThresholdFunction=lambda _VariableFloat
:(_VariableFloat<=0.)

#</DefineClass>

```

<small>
View the Rater sources on <a href="https://github.com/Ledoux/ShareYourSystem/tre
e/master/Pythonlogy/ShareYourSystem/Simulaters/Rater" target="_blank">Github</a>
</small>

