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
BaseModuleStr="ShareYourSystem.Standards.Teamers.Manager"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
from ShareYourSystem.Standards.Itemizers import Pather
#</ImportSpecificModules>

#<DefineLocals>
ParentPreviousStr="^"
ParentTopStr="Top"
ParentAllStr="&$"
#</DefineLocals>

#<DefineClass>
@DecorationClass(
	**{'ClassingSwitchMethodStrsList':['parent']}
)
class ParenterClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
								'ParentingTopGetVariable',
								'ParentingClimbBool',
								'ParentedTotalDeriveTeamersList',
								'ParentedDeriveTeamersList',
								'ParentedDeriveManagersList',
								'ParentedTotalPathStr',
								'ParentedTeamPathStr',
								'ParentedManagementPathStr'
							]

	def default_init(self,
				_ParentingTopGetVariable=None,
				_ParentingClimbBool=True,
				_ParentedTotalDeriveTeamersList=None,
				_ParentedDeriveTeamersList=None,
				_ParentedDeriveManagersList=None,
				_ParentedTotalPathStr="",
				_ParentedTeamPathStr="",
				_ParentedManagementPathStr="",
				**_KwargVariablesDict
			):	

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#init
		self.ParentKeyStr="Top"

		#init
		self.ParentDeriveTeamer=None

		#init
		self.ParentedTotalDeriveTeamersList=[]
		self.ParentedDeriveTeamersList=[]
		self.ParentedDeriveManagersList=[]

		#set
		#self.CommandingBeforeWalkBool=True
		
		#set top
		self.ParentTopDeriveTeamer=self

	def do_parent(self):

		#debug
		'''
		self.debug(('self.',self,[
					#'ManagementPointDeriveTeamer',
					'NameStr'
				]))
		'''

		#get 
		ParentedDeriveTeamerVariable=self.ParentDeriveTeamer

		#Check
		if ParentedDeriveTeamerVariable!=None:

			#/####################/#
			# Check if we have to climb to parent the parent
			#

			#debug
			'''
			self.debug('We are going to parent the parent')
			'''
			
			"""
			#Parent the parent maybe
			if self.ParentingClimbBool:

				#debug
				'''
				self.debug('First we make parent the parent')
				'''
				
				#parent the parent
				ParentedDeriveTeamerVariable.parent(
						self.ParentingTopGetVariable,
						self.ParentingClimbBool
					)

				#debug
				'''
				self.debug(
						[
							'Ok parent has parented',
							'ParentedDeriveTeamerVariable is '+SYS._str(
								ParentedDeriveTeamerVariable
							)
						]
					)
				'''
			"""

			#/####################/#
			# Now build the chain of Teamers and Managers
			#

			#add
			self.ParentedTotalDeriveTeamersList=[
				ParentedDeriveTeamerVariable
			]+ParentedDeriveTeamerVariable.ParentedTotalDeriveTeamersList

			#add
			if self.TeamKeyStr=="":

				#add
				self.ParentedDeriveTeamersList=[
					ParentedDeriveTeamerVariable
				]+ParentedDeriveTeamerVariable.ParentedDeriveTeamersList

				#set
				self.ParentedDeriveManagersList=ParentedDeriveTeamerVariable.ParentedDeriveManagersList

			else:

				#add
				self.ParentedDeriveManagersList=[
					ParentedDeriveTeamerVariable
				]+ParentedDeriveTeamerVariable.ParentedDeriveManagersList

				#set
				self.ParentedDeriveTeamersList=ParentedDeriveTeamerVariable.ParentedDeriveTeamersList

			#map 
			[
				self.ParentedTotalPathStr,
				self.ParentedTeamPathStr,
				self.ParentedManagementPathStr,
			]=map(
				lambda __ParentedList:
				Pather.PathPrefixStr+Pather.PathPrefixStr.join(
					SYS.reverse(
						map(
							lambda __ParentedDeriveTeamer:
							__ParentedDeriveTeamer.ParentKeyStr,
							__ParentedList
						)
					)
				),
				map(
					lambda __KeyStr:
					getattr(self,__KeyStr),
					[
						'ParentedTotalDeriveTeamersList',
						'ParentedDeriveTeamersList',
						'ParentedDeriveManagersList',
					]
				)
			)

			#debug
			self.debug(
					("self.",self,[
							'ParentedTotalPathStr',
							'ParentedTeamPathStr',
							'ParentedManagementPathStr'
						]
					)
				)

			#set

			#/####################/#
			# Set the top teamer variable
			#

			#Check
			if len(self.ParentedTotalDeriveTeamersList)>0:

				#last one
				self.ParentTopDeriveTeamer=self.ParentedTotalDeriveTeamersList[-1]
							
			#debug
			'''
			self.debug(
					('self.',self,['ParentTopDeriveTeamer'])
				)
			'''

			#/####################/#
			# Command things
			#

			#debug
			'''
			self.debug(('self.',self,['ParentingTopGetVariable']))
			'''

			"""
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
					ParentedValueVariablesList=self.ParentTopDeriveTeamer[
							'map*get'](
											*self.ParentingTopGetVariable
									).ItemizedMapValueVariablesList
									
					
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
							self.ParentTopDeriveTeamer[
								self.ParentingTopGetVariable
							]
						)
			"""
		else:

			#set
			self.ParentTopDeriveTeamer=self

	def mimic_team(self):

		#call the base method
		BaseClass.team(self)

		#debug
		'''
		self.debug(
				('self.',self,['TeamingKeyStr'])
			)
		'''
		
		#set
		self.TeamedValueVariable.ParentDeriveTeamer=self
		self.TeamedValueVariable.ParentKeyStr=self.TeamingKeyStr

		#Check
		'''
		if self.ParentKeyStr=='Top':

			#debug
			self.debug('We are the top so we command a parent')

			#command
			self.command(
				['TeamDict.values','ManagementDict.values'],
				('parent',[]),
				_AfterWalkBool=True
			)
		'''
		
	def mimic_manage(self):

		#call the base method
		BaseClass.manage(self)

		#debug
		'''
		self.debug(
				('self.',self,['ManagingKeyStr'])
			)
		'''

		#set
		self.ManagedValueVariable.ParentDeriveTeamer=self
		self.ManagedValueVariable.ParentKeyStr=self.ManagingKeyStr

	def mimic_get(self):
		
		#debug
		'''
		self.debug(
				[
					('self.',self,[
							'GettingKeyVariable',
						])
				]
			)
		'''

		#Check
		if self.GettingKeyVariable==ParentPreviousStr:
			
			#debug
			'''
			self.debug('We get the previous parent')
			'''

			#alias
			self.GettedValueVariable=self.ParentDeriveTeamer

			#Stop the setting
			return {"HookingIsBool":False}

		#Check
		elif self.GettingKeyVariable==ParentTopStr:
			
			#debug
			'''
			self.debug(
				[
					'We get the top parent',
					('self.',self,['ParentTopDeriveTeamer'])
				]
			)
			'''

			#alias
			self.GettedValueVariable=self.ParentTopDeriveTeamer

			#Stop the setting
			return {"HookingIsBool":False}

		#Check
		elif self.GettingKeyVariable==ParentAllStr:

			#add
			self.GettedValueVariable=self.ManagementDict.values()+self.TeamDict.values()

			#Stop the setting
			return {"HookingIsBool":False}

		#debug
		'''
		self.debug(
			[
				'get with the base method',
				'BaseClass is '+str(BaseClass)
			]
		)
		'''

		#Call the base method
		return BaseClass.get(self)

#</DefineClass>

#Set
SYS.ManagerClass.ManagingValueClass=ParenterClass
SYS.TeamerClass.TeamingValueClass=ParenterClass

