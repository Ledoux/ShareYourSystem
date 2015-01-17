
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


A Visiter

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Walkers.Cumulater"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>

from ShareYourSystem.Noders import Noder
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class VisiterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'VisitingCollectionStrsList',
									'VisitingBeforeUpdateList',
									'VisitingAfterUpdateList'
								]

	def default_init(self,
				_VisitingCollectionStrsList=None,
				_VisitingBeforeUpdateList=None,
				_VisitingAfterUpdateList=None,
				**_KwargVariablesDict
			):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_visit(self):
			
		#Walk inside the group in order to parent
		self.walk(
					{
						'BeforeUpdateList':self.VisitingBeforeUpdateList,
						'AfterUpdateList':self.VisitingAfterUpdateList,
						'GatherVariablesList':map(
								lambda __NodeCollectionStr:
								Noder.NodingPrefixGetStr+__NodeCollectionStr+Noder.NodingSuffixGetStr,
								self.VisitingCollectionStrsList
							)
					}
				)
		

#</DefineClass>

```

<small>
View the Visiter sources on <a href="https://github.com/Ledoux/ShareYourSystem/tree/master/Pythonlogy/ShareYourSystem/Walkers/Visiter" target="_blank">Github</a>
</small>

