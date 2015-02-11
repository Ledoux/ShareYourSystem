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
from ShareYourSystem.Standards.Teamers import Manager,Teamer
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
		self.debug(('self.',self,[
					'ManagementPointDeriveTeamer',
					'NameStr'
				]))

		#Check
		if self.ManagementPointDeriveTeamer!=None:

			#debug
			'''
			self.debug('We are going to parent the parent teamer')
			'''
			
			#Parent the parent maybe
			if self.ParentingClimbBool:

				#parent the parent
				self.ManagementPointDeriveTeamer.parent(
						self.ParentingTopGetVariable,
						self.ParentingClimbBool
					)

			#set
			self.ParentedDeriveTeamersList=[
				self.ManagementPointDeriveTeamer
			]+self.ManagementPointDeriveTeamer.ParentedDeriveTeamersList

			self.ParentedManagerKeyStrsList=[
				self.ManagementTeamKeyStr
			]+self.ManagementPointDeriveTeamer.ParentedManagerKeyStrsList
			self.ParentedManagerKeyStrsList.reverse()

			#definition
			ParentedTeamerPathStrsList=map(
					lambda __ParentedDeriveTeamer:
					__ParentedDeriveTeamer.ManagementKeyStr,
					self.ParentedDeriveTeamersList
				)
			ParentedTeamerPathStrsList.reverse()

			#definition
			ParentedTotalPathTuplesList=map(
					lambda __ParentedDeriveTeamer:
					(
						Manager.ManagementChildPrefixStr+__ParentedDeriveTeamer.ManagementTeamKeyStr,
						Teamer.TeamChildPrefixStr+__ParentedDeriveTeamer.ManagementKeyStr
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
			self.apply(
						'map*set',
						zip(
							self.ParentingTopGetVariable,
							self.ParentedTopDeriveTeamerVariable.apply(
									'map*get',
									self.ParentingTopGetVariable
								)
							)
					)

		else:
			self.ParentedTopDeriveTeamerVariable=self

#</DefineClass>

#Set
SYS.ManagerClass.ManagingValueClass=ParenterClass
