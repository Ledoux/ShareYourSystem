
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


A Parenter completes the list of grand-parent nodes that 
a child node could have. It acts only at one level.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Noders.Distinguisher"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
from ShareYourSystem.Itemizers import Pather
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass(
	**{'ClassingSwitchMethodStrsList':['parent']}
)
class ParenterClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
								'ParentingWalkBool',
								'ParentedDeriveParentersList',
								'ParentedNodeCollectionStrsList',
								'ParentedPathStr'
							]

	def default_init(self,
				_ParentingWalkBool=True,
				_ParentedDeriveParentersList=None,
				_ParentedNodeCollectionStrsList=None,
				_ParentedPathStr="",
				**_KwargVariablesDict):	

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_parent(self):

		#debug
		'''
		self.debug(('self.',self,['ParentingNodeStr','NodePointDeriveNoder']))
		'''

		#Check of a parent pointer
		if self.NodePointDeriveNoder!=None:

			#debug
			'''
			self.debug('We are going to node the parent pointer')
			'''

			#Parent the parent maybe
			if self.ParentingWalkBool:

				#parent the parent
				self.NodePointDeriveNoder.parent()

			#set
			self.ParentedDeriveParentersList=[self.NodePointDeriveNoder
			]+self.NodePointDeriveNoder.ParentedDeriveParentersList

			self.ParentedNodeCollectionStrsList=[self.NodedCollectionStr
			]+self.NodePointDeriveNoder.ParentedNodeCollectionStrsList
			self.ParentedNodeCollectionStrsList.reverse()

			#definition
			ParentedPathStrsList=map(
					lambda __ParentedDeriveParenter:
					__ParentedDeriveParenter.NodeKeyStr,
					self.ParentedDeriveParentersList
				)
			ParentedPathStrsList.reverse()
			
			#Debug
			'''
			self.debug('ParentedPathStrsList is '+str(ParentedPathStrsList))
			'''
			
			#set
			self.ParentedPathStr=Pather.PathingPrefixStr.join(ParentedPathStrsList)

		#Return self
		#return self

#</DefineClass>


```

<small>
View the Parenter sources on <a href="https://github.com/Ledoux/ShareYourSystem/tree/master/Pythonlogy/ShareYourSystem/Noders/Parenter" target="_blank">Github</a>
</small>

