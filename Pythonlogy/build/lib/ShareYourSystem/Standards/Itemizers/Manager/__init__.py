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
ManagementChildPrefixStr="|"
class ManagementDict(collections.OrderedDict):
	def __init__(self,_LiargDict=None,**_KwargDict):

		#Check
		if _LiargDict==None:
			_LiargDict={}

		#call the manage init method
		collections.OrderedDict.__init__(self,_LiargDict,**_KwargDict)

	def get(self,_IndexInt):
		Iterator=self.iterkeys()
		if _IndexInt==0:
			return self[Iterator.next()]
		else:
			return self[map(lambda __Int:Iterator.next(),xrange(_IndexInt+1))[-1]]

SYS.ManagementDict=ManagementDict
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class ManagerClass(BaseClass):

	def default_init(
				self,
				_TeamTagStr="",
				_TeamIndexInt=-1,
				_ManagementDict=None,
				_ManagingKeyStr="",
				_ManagingValueRigidVariable=None,
				_ManagingValueClass=Teamer.TeamerClass,
				_ManagingBeforeSetVariable=None,
				_ManagingAfterSetVariable=None,
				_ManagingClassesDict=None,
				_ManagedValueVariable=None,
				_ManagedInBool=False,
				_ManagedOnceBool=False,
				**_KwargVariablesDict
			):	

		#Call the manage init method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#Init the ManagementDict
		self.ManagementDict=ManagementDict()
		
	def do_manage(self):

		#debug
		'''
		self.debug(
			('self.',self,[
					'ManagingKeyStr',
					'ManagingValueRigidVariable'
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
		# Is it a new managed value
		#

		#in
		self.ManagedInBool=self.ManagingKeyStr in self.ManagementDict

		#debug
		'''
		self.debug(
				[
					'Is it a new managed value ?',
					('self.',self,[
						'ManagingKeyStr',
						'ManagedInBool'
					])
				]
			)
		'''
		
		#Check
		if self.ManagedInBool==False:

			#debug
			'''
			self.debug(
				[
					'This is a new managed value',
					('self.',self,['ManagingKeyStr'])
				]
			)
			'''

			#/####################/#
			# Check if there is a special type for this
			# 

			#debug
			'''
			self.debug(
					[
						'Is there a special type for this',
						('self.',self,['ManagingClassesDict','ManagingKeyStr'])
					]
				)
			'''

			#Check
			if self.ManagingKeyStr in self.ManagingClassesDict:

				#get
				self.ManagingValueClass=self.ManagingClassesDict[
					self.ManagingKeyStr
				]

				#debug
				'''
				self.debug(
						[
							'There is a special type for this',
							('self.',self,['ManagingValueClass'])
						]
					)
				'''

			#/####################/#
			# do we have to init 
			#

			#debug
			'''
			self.debug(
				[
					'This is a new managed value',
					('self.',self,['ManagingKeyStr']),
					'Check first if this managingkey str is known
				]
			)
			'''
			
			#Check
			if self.ManagingValueRigidVariable==None:

				#init
				self.ManagedValueVariable=self.ManagingValueClass()

			else:

				#alias
				self.ManagedValueVariable=self.ManagingValueRigidVariable

			#/####################/#
			# Case where it is a dict or tuples list like
			# we wrap then in a teamer new object

			#Check
			if hasattr(
				self.ManagedValueVariable,
				'items'
			) or SYS.getIsTuplesListBool(self.ManagedValueVariable):

				#debug
				'''
				self.debug(
						[
							'This is a manage with a value dict',
							'We wrap into an instance',
							('self.',self,[
								'ManagingKeyStr',
								'ManagingValueClass',
								'ManagingClassesDict'
								])
						]
					)
				'''

				#Check
				if self.ManagingKeyStr in self.ManagingClassesDict:

					#get
					self.ManagingValueClass=self.ManagingClassesDict[
						self.ManagingKeyStr
					]

					#debug
					'''
					self.debug(
							[
								'There is a special type for this',
								('self.',self,['ManagingValueClass'])
							]
						)
					'''
				
				#temp and init
				ManagedValueVariable=self.ManagedValueVariable
				self.ManagedValueVariable=self.ManagingValueClass()
				
				#Check
				if self.ManagingBeforeSetVariable!=None:

					#debug
					'''
					self.debug(
							[
								'The Manager has something before for the managed value',
								('self.',self,['ManagingBeforeSetVariable'])
							]
						)
					'''
					
					#map set
					self.ManagedValueVariable['#map@set'](
						self.ManagingBeforeSetVariable	
					)

				#debug
				'''
				self.debug(
						[
							'We set the wrapped dicts',
							'ManagedValueVariable is ',
							str(ManagedValueVariable)
						]
					)
				'''

				#set
				self.ManagedValueVariable['#map@set'](
						ManagedValueVariable
					)

				#debug
				'''
				self.debug(
						[
							'Ok the wrapped dict has been setted'
						]
					)
				'''

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

			#/########################/#
			# give some manage attributes
			#

			#set
			self.ManagedValueVariable.ManagementTagStr=self.ManagingKeyStr

			#index
			self.ManagedValueVariable.ManagementIndexInt=len(self.ManagementDict)-1

			#Check
			if self.ManagingAfterSetVariable!=None:

				#debug
				'''
				self.debug(
						[
							'The Manager has something after for the managed value',
							('self.',self,['ManagingAfterSetVariable'])
						]
					)
				'''

				#map set
				self.ManagedValueVariable['#map@set'](
					self.ManagingAfterSetVariable	
				)

		else:

			#/########################/#
			# just get and update 
			#

			#debug
			'''
			self.debug(
					[
						'Ok we just get'
					]
				)
			'''

			#get
			self.ManagedValueVariable=self.ManagementDict[
				self.ManagingKeyStr
			]
			
			#debug
			'''
			self.debug(
					[
						'We maybe update',
						('self.',self,['ManagingValueRigidVariable'])
					]
				)
			'''

			#Check
			if hasattr(
				self.ManagingValueRigidVariable,
				'items'
			) or SYS.getIsTuplesListBool(self.ManagingValueRigidVariable):

				#set
				self.ManagedValueVariable['#map@set'](
						self.ManagingValueRigidVariable
					)

		#/###################/#
		# reset rigid variable
		#

		#set
		self.ManagingValueRigidVariable=None


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
				self.debug(
					[
						'We manage here',
						"SYS.deprefix(self.GettingKeyVariable,ManagementChildPrefixStr) is",
						SYS.deprefix(self.GettingKeyVariable,ManagementChildPrefixStr)
					]
				)
				'''

				#manage
				self.GettedValueVariable=self.manage(
					SYS.deprefix(self.GettingKeyVariable,ManagementChildPrefixStr)
				).ManagedValueVariable

				#debug
				'''
				self.debug(
					[
						'Ok we have managed',
						('self.',self,['GettedValueVariable'])
					]
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
		'TeamIndexInt',
		'ManagementDict',
		'ManagingKeyStr',
		'ManagingValueRigidVariable',
		'ManagingValueClass',
		'ManagingClassesDict',
		'ManagingBeforeSetVariable',
		'ManagingAfterSetVariable',
		'ManagedValueVariable',
		'ManagedInBool',
		'ManagedOnceBool'
	]
)
#<DefinePrint>
