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
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Filterer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
from ShareYourSystem.Standards.Itemizers import Pather
from ShareYourSystem.Standards.Teamers import Manager
#</ImportSpecificModules>

#<DefineLocals>
TeamPrefixStr='*'
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
				_TeamingValueClass=Manager.ManagerClass, 	
				_TeamedValueVariable=None,																	
				**_KwargVariablesDict
			):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#init
		self.TeamDict=TeamDictClass()

		##########################
		#init some management attributes
		#

		#Init
		self.ManagementKeyStr=""

		#point
		self.ManagementPointDeriveManager=None

	
	def do_team(self):

		#debug
		self.debug(
			('self.',self,[
					'TeamingKeyStr',
					'TeamingValueVariable'
				])
		)

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

			#set in the __dict__
			self.__setattr__(
					TeamPrefixStr+self.TeamingKeyStr+type(
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

			#debug
			'''
			self.debug(
				'We make point the teamed instance to self'
			)
			'''

			#set
			'''
			self.TeamedValueVariable.point(
					self,
					'TeamPointDeriveTeamer'
				)
			'''
			self.TeamedValueVariable.TeamPointDeriveTeamer=self
				
			#debug
			'''
			self.debug(
				'Ok it is pointed'
			)	
			'''

			#set
			self.TeamedValueVariable.__setattr__(
				'TeamKeyStr',
				self.TeamingKeyStr
			)


	def mimic_get(self):

		#Definition
		OutputDict={'HookingIsBool':True}

		#debug
		self.debug(('self.',self,['GettingKeyVariable']))

		#Check
		if type(
			self.GettingKeyVariable
		)==str and self.GettingKeyVariable.startswith(TeamPrefixStr):

			#debug
			self.debug('We team here')

			#team
			self.GettedValueVariable=self.team(
				SYS.deprefix(
					self.GettingKeyVariable,
					TeamPrefixStr
				)
			).TeamedValueVariable

			#Stop the setting
			OutputDict["HookingIsBool"]=False 

		#Call the parent get method
		if OutputDict['HookingIsBool']:
			return BaseClass.get(self)

	def mimic_set(self):

		#Definition
		OutputDict={'HookingIsBool':True}

		#debug
		self.debug(('self.',self,['SettingKeyVariable']))

		#Check
		if type(
			self.SettingKeyVariable
		)==str and self.SettingKeyVariable.startswith(TeamPrefixStr):

			#debug
			self.debug('We team here')

			#team
			self.team(
				SYS.deprefix(
					self.SettingKeyVariable,
					TeamPrefixStr
				),
				self.SettingValueVariable
			)

			#Stop the setting
			OutputDict["HookingIsBool"]=False 

		#Call the parent get method
		if OutputDict['HookingIsBool']:
			return BaseClass.set(self)

#</DefineClass>

#set
SYS.ManagerClass.ManagingValueClass=TeamerClass