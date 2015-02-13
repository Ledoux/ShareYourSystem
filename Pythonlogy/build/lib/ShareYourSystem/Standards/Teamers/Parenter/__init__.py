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
								'ParentedManagementKeyStrsList',
								'ParentedTeamPathStr',
								'ParentedManagementPathStr',
								'ParentedTotalPathStr',
								'ParentedTopDeriveTeamerVariable'
							]

	def default_init(self,
				_ParentingTopGetVariable=None,
				_ParentingClimbBool=True,
				_ParentedDeriveTeamersList=None,
				_ParentedManagementKeyStrsList=None,
				_ParentedTeamPathStr="",
				_ParentedManagementPathStr="",
				_ParentedTotalPathStr="",
				_ParentedTopDeriveTeamerVariable=None,
				**_KwargVariablesDict
			):	

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_parent(self):

		#debug
		self.debug(('self.',self,[
					#'ManagementPointDeriveTeamer',
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

				#debug
				self.debug('First we make parent the parent')

				#parent the parent
				self.ManagementPointDeriveTeamer.parent(
						self.ParentingTopGetVariable,
						self.ParentingClimbBool
					)

				#debug
				self.debug(
						[
							'Ok parent has parented',
							('self.ManagementPointDeriveTeamer.',
								self.ManagementPointDeriveTeamer,
								['ParentedManagementKeyStrsList']
							)
						]
					)

			#add
			self.ParentedDeriveTeamersList=[
				self.ManagementPointDeriveTeamer
			]+self.ManagementPointDeriveTeamer.ParentedDeriveTeamersList

			#add
			self.ParentedManagementKeyStrsList=[
				self.ManagementKeyStr
			]+self.ManagementPointDeriveTeamer.ParentedManagementKeyStrsList
			self.ParentedManagementKeyStrsList.reverse()

			#debug
			self.debug(
				('self.',self,['ParentedManagementKeyStrsList'])
			)

			#definition
			ParentedTeamPathStrsList=map(
					lambda __ParentedDeriveTeamer:
					__ParentedDeriveTeamer.ManagementKeyStr,
					self.ParentedDeriveTeamersList
				)
			ParentedTeamPathStrsList.reverse()

			#definition
			ParentedTotalPathTuplesList=map(
					lambda __ParentedDeriveTeamer:
					(
						Teamer.TeamChildPrefixStr+__ParentedDeriveTeamer.ManagementTeamKeyStr
						#if __ParentedDeriveTeamer.ManagementTeamKeyStr!=""
						#else ""
						,
						Manager.ManagementChildPrefixStr+__ParentedDeriveTeamer.ManagementKeyStr
						#if __ParentedDeriveTeamer.ManagementKeyStr!=""
						#else ""
					),
					self.ParentedDeriveTeamersList
				)
			ParentedTotalPathTuplesList.reverse()

			#Debug
			self.debug('ParentedTotalPathTuplesList is '+str(ParentedTotalPathTuplesList))
			
			#set
			self.ParentedTeamPathStr=Pather.PathPrefixStr+Pather.PathPrefixStr.join(
				SYS.unzip(ParentedTotalPathTuplesList,[1])
			)
			self.ParentedManagementPathStr=Pather.PathPrefixStr+Pather.PathPrefixStr.join(
				SYS.unzip(ParentedTotalPathTuplesList,[0])
			)
			self.ParentedTotalPathStr=Pather.PathPrefixStr+Pather.PathPrefixStr.join(
				map(
					lambda __ParentedTotalPathTuple:
					__ParentedTotalPathTuple[0
					]+Pather.PathPrefixStr+__ParentedTotalPathTuple[1]
					#if __ParentedTotalPathTuple[0]!=""
					#else __ParentedTotalPathTuple[1]
					,ParentedTotalPathTuplesList
				)
			)

			#Check
			if len(self.ParentedDeriveTeamersList)>0:
				self.ParentedTopDeriveTeamerVariable=self.ParentedDeriveTeamersList[-1]
			else:
				self.ParentedTopDeriveTeamerVariable=self

			#debug
			'''
			self.debug(('self.',self,['ParentingTopGetVariable']))
			'''
			
			#Check
			if self.ParentingTopGetVariable!=None:

				#Check
				if type(self.ParentingTopGetVariable)==list:

					#debug
					'''
					self.debug(
							'This is a list'
						)
					'''
					
					#get
					ParentedValueVariablesList=self.ParentedTopDeriveTeamerVariable[
							'map*get'](
											*self.ParentingTopGetVariable
									).ItemizedMapVariablesList
									
					
					#debug
					'''
					self.debug('ParentedValueVariablesList is '+str(ParentedValueVariablesList))
					'''

					#Link
					self['map*set'](
								zip(
									self.ParentingTopGetVariable,
									ParentedValueVariablesList
								)
						)

				else:

					#Link
					self.set(
							self.ParentingTopGetVariable,
							self.ParentedTopDeriveTeamerVariable[
								self.ParentingTopGetVariable
							]
						)

		else:
			self.ParentedTopDeriveTeamerVariable=self

#</DefineClass>

#Set
SYS.ManagerClass.ManagingValueClass=ParenterClass
