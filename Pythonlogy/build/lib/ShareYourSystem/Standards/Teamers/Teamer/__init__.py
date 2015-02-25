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

	def default_init(self,
				_ManagementTagStr="",
				_TeamDict=None,
				_TeamingKeyStr="",	
				_TeamingValueVariable=None,	
				_TeamingManageVariable=None,					
				_TeamingValueClass=Pointer.PointerClass, 	
				_TeamedValueVariable=None,	
				_TeamedIsBool=False,
				_TeamedOnceBool=False,																
				**_KwargVariablesDict
			):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#init
		self.TeamDict=TeamDictClass()

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

		#/###################/#
		# Force the repr with the ManagementDict
		#

		#Check
		if self.TeamedOnceBool==False:
			self.PrintingInstanceForceKeyStrsList.extend(
				[
					'TeamDict',
					#'ManagementTagStr'
				]
			)
			self.TeamedOnceBool=True

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
				self.TeamedValueVariable=self.TeamingValueClass(
					)['#map@set'](
						self.TeamedValueVariable
					)

			#define the keystr to define in the dict
			TeamedKeyStr=self.TeamingKeyStr+type(
						self.TeamedValueVariable
					).NameStr

			#set in the __dict__
			self.__setattr__(
					TeamedKeyStr,
					self.TeamedValueVariable
				)

			#add in the RepresentingSkipKeyStrsList to not be seen in the repr
			self.PrintingInstanceSkipKeyStrsList.append(TeamedKeyStr)

			#put in the dict
			self.TeamDict[
				self.TeamingKeyStr
			]=self.TeamedValueVariable

			##########################
			#give some team attributes
			#

			#set
			self.TeamedValueVariable.TeamTagStr=self.TeamingKeyStr


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

				#deprefix
				GetKeyStr=SYS.deprefix(
						self.GettingKeyVariable,
						TeamChildPrefixStr
					)

				#Check
				if GetKeyStr[0]!='.':

					#debug
					'''
					self.debug(
						[
							'We team here',
							('self.',self,['GettingKeyVariable'])
						]
					)
					'''

					#team
					self.GettedValueVariable=self.team(
						GetKeyStr
					).TeamedValueVariable

					#Stop the setting
					return {'HookingIsBool':False}

				else:

					#debug
					'''
					self.debug(
						[
							'We team here',
							('self.',self,['GettingKeyVariable'])
						]
					)
					'''

					#team
					self.GettedValueVariable=getattr(
						self.TeamDict,
						GetKeyStr[1:]
					)()

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
			return {'HookingIsBool':False}

		#debug
		'''
		self.debug(
				[
					'Call the base set method',
					'BaseClass is '+str(BaseClass),
					('self.',self,['SettingKeyVariable'])
				]
			)
		'''
		
		#Call the parent get method
		return BaseClass.set(self)

#</DefineClass>


#</DefinePrint>
TeamerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'ManagementTagStr',
		'TeamDict',
		'TeamingKeyStr',
		'TeamingValueVariable',
		'TeamingManageVariable',
		'TeamingValueClass',
		'TeamedValueVariable',
		'TeamedIsBool',
		'TeamedOnceBool'
	]
)
#<DefinePrint>
