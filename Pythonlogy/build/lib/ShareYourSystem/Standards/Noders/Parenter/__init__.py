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
BaseModuleStr="ShareYourSystem.Standards.Noders.Distinguisher"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
from ShareYourSystem.Standards.Itemizers import Pather
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass(
	**{'ClassingSwitchMethodStrsList':['parent']}
)
class ParenterClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
								'ParentingTopPickVariablesList',
								'ParentingWalkBool',
								'ParentedDeriveParentersList',
								'ParentedNodeCollectionStrsList',
								'ParentedPathStr',
								'ParentedTopDeriveParenterVariable'
							]

	def default_init(self,
				_ParentingTopPickVariablesList=None,
				_ParentingWalkBool=True,
				_ParentedDeriveParentersList=None,
				_ParentedNodeCollectionStrsList=None,
				_ParentedPathStr="",
				_ParentedTopDeriveParenterVariable=None,
				**_KwargVariablesDict):	

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_parent(self):

		#debug
		'''
		self.debug(('self.',self,[
					
				]))
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
				self.NodePointDeriveNoder.parent(
						self.ParentingTopPickVariablesList,
						self.ParentingWalkBool
					)

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


			#Check
			if len(self.ParentedDeriveParentersList)>0:
				self.ParentedTopDeriveParenterVariable=self.ParentedDeriveParentersList[-1]
			else:
				self.ParentedTopDeriveParenterVariable=self

			#Link
			self.update(
							zip(
								self.ParentingTopPickVariablesList,
								self.ParentedTopDeriveParenterVariable.pick(
										self.ParentingTopPickVariablesList
									)
								)
						)

		else:
			self.ParentedTopDeriveParenterVariable=self

#</DefineClass>

