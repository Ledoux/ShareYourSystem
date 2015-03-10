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
TeamChildPrefixStr='-'
class TeamDict(collections.OrderedDict):
	def __init__(self,_LiargDict=None,**_KwargDict):

		#Check
		if _LiargDict==None:
			_LiargDict={}

		#call the parent init method
		collections.OrderedDict.__init__(self,_LiargDict,**_KwargDict)

	def get(self,_IndexInt):
		Iterator=self.iterkeys()
		if _IndexInt==0:
			return self[Iterator.next()]
		else:
			return self[map(lambda __Int:Iterator.next(),xrange(_IndexInt+1))[-1]]

SYS.TeamDict=TeamDict
#</DefineLocals>


#<DefineClass>
@DecorationClass()
class TeamerClass(BaseClass):

	def default_init(self,
				_ManagementTagStr="",
				_ManagementIndexInt=-1,
				_TeamDict=None,
				_TeamingKeyStr="",	
				_TeamingValueVariable=None,	
				_TeamingManageVariable=None,					
				_TeamingValueClass=Pointer.PointerClass, 	
				_TeamingClassesDict=None,
				_TeamingBeforeSetVariable=None,
				_TeamingAfterSetVariable=None,
				_TeamedValueVariable=None,	
				_TeamedIsBool=False,
				_TeamedOnceBool=False,																
				**_KwargVariablesDict
			):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#init
		self.TeamDict=TeamDict()

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

		
		#/###################/#
		# Is it a new teamed value
		#

		#in
		self.TeamedIsBool=self.TeamingKeyStr in self.TeamDict

		#Check
		if self.TeamedIsBool==False:

			#debug
			'''
			self.debug(
				[
					'This is a new teamed value',
					('self.',self,['TeamingKeyStr'])
				]
			)
			'''

			#/####################/#
			# do we have to init 
			#

			#Check
			if self.TeamingValueVariable==None:

				#init
				self.TeamedValueVariable=self.TeamingValueClass()

			else:

				#alias
				self.TeamedValueVariable=self.TeamingValueVariable

			#/####################/#
			# Case where it is a dict or tuples list like
			# we wrap then in a manager new object

			#Check
			if hasattr(
				self.TeamedValueVariable,
				'items'
			) or SYS.getIsTuplesListBool(self.TeamedValueVariable):

				#debug
				'''
				self.debug(
						[
							'This is a team with a value dict',
							'We wrap into an instance',
							('self.',self,[
								'TeamingKeyStr',
								'TeamingValueClass',
								'TeamingClassesDict'
								])
						]
					)
				'''

				#Check
				if self.TeamingKeyStr in self.TeamingClassesDict:

					#get
					self.TeamingValueClass=self.TeamingClassesDict[
						self.TeamingKeyStr
					]

					#debug
					'''
					self.debug(
							[
								'There is a special type for this',
								('self.',self,['TeamingValueClass'])
							]
						)
					'''
					
				#temp and init
				TeamedValueVariable=self.TeamedValueVariable
				self.TeamedValueVariable=self.TeamingValueClass()

				#Check
				if self.TeamingBeforeSetVariable!=None:

					#debug
					'''
					self.debug(
						[
							'The Teamer has something before for the teamed value',
							('self.',self,['TeamingBeforeSetVariable'])
						]
					)
					'''

					#map set
					self.TeamedValueVariable['#map@set'](
						self.TeamingBeforeSetVariable	
					)

				#set
				self.TeamedValueVariable['#map@set'](
						TeamedValueVariable
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

			#index
			self.TeamedValueVariable.TeamIndexInt=len(self.TeamDict)-1

			#Check
			if self.TeamingAfterSetVariable!=None:

				#debug
				'''
				self.debug(
						[
							'The Teamed has something after for the teamed value',
							('self.',self,['TeamingAfterSetVariable'])
						]
					)
				'''

				#map set
				self.TeamedValueVariable['#map@set'](
					self.TeamingAfterSetVariable	
				)

		else:

			##########################
			# just get
			#

			#get
			self.TeamedValueVariable=self.TeamDict[self.TeamingKeyStr]


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
		)==str:

			#Check
			if self.SettingKeyVariable.startswith(
				TeamChildPrefixStr
			):

				#debug
				'''
				self.debug(
					[
						'We team here',
						('self.',self,['SettingKeyVariable'])
					]
				)
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
		'ManagementIndexInt',
		'TeamDict',
		'TeamingKeyStr',
		'TeamingValueVariable',
		'TeamingClassesDict',
		'TeamingManageVariable',
		'TeamingClassesDict',
		'TeamingValueClass',
		'TeamingBeforeSetVariable',
		'TeamingAfterSetVariable',
		'TeamedValueVariable',
		'TeamedIsBool',
		'TeamedOnceBool'
	]
)
#<DefinePrint>
