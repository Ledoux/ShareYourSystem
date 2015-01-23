
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


The Object defines the first class for augmenting new-style object classes

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr=""
DecorationModuleStr=""
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import sys
#</ImportSpecificModules>

#<DefineClass>
#@DecorationClass
class ObjectClass(object):

	#Definition 	
	IdInt=-1
	SysStr=""

#</DefineClass>

#set
ObjectClass.NameStr="Object"
SYS.ObjectClass=ObjectClass
SYS.Object=sys.modules[ObjectClass.__module__]

```

<small>
View the Object sources on <a href="https://github.com/Ledoux/ShareYourSystem/tree/master/Pythonlogy/ShareYourSystem/Objects/Object" target="_blank">Github</a>
</small>

