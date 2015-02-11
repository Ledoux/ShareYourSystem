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
BaseModuleStr="ShareYourSystem.Standards.Teamers.Teamer"
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
								'ParentingTopGetVariable',
								'ParentingClimbBool',
								'ParentedDeriveTeamersList',
								'ParentedManagerKeyStrsList',
								'ParentedTeamerPathStr',
								'ParentedManagerPathStr',
								'ParentedTotalPathStr',
								'ParentedTopDeriveTeamerVariable'
							]

	def default_init(self,
				_ParentingTopGetVariable=None,
				_ParentingClimbBool=True,
				_ParentedDeriveTeamersList=None,
				_ParentedManagerKeyStrsList=None,
				_ParentedTeamerPathStr="",
				_ParentedManagerPathStr="",
				_ParentedTotalPathStr="",
				_ParentedTopDeriveTeamerVariable=None,
				**_KwargVariablesDict
			):	

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
			if self.ParentingClimbBool:

				#parent the parent
				self.NodePointDeriveNoder.parent(
						self.ParentingTopGetVariable,
						self.ParentingClimbBool
					)

			#set
			self.ParentedDeriveTeamersList=[self.NodePointDeriveNoder
			]+self.NodePointDeriveNoder.ParentedDeriveTeamersList

			self.ParentedManagerKeyStrsList=[self.NodedCollectionStr
			]+self.NodePointDeriveNoder.ParentedManagerKeyStrsList
			self.ParentedManagerKeyStrsList.reverse()

			#definition
			ParentedTeamerPathStrsList=map(
					lambda __ParentedDeriveTeamer:
					__ParentedDeriveTeamer.NodeKeyStr,
					self.ParentedDeriveTeamersList
				)
			ParentedTeamerPathStrsList.reverse()

			#definition
			ParentedTotalPathTuplesList=map(
					lambda __ParentedDeriveTeamer:
					(
						Noder.NodingPrefixGetStr+__ParentedDeriveTeamer.NodeCollectionStr+Noder.NodingSuffixGetStr,
						__ParentedDeriveTeamer.NodeKeyStr
					),
					self.ParentedDeriveTeamersList
				)
			ParentedTotalPathTuplesList.reverse()

			
			#Debug
			'''
			self.debug('ParentedTotalPathTuplesList is '+str(ParentedTotalPathTuplesList))
			'''
			
			#set
			self.ParentedTeamerPathStr=Pather.PathPrefixStr.join(
				SYS.unzip(ParentedTotalPathTuplesList,[1])
			)
			self.ParentedManagerPathStr=Pather.PathPrefixStr.join(
				SYS.unzip(ParentedTotalPathTuplesList,[0])
			)
			self.ParentedTotalPathStr=Pather.PathPrefixStr.join(
				map(
					lambda __ParentedTotalPathTuple:
					__ParentedTotalPathTuple[0]+__ParentedTotalPathTuple[1],
					ParentedTotalPathTuplesList
				)
			)

			#Check
			if len(self.ParentedDeriveTeamersList)>0:
				self.ParentedTopDeriveTeamerVariable=self.ParentedDeriveTeamersList[-1]
			else:
				self.ParentedTopDeriveTeamerVariable=self

			#Link
			self.update(
							zip(
								self.ParentingTopGetVariable,
								self.ParentedTopDeriveTeamerVariable.pick(
										self.ParentingTopGetVariable
									)
								)
						)

		else:
			self.ParentedTopDeriveTeamerVariable=self

#</DefineClass>

