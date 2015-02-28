# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Manager completes the list of grand-manage nodes that 
a child node could have. It acts only at one level.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Teamer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
import collections
from ShareYourSystem.Standards.Itemizers import Pather
Teamer=BaseModule
#</ImportSpecificModules>

#<DefineLocals>
ManagementChildPrefixStr="$"
class ManagementDictClass(collections.OrderedDict):
	def __init__(self,_Dict=None):

		#Check
		if _Dict==None:
			_Dict={}

		#call the manage init method
		collections.OrderedDict.__init__(self,_Dict)

		#update
		self.update(_Dict)

SYS.ManagementDictClass=ManagementDictClass
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class ManagerClass(BaseClass):

	def default_init(
				self,
				_TeamTagStr="",
				_ManagementDict=None,
				_ManagingKeyStr="",
				_ManagingValueVariable=None,
				_ManagingValueClass=Teamer.TeamerClass,
				_ManagedValueVariable=None,
				_ManagedIsBool=False,
				_ManagedOnceBool=False,
				**_KwargVariablesDict
			):	

		#Call the manage init method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#Init the ManagementDict
		self.ManagementDict=ManagementDictClass()
		
	def do_manage(self):

		#debug
		'''
		self.debug(
			('self.',self,[
					'ManagingKeyStr',
					'ManagingValueVariable'
				])
		)
		'''

		#/###################/#
		# Force the repr with the ManagementDict
		#

		#Check
		if self.ManagedOnceBool==False:
			self.PrintingInstanceForceKeyStrsList.extend(
				[
					'ManagementDict',
					#'TeamTagStr'
				]
			)
			self.ManagedOnceBool=True

		#/###################/#
		# Add this managed variable
		#

		#Check
		if self.ManagingValueVariable==None:

			#try to get
			try:

				#get
				self.ManagedValueVariable=self.ManagementDict[
					self.ManagingKeyStr
				]

				#set
				self.ManagedIsBool=True
			
			except KeyError:

				#init
				self.ManagedValueVariable=self.ManagingValueClass()

				#set
				self.ManagedIsBool=False

		else:

			#init
			self.ManagedIsBool=False

			#alias
			self.ManagedValueVariable=self.ManagingValueVariable

		#Check
		if self.ManagedIsBool==False:

			#/####################/#
			# Case where it is a dict or tuples list like
			# we wrap then in a teamer new object

			#Check
			if hasattr(
				self.ManagedValueVariable,
				'items'
			) or SYS.getIsTuplesListBool(self.ManagedValueVariable):

				#init
				self.ManagedValueVariable=self.ManagingValueClass(
					)['#map@set'](
						self.ManagedValueVariable
					)

			#define the keystr to define in the dict
			ManagedKeyStr=self.ManagingKeyStr+type(
						self.ManagedValueVariable
					).NameStr

			#set in the __dict__
			self.__setattr__(
					ManagedKeyStr,
					self.ManagedValueVariable
				)

			#add in the RepresentingSkipKeyStrsList to not be seen in the repr
			self.PrintingInstanceSkipKeyStrsList.append(ManagedKeyStr)

			#put in the dict
			self.ManagementDict[
				self.ManagingKeyStr
			]=self.ManagedValueVariable

			##########################
			#give some manage attributes
			#
			
			#set
			self.ManagedValueVariable.ManagementTagStr=self.ManagingKeyStr


	def mimic_get(self):

		#Definition
		OutputDict={'HookingIsBool':True}

		#debug
		'''
		self.debug(
			('self.',self,['GettingKeyVariable'])
		)
		'''
		
		#Check
		if self.GettingKeyVariable==ManagementChildPrefixStr:

			#debug
			'''
			self.debug('We get all the children teams')
			'''

			#return
			self.GettedValueVariable=self.ManagementDict

			#Stop the getting
			return {'HookingIsBool':False}

		elif type(
			self.GettingKeyVariable
		)==str and self.GettingKeyVariable.startswith(
			ManagementChildPrefixStr
		):

			#deprefix
			GetKeyStr=SYS.deprefix(
					self.GettingKeyVariable,
					ManagementChildPrefixStr
				)

			#Check
			if GetKeyStr[0]!='.':

				#debug
				'''
				self.debug('We manage here')
				'''

				#team
				self.GettedValueVariable=self.manage(
					SYS.deprefix(
						self.GettingKeyVariable,
						ManagementChildPrefixStr
					)
				).ManagedValueVariable

				#debug
				'''
				self.debug(
					('self.',self,['GettedValueVariable'])
				)
				'''

				#Stop the getting
				return {'HookingIsBool':False}

			#Check
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
					self.ManagementDict,
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
			ManagementChildPrefixStr
		):

			#debug
			'''
			self.debug('We manage here')
			'''

			#manage
			self.manage(
				SYS.deprefix(
					self.SettingKeyVariable,
					ManagementChildPrefixStr
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
		
		#return 
		return BaseClass.set(self)

#</DefineClass>

#set
SYS.TeamerClass.TeamingValueClass=ManagerClass

#</DefinePrint>
ManagerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'TeamTagStr',
		'ManagementDict',
		'ManagingKeyStr',
		'ManagingValueVariable',
		'ManagingValueClass',
		'ManagedValueVariable',
		'ManagedIsBool',
		'ManagedOnceBool'
	]
)
#<DefinePrint>
