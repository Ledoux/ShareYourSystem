# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Teamer defines Child ordered dicts with <DoStr> as KeyStr. 
The items inside are automatically setted with Teamed<DoStr><TypeStr> and have 
a Pointer to the parent InstanceVariable. This is the beginning for buiding high
arborescent and (possibly circular) structures of objects.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Pointer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
from ShareYourSystem.Standards.Itemizers import Pather,Pointer
#</ImportSpecificModules>

#<DefineLocals>
TeamChildPrefixStr='&'
class TeamDictClass(collections.OrderedDict):
	def __init__(self,_Dict=None):

		#Check
		if _Dict==None:
			_Dict={}

		#call the parent init method
		collections.OrderedDict.__init__(self,_Dict)

		#update
		self.update(_Dict)

SYS.TeamDictClass=TeamDictClass
#</DefineLocals>


#<DefineClass>
@DecorationClass()
class TeamerClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
								'TeamingKeyStr',
								'TeamingValueVariable',
								'TeamingManageVariable',
								'TeamingValueClass',
								'TeamedValueVariable'
							]

	def default_init(self,
				_TeamingKeyStr="",	
				_TeamingValueVariable=None,	
				_TeamingManageVariable=None,					
				_TeamingValueClass=Pointer.PointerClass, 	
				_TeamedValueVariable=None,																	
				**_KwargVariablesDict
			):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#init
		self.TeamDict=TeamDictClass()

		#init
		self.ManagementKeyStr=""

	def do_team(self):

		#debug
		'''
		self.debug(
			('self.',self,[
					'TeamingKeyStr',
					'TeamingValueVariable'
				])
		)
		'''

		#Check
		if self.TeamingValueVariable==None:

			#try to get
			try:

				#get
				self.TeamedValueVariable=self.TeamDict[
					self.TeamingKeyStr
				]

				#set
				self.TeamedIsBool=True
			
			except KeyError:

				#init
				self.TeamedValueVariable=self.TeamingValueClass()

				#set
				self.TeamedIsBool=False

		else:

			#init
			self.TeamedIsBool=False

			#alias
			self.TeamedValueVariable=self.TeamingValueVariable

		#Check
		if self.TeamedIsBool==False:

			#/####################/#
			# Case where it is a dict or tuples list like
			# we wrap then in a manager new object

			#Check
			if hasattr(
				self.TeamedValueVariable,
				'items'
			) or SYS.getIsTuplesListBool(self.TeamedValueVariable):

				#init
				self.TeamedValueVariable=Manager.ManagerClass(
					)['map*set'](
						self.TeamedValueVariable
					)

			#set in the __dict__
			self.__setattr__(
					self.TeamingKeyStr+type(
						self.TeamedValueVariable
					).NameStr,
					self.TeamedValueVariable
				)

			#put in the dict
			self.TeamDict[
				self.TeamingKeyStr
			]=self.TeamedValueVariable

			##########################
			#give some team attributes
			#

			#set
			self.TeamedValueVariable.TeamKeyStr=self.TeamingKeyStr


	def mimic_get(self):

		#Definition
		OutputDict={'HookingIsBool':True}

		#debug
		'''
		self.debug(('self.',self,['GettingKeyVariable']))
		'''

		#Check
		if type(
			self.GettingKeyVariable
		)==str:

			#Check
			if self.GettingKeyVariable==TeamChildPrefixStr:

				#return 
				self.GettedValueVariable=self.TeamDict

				#Stop the setting
				return {'HookingIsBool':False}

			elif self.GettingKeyVariable.startswith(TeamChildPrefixStr):

				#debug
				'''
				self.debug('We team here')
				'''

				#team
				self.GettedValueVariable=self.team(
					SYS.deprefix(
						self.GettingKeyVariable,
						TeamChildPrefixStr
					)
				).TeamedValueVariable

				#Stop the setting
				return {'HookingIsBool':False}

		#Call the parent get method
		return BaseClass.get(self)

	def mimic_set(self):

		#Definition
		OutputDict={'HookingIsBool':True}

		#debug
		'''
		self.debug(('self.',self,['SettingKeyVariable']))
		'''

		#Check
		if type(
			self.SettingKeyVariable
		)==str and self.SettingKeyVariable.startswith(
			TeamChildPrefixStr
		):

			#debug
			'''
			self.debug('We team here')
			'''
			
			#team
			self.team(
				SYS.deprefix(
					self.SettingKeyVariable,
					TeamChildPrefixStr
				),
				self.SettingValueVariable
			)

			#Stop the setting
			OutputDict["HookingIsBool"]=False 

		#Call the parent get method
		if OutputDict['HookingIsBool']:
			return BaseClass.set(self)

#</DefineClass>
