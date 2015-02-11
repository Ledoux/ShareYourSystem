

<!--
FrozenIsBool False
-->

#Deleter

##Doc
----


>
> A Deleter has a __delitem__ method for deleting things in the
<InstanceVariable>.__dict__
>
>

----

<small>
View the Deleter notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyou
rsystem.ouvaton.org/Deleter.ipynb)
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


A Deleter has a __delitem__ method for deleting things in the
<InstanceVariable>.__dict__

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Setter"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class DeleterClass(BaseClass):

        def default_init(self,
                                                _DeletingKeyVariable=None,
                                                **_KwargVariablesDict
                                        ):
                """ """

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        #@Argumenter.ArgumenterClass(**{'ArgumentingDoStr':"Delete"})
        def __delitem__(self,_KeyVariable,**_KwargVariablesDict):
                """ """

                #debug
                '''
                self.debug(('self.',self,['DeletingKeyVariable']))
                '''

                #Delete
                self.delete(_KeyVariable)

                #set
                return self

        def do_delete(self):
                """ """

                #Do the minimal delitem
                if type(self.DeletingKeyVariable) in [str,unicode]:

                        #Del Safely the Value
                        if self.DeletingKeyVariable in self.__dict__:
                                del self.__dict__[self.DeletingKeyVariable]

#</DefineClass>



```

<small>
View the Deleter sources on <a href="https://github.com/Ledoux/ShareYourSystem/t
ree/master/Pythonlogy/ShareYourSystem/Itemizers/Deleter"
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
from ShareYourSystem.Standards.Itemizers import Deleter

#Definition a Deleter
MyDeleter=Deleter.DeleterClass().__setitem__('MyInt',0).__delitem__('MyInt')

#Definition the AttestedStr
SYS._attest(
    [
    'MyDeleter is '+SYS._str(
            MyDeleter,
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


*****Start of the Attest *****

MyDeleter is < (DeleterClass), 4540871120>
   /{
   /  '<New><Instance>IdInt' : 4540871120
   /}

*****End of the Attest *****



```

